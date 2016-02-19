#!/usr/bin/env python

import distutils.core
distutils.core.setup (
		name = 'pcb',
		packages = ['pcb', 'pcb.bbb', 'pcb.avr'],
		version = '0.1',
		description = 'Generate KiCAD files for pcbnew',
		author = 'Bas Wijnen',
		author_email = 'wijnen@debian.org',
		)
