# Module to allow replacing eeschema with a python script.
# Import this module, create parts and write a netlist.
# Then use this netlist to create a pcb with pcbnew.

import sys
import os
import time

POWER_OUT = 'power_out'
POWER_IN = 'power_in'
POWER_GND = 'power_gnd'
OUT = 'output'
IN = 'input'
PASSIVE = 'passive'
BI = 'BiDi'
UNSPECIFIED = 'unspc'
THREESTATE = '3state'

nets = {}
_anon_nets = []

_components = {}
_libparts = {}

_lastref = {}

def check(cond, msg):
	if cond:
		return
	sys.stderr.write('Error: %s\n' % msg)
	sys.exit(1)

def _mk_ref(base):
	if base not in _lastref:
		_lastref[base] = 0
	_lastref[base] += 1
	return base + '%d' % _lastref[base]

class Net:
	def __init__(self, name):
		self.pins = []
		self.realpins = 0
		self.sparse = False
		self.used = False
		if name is None:
			self.anon = True
			self.name = '(anon)'
			_anon_nets.append(self)
		else:
			name = str(name)
			check(name not in nets, 'duplicate net name %s' % name)
			self.anon = False
			self.name = name
			nets[name] = self
	def merge(self, other):
		check(other.anon, 'merging named net %s with other named net %s' % (self.name, other.name))
		self.realpins += other.realpins
		self.used = True
		for p in other.pins:
			self.pins.append(p)
			p.net = self
		_anon_nets.remove(other)

class Pin:
	def __init__(self, part, name, type = PASSIVE):
		self.part = part
		self.name = name
		self.net = Net(None)
		self.net.pins.append(self)
		self.type = type

def _add_pin(pin, value, addpin, addalias):
	if isinstance(pin, tuple):
		name = str(pin[0])
		addpin(name, value)
		for a in pin[1:]:
			addalias(str(a), name)
	else:
		name = str(pin)
		addpin(name, value)

def _add(pins, add, alias):
	if isinstance(pins, dict):
		for p in pins:
			_add_pin(p, pins[p], add, alias)
	elif isinstance(pins, int):
		for p in range(1, pins + 1):
			_add_pin(p, UNSPECIFIED, add, alias)
	elif isinstance(pins, (tuple, list)):
		for p, t in enumerate(pins):
			_add_pin(p + 1, t, add, alias)
	else:
		raise TypeError('invalid argument type for Part')

class Part:
	def __init__(self, name, pins, module = None):
		self.name = name
		self.pins = {}
		self.desc = ''
		self.fields = {'Reference': name[0], 'Value': name}
		self.alias = {}
		self.module = module or name
		_add(pins, self._add_pin, self._add_alias)
		_libparts[name] = self
	def _add_pin(self, name, type):
		check(name not in self.pins and name not in self.alias, 'duplicate pin name %s' % name)
		self.pins[name] = type
	def _add_alias(self, name, orig):
		check(name not in self.pins and name not in self.alias, 'duplicate alias %s' % name)
		check(orig in self.pins or orig in self.alias, 'nonexistant alias target %s' % orig)
		self.alias[name] = orig if orig in self.pins else self.alias[orig]
	def __call__(self, name = None, module = None):
		if name is None:
			name = _mk_ref(self.fields['Reference'])
		ret = group((), name, self, module or self.module, init = False)
		ret._init({p: Pin(ret, p, self.pins[p]) for p in self.pins}, module or self.module, self.alias, real = True)
		return ret

class group:
	def __init__(self, pins, name = None, part = None, module = None, alias = None, init = True):
		self.name = name
		self.part = part
		self.pins = {}
		self.alias = {}
		if init:
			self._init(pins, module, alias)
	def _init(self, pins, module, alias, real = False):
		_add(pins, lambda name, pin: self._add_pin(name, pin, real), self._add_alias)
		if alias:
			for a in alias:
				self._add_alias(a, alias[a])
		self.module = module
		check(self.name not in _components, 'component name %s redefined' % self.name)
		_components[self.name] = self
	def _add_pin(self, name, pin, real):
		check(name not in self.pins and name not in self.alias, 'duplicate pin %s added' % name)
		if isinstance(pin, Pin):
			self.pins[name] = pin
		else:
			self.pins[name] = Pin(self, name, pin)
		if real:
			self.pins[name].net.realpins += 1
	def _add_alias(self, name, orig):
		check(name not in self.pins and name not in self.alias, 'duplicate alias %s added' % name)
		check(orig in self.pins or orig in self.alias, 'nonexistant alias target %s added' % orig)
		self.alias[name] = orig if orig in self.pins else self.alias[orig]
	def __setitem__(self, item, value):
		item = str(item)
		if isinstance(value, (tuple, list)):
			check(value is not None, 'cannot assign netname to no-connect pin')
			value, netname = value
			check(isinstance(value, Pin), 'name target %s must be a pin' % item)
			Net(netname).merge(value.net)
		if isinstance(value, Pin):
			value = value.net
		try:
			pin = self[item]
		except:
			sys.stderr.write('Error: using undeclared pin %s:%s\n' % (self.name, item))
			pin = Pin(self, item)
			self.pins[item] = pin
		check(pin.net is not None or value is None, 'pin %s:%s assigned to %s, but was already marked as not connected' % (self.name, item, value.name if value is not None else ''))
		if value is None:
			check(pin.net is None or pin.net.anon, 'pin %s:%s marked as not connected, but was already connected to %s' % (self.name, item, pin.net.name if pin.net is not None else ''))
			if pin.net.anon:
				_anon_nets.remove(pin.net)
			pin.net = None
		elif value.anon:
			pin.net.merge(value)
		else:
			check(pin.net.anon, 'merging named nets %s and %s through assignment' % (pin.net.name, value.name))
			value.merge(pin.net)
	def __getitem__(self, item):
		item = str(item)
		if item in self.pins:
			return self.pins[item]
		if item in self.alias and self.alias[item] in self.pins:
			return self.pins[self.alias[item]]
		raise KeyError('key %s not found' % item)
	def __contains__(self, item):
		if item in self.pins:
			return True
		if item in self.alias and self.alias[item] in self.pins:
			return True
		return False
	def sparse(self):
		for p in self.pins:
			if self.pins[p].net is not None:
				self.pins[p].net.sparse = True

def check_pin(type, name, state, pinname):
	# State:
	# [0]: have_output
	# [1]: None=nothing, False=need_power_out, True=have_power_out
	# [2]: List of output pins.
	if len(state) == 0:
		state.extend((False, None, []))
	check(any(type is x for x in (None, POWER_OUT, POWER_IN, POWER_GND, OUT, IN, PASSIVE, BI, UNSPECIFIED, THREESTATE)), 'invalid pin type %s' % type)
	if type in (POWER_OUT, UNSPECIFIED):
		state[1] = True
	if type is POWER_IN and state[1] is None:
		state[1] = False
	if type in (POWER_OUT, OUT):
		state[0] = True
		state[2].append(pinname)
	if type in (BI, THREESTATE, UNSPECIFIED, PASSIVE, POWER_GND):
		state[0] = True
	if type is None:
		if not state[0]:
			sys.stderr.write('Error: net %s contains no driving pins.\n' % name)
		if state[1] is False:
			sys.stderr.write('Error: net %s contains power input, but no power output.\n' % name)
		if len(state[2]) > 1:
			sys.stderr.write('Error: net %s contains multiple driving pins: %s.\n' % (name, ', '.join(state[2])))

def write(base):
	with open(base + os.extsep + 'net', 'w') as net:
		net.write('(export (version D)')
		net.write('\n  (design')
		net.write('\n    (source %s)' % sys.argv[0])
		net.write('\n    (date %s)' % time.asctime(time.gmtime()))
		net.write('\n    (tool %s))' % 'Python pcb module')
		net.write('\n  (components')
		comps = [c for c in _components.keys() if c]
		comps.sort()
		for c in comps:
			if _components[c].module is None:
				continue
			net.write('\n    (comp (ref %s)' % c)
			net.write('\n      (value %s)' % _components[c].part.name)
			net.write('\n      (footprint %s)' % _components[c].module)
			net.write('\n      (libsource (lib generated) (part %s))' % _components[c].part.name)
			net.write('\n      (sheetpath (names /) (tstamps /))')
			net.write('\n      (tstamp 55AE2970))')
		net.write(')')
		net.write('\n  (libparts')
		for p in _libparts:
			net.write('\n    (libpart (lib generated) (part %s)' % p)
			net.write('\n      (description "%s")' % _libparts[p].desc)
			net.write('\n      (fields')
			for f in _libparts[p].fields:
				net.write('\n        (field (name %s) %s)' % (f, _libparts[p].fields[f]))
			net.write(')')
			net.write('\n      (pins')
			for pin in _libparts[p].pins:
				net.write('\n        (pin (num %s) (name %s) (type %s))' % (pin, pin, _libparts[p].pins[pin]))
			net.write(')')
			net.write(')')
		net.write(')')
		net.write('\n  (libraries')
		net.write('\n    (library (logical generated)')
		net.write('\n    (uri /generated.lib)))')
		net.write('\n  (nets')
		for i, n in enumerate(nets):
			pins = [p for p in nets[n].pins if p.part.module is not None]
			netname = '%s (%s)' % (n, ', '.join('%s:%s(%s)' % (node.part.name, node.name, node.type) for node in nets[n].pins))
			if len(pins) < 2:
				if not nets[n].sparse:
					sys.stderr.write('unconnected named net %s not marked as no-connect\n' % netname)
				continue
			net.write('\n    (net (code %d) (name %s)' % (i, n))
			state = []
			for node in pins:
				check_pin(node.type, netname, state, '%s:%s' % (node.part.name, node.name))
				net.write('\n      (node (ref %s) (pin %s))' % (node.part.name, node.name))
			check_pin(None, netname, state, None)
			net.write(')')
		for i, n in enumerate(_anon_nets):
			pins = [p for p in n.pins if p.part.module is not None]
			netname = ', '.join('%s:%s(%s)' % (node.part.name, node.name, node.type) for node in n.pins)
			if len(pins) < 2:
				if not n.sparse:
					sys.stderr.write('pin %s is not connected and not marked no-connect\n' % netname)
				continue
			if n.used:
				sys.stderr.write('Warning: anonymous net found on %s\n' % netname)
			net.write('\n    (net (code %d) (name _net_%d)' % (i, i))
			state = []
			for node in pins:
				check_pin(node.type, netname, state, '%s:%s' % (node.part.name, node.name))
				net.write('\n      (node (ref %s) (pin %s))' % (node.part.name, node.name))
			check_pin(None, netname, state, None)
			net.write(')')
		net.write(')')
		net.write(')\n')
