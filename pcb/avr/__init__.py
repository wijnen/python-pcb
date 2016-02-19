import pcb

def atmega1284p(name = 'avr', avcc = False, pdip = True):
	if pdip:
		ret = pcb.Part('Housings_DIP:DIP-40_W15.24mm_LongPads', {
			(1, 'pb0', 'pcint8', 'xck0', 't0'): pcb.BI,
			(2, 'pb1', 'pcint9', 'clko', 't1'): pcb.BI,
			(3, 'pb2', 'pcint10', 'int2', 'ain0'): pcb.BI,
			(4, 'pb3', 'pcint11', 'oc0a', 'ain1'): pcb.BI,
			(5, 'pb4', 'pcint12', 'oc0b', 'ss'): pcb.BI,
			(6, 'pb5', 'pcint13', 'icp3', 'mosi'): pcb.BI,
			(7, 'pb6', 'pcint14', 'oc3a', 'miso'): pcb.BI,
			(8, 'pb7', 'pcint15', 'oc3b', 'sck'): pcb.BI,
			(9, 'reset'): pcb.IN,
			(10, 'vcc'): pcb.POWER_IN,
			(11, 'gnd'): pcb.POWER_GND,
			(12, 'xtal2'): pcb.OUT,
			(13, 'xtal1'): pcb.IN,
			(14, 'pd0', 'pcint24', 'rxd0', 't3'): pcb.BI,
			(15, 'pd1', 'pcint25', 'txd0'): pcb.BI,
			(16, 'pd2', 'pcint26', 'rxd1', 'int0'): pcb.BI,
			(17, 'pd3', 'pcint27', 'txd1', 'int1'): pcb.BI,
			(18, 'pd4', 'pcint28', 'xck1', 'oc1b'): pcb.BI,
			(19, 'pd5', 'pcint29', 'oc1a'): pcb.BI,
			(20, 'pd6', 'pcint30', 'oc2b', 'icp'): pcb.BI,
			(21, 'pd7', 'pcint31', 'oc2a'): pcb.BI,
			(22, 'pc0', 'pcint16', 'scl'): pcb.BI,
			(23, 'pc1', 'pcint17', 'sda'): pcb.BI,
			(24, 'pc2', 'pcint18', 'tck'): pcb.BI,
			(25, 'pc3', 'pcint19', 'tms'): pcb.BI,
			(26, 'pc4', 'pcint20', 'tdo'): pcb.BI,
			(27, 'pc5', 'pcint21', 'tdi'): pcb.BI,
			(28, 'pc6', 'pcint22', 'tosc1'): pcb.BI,
			(29, 'pc7', 'pcint23', 'tosc2'): pcb.BI,
			(30, 'avcc'): pcb.POWER_IN,
			(31, 'gnd2'): pcb.POWER_GND,
			(32, 'aref'): pcb.IN,
			(33, 'pa7', 'pcint7', 'adc7'): pcb.BI,
			(34, 'pa6', 'pcint6', 'adc6'): pcb.BI,
			(35, 'pa5', 'pcint5', 'adc5'): pcb.BI,
			(36, 'pa4', 'pcint4', 'adc4'): pcb.BI,
			(37, 'pa3', 'pcint3', 'adc3'): pcb.BI,
			(38, 'pa2', 'pcint2', 'adc2'): pcb.BI,
			(39, 'pa1', 'pcint1', 'adc1'): pcb.BI,
			(40, 'pa0', 'pcint0', 'adc0'): pcb.BI,
			})(name)
	else:
		raise NotImplementedError('Only PDIP atmega1284p is implemented at this moment.')
	ret['gnd2'] = ret['gnd']
	ret['gnd'].net.used = False
	if not avcc:
		ret['avcc'] = ret['vcc']
		ret['vcc'].net.used = False
	return ret

def atmega328p(name = 'avr', avcc = False):
	ret = pcb.Part('Housings_QFP:TQFP-32_7x7mm_Pitch0.8mm', {
		(1, 'pcint19', 'oc2b', 'int1', 'pd3'): pcb.BI,
		(2, 'pcint20', 'xck', 't0', 'pd4'): pcb.BI,
		(3, 'gnd'): pcb.POWER_GND,
		(4, 'vcc'): pcb.POWER_IN,
		5: pcb.POWER_GND,
		6: pcb.POWER_IN,
		(7, 'pcint6', 'xtal1', 'tosc1', 'pb6'): pcb.BI,
		(8, 'pcint7', 'xtal2', 'tosc2', 'pb7'): pcb.BI,
		(9, 'pcint21', 'oc0b', 't1', 'pd5'): pcb.BI,
		(10, 'pcint22', 'oc0a', 'ain0', 'pd6'): pcb.BI,
		(11, 'pcint23', 'ain1', 'pd7'): pcb.BI,
		(12, 'pcint0', 'clko', 'icp1', 'pb0'): pcb.BI,
		(13, 'pcint1', 'oc1a', 'pb1'): pcb.BI,
		(14, 'pcint2', 'ss', 'oc1b', 'pb2'): pcb.BI,
		(15, 'pcint3', 'oc2a', 'mosi', 'pb3'): pcb.BI,
		(16, 'pcint4', 'miso', 'pb4'): pcb.BI,
		(17, 'pcint5', 'sck', 'pb5'): pcb.BI,
		(18, 'avcc'): pcb.POWER_IN,
		(19, 'adc6'): pcb.BI,
		(20, 'aref'): pcb.IN,
		21: pcb.POWER_GND,
		(22, 'adc7'): pcb.BI,
		(23, 'pcint8', 'adc0', 'pc0'): pcb.BI,
		(24, 'pcint9', 'adc1', 'pc1'): pcb.BI,
		(25, 'pcint10', 'adc2', 'pc2'): pcb.BI,
		(26, 'pcint11', 'adc3', 'pc3'): pcb.BI,
		(27, 'pcint12', 'sda', 'adc4', 'pc4'): pcb.BI,
		(28, 'pcint13', 'scl', 'adc5', 'pc5'): pcb.BI,
		(29, 'pcint14', 'reset', 'pc6'): pcb.BI,
		(30, 'pcint16', 'rxd', 'pd0'): pcb.BI,
		(31, 'pcint17', 'txd', 'pd1'): pcb.BI,
		(32, 'pcint18', 'int0', 'pd2'): pcb.BI,
		})(name)
	for pin in 5, 21:
		ret[pin] = ret['gnd']
	ret['gnd'].net.used = False
	ret[6] = ret['vcc']
	if not avcc:
		ret['avcc'] = ret['vcc']
	ret['vcc'].net.used = False
	return ret

def atxmega128d4(name = 'avr', avcc = False):
	ret = pcb.Part('Housings_QFP:TQFP-44_10x10mm_Pitch0.8mm', {
		(8, 'gnd'): pcb.BI,
		18: pcb.BI,
		30: pcb.BI,
		38: pcb.BI,
		(9, 'vcc'): pcb.BI,
		19: pcb.BI,
		31: pcb.BI,
		(39, 'avcc'): pcb.BI,

		(34, 'pdi_data'): pcb.BI,
		(35, 'pdi_clock', 'reset'): pcb.BI,
		(36, 'pr0', 'xtal2', 'tosc2'): pcb.BI,
		(37, 'pr1', 'xtal1', 'tosc1'): pcb.BI,

		(40, 'pa0', 'adc0', 'ac0', 'aref0'): pcb.BI,
		(41, 'pa1', 'adc1', 'ac1'): pcb.BI,
		(42, 'pa2', 'adc2', 'ac2'): pcb.BI,
		(43, 'pa3', 'adc3', 'ac3'): pcb.BI,
		(44, 'pa4', 'adc4', 'ac4'): pcb.BI,
		(1, 'pa5', 'adc5', 'ac5'): pcb.BI,
		(2, 'pa6', 'adc6', 'ac6'): pcb.BI,
		(3, 'pa7', 'adc7', 'ac7', 'ac0out'): pcb.BI,

		(4, 'pb0', 'adc8', 'aref1'): pcb.BI,
		(5, 'pb1', 'adc9'): pcb.BI,
		(6, 'pb2', 'adc10'): pcb.BI,
		(7, 'pb3', 'adc11'): pcb.BI,

		(10, 'pc0', 'oc0a_c', 'oc0als', 'sda_c'): pcb.BI,
		(11, 'pc1', 'oc0b_c', 'oc0ahs', 'xck0_c', 'scl_c'): pcb.BI,
		(12, 'pc2', 'oc0c_c', 'oc0bls', 'rxd0_c'): pcb.BI,
		(13, 'pc3', 'oc0d_c', 'oc0bhs', 'txd0_c'): pcb.BI,
		(14, 'pc4', 'oc0cls', 'oc1a', 'ss_c'): pcb.BI,
		(15, 'pc5', 'oc0chs', 'oc1b', 'mosi_c'): pcb.BI,
		(16, 'pc6', 'oc0dls', 'miso_c', 'clkrtc'): pcb.BI,
		(17, 'pc7', 'oc0dhs', 'sck_c', 'clkper_c', 'evout_c'): pcb.BI,

		(20, 'pd0', 'oc0a_d'): pcb.BI,
		(21, 'pd1', 'oc0b_d', 'xck0_d'): pcb.BI,
		(22, 'pd2', 'oc0c_d', 'rxd0_d'): pcb.BI,
		(23, 'pd3', 'oc0d_d', 'txd0_d'): pcb.BI,
		(24, 'pd4', 'ss_d'): pcb.BI,
		(25, 'pd5', 'mosi_d'): pcb.BI,
		(26, 'pd6', 'miso_d'): pcb.BI,
		(27, 'pd7', 'sck_d', 'clkper_d', 'evout_d'): pcb.BI,

		(28, 'pe0', 'oc0a_e', 'sda_e'): pcb.BI,
		(29, 'pe1', 'oc0b_e', 'scl_e'): pcb.BI,
		(32, 'pe2', 'oc0c_e'): pcb.BI,
		(33, 'pe3', 'oc0d_e'): pcb.BI,
		})(name)
	ret['gnd'] = ret[18]
	ret['gnd'] = ret[30]
	ret['gnd'] = ret[38]
	ret['gnd'].net.used = False
	ret['vcc'] = ret[19]
	ret['vcc'] = ret[31]
	if not avcc:
		ret['vcc'] = ret['avcc']
	ret['vcc'].net.used = False
	return ret
