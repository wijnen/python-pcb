# vim: set foldmethod=marker :
import pcb

def bbb(base = 'bbb', flash = True, hdmi = False, J1 = False, P8 = True, P9 = True):
	bbb_pins = {}
	gnd_pins = ['gnd']
	if P8:
		bbb_pins.update({
			(22, '0.22', 'P8_19', 'ehrpwm2a_1', 'mmc2_dat4', 'mmc1_dat0', 'lcd_data23', 'gpmc_ad8'): pcb.BI,
			(23, '0.23', 'P8_13', 'ehrpwm2b_1', 'mmc2_dat5', 'mmc1_dat1', 'lcd_data22', 'gpmc_ad9'): pcb.BI,
			(26, '0.26', 'P8_14', 'ehrpwm2_tripzone_in_1', 'mmc2_dat6', 'mmc1_dat2', 'lcd_data21', 'gpmc_ad10'): pcb.BI,
			(27, '0.27', 'P8_17', 'ehrpwm0_synco_0', 'mmc2_dat7', 'mmc1_dat3', 'lcd_data20', 'gpmc_ad11'): pcb.BI,
			(44, '1.12', 'P8_12', 'pru0o14', 'eQEP2a_in_1', 'mmc2_dat0', 'mmc1_dat4', 'lcd_data19', 'gpmc_ad12'): pcb.BI,
			(45, '1.13', 'P8_11', 'pru0o15', 'eQEP2b_in_1', 'mmc2_dat1', 'mmc1_dat5', 'lcd_data18', 'gpmc_ad13'): pcb.BI,
			(46, '1.14', 'P8_16', 'pru0i14', 'eQEP2_index_1', 'mmc2_dat2', 'mmc1_dat6', 'lcd_data17', 'gpmc_ad14'): pcb.BI,
			(47, '1.15', 'P8_15', 'pru0i15', 'eQEP2_strobe_1', 'mmc2_dat3', 'mmc1_dat7', 'lcd_data16', 'gpmc_ad15'): pcb.BI,
			(61, '1.29', 'P8_26', 'gpmc_csn0'): pcb.BI,
			(65, '2.1', 'P8_18', 'mcasp0_fsr_1', 'mmc2_clk', 'gpmc_wait1', 'lcd_memory_clk', 'gpmc_clk_mux0'): pcb.BI,
			(66, '2.2', 'P8_7', 'timer4', 'gpmc_advn_ale'): pcb.BI,
			(67, '2.3', 'P8_8', 'timer7', 'gpmc_oen_ren'): pcb.BI,
			(68, '2.4', 'P8_10', 'timer5', 'gpmc_be0n_cle'): pcb.BI,
			(69, '2.5', 'P8_9', 'timer6', 'gpmc_wen'): pcb.BI,
		})
		gnd_pins += ['P8_1', 'P8_2']
	if P9:
		bbb_pins.update({
			('3v3', 'P9_3', 'P9_4'): pcb.POWER_OUT,
			('vin', 'P9_5', 'P9_6'): pcb.POWER_IN,
			('sys_5v', 'P9_7', 'P9_8'): pcb.POWER_OUT,
			('pwr_but', 'P9_9'): pcb.IN,
			('reset', 'P9_10'): pcb.IN,
			('vadc', 'P9_32'): pcb.POWER_OUT,
			('agnd', 'P9_34'): pcb.POWER_GND,
			('ain0', 'P9_39'): pcb.IN,
			('ain1', 'P9_40'): pcb.IN,
			('ain2', 'P9_37'): pcb.IN,
			('ain3', 'P9_38'): pcb.IN,
			('ain4', 'P9_33'): pcb.IN,
			('ain5', 'P9_36'): pcb.IN,
			('ain6', 'P9_35'): pcb.IN,
			(2, '0.2', 'P9_22', 'emu2_1', 'pru_uart_cts_1', 'ehrpwm0a_0', 'i2c2_sda_1', 'uart2_rxd', 'spi0_sclk'): pcb.BI,
			(3, '0.3', 'P9_21', 'emu3_1', 'pru_uart_rts_1', 'ehrpwm0b_0', 'i2c2_scl_1', 'uart2_txd', 'spi0_d0'): pcb.BI,
			(4, '0.4', 'P9_18', 'pru_uart_rxd_0', 'ehrpwm0_tripzone_1', 'i2c1_sda_1', 'mmc1_sdwp_0', 'spi0_d1'): pcb.BI,
			(5, '0.5', 'P9_17', 'pru_uart_txd_0', 'ehrpwm0_synci_0', 'i2c1_scl_1', 'mmc2_sdwp_0', 'spi0_cs0'): pcb.BI,
			(7, '0.7', 'P9_42', 'xdma_event_intr2', 'mmc0_sdwp', 'spi1_sclk_0', 'pr1_ecap0_ecap_capin_apwm_o', 'spi1_cs1_0', 'uart3_txd', 'eCAP0_in_pwm0_out', 114, '3.18', 'pru0i4', 'pru0o4', 'mcasp1_aclkx', 'mcaspo_axr2', 'eQEP0a_in', 'mcasp0_aclkr_0'): pcb.BI,	# In use by mcasp?
			(12, '0.12', 'P9_20', 'pru_uart_cts_0', 'spi1_cs0_0', 'i2c2sda', 'dcan0_tx', 'timer6', 'uart1_ctsn'): pcb.BI,
			(13, '0.13', 'P9_19', 'pru_uart_rts_0', 'spi1_cs1_1', 'i2c2scl', 'dcan0_rx', 'timer5', 'uart1_rtsn'): pcb.BI,
			(14, '0.14', 'P9_26', 'pru1i16', 'pru_uart_rxd_1', 'i2c1_sda_2', 'dcan1_tx', 'mmc1_sdwp_1', 'uart1_rxd'): pcb.BI,
			(15, '0.15', 'P9_24', 'pru0i16a', 'pru_uart_txd_1', 'i2c1_scl_2', 'dcan1_rx', 'mmc2_sdwp_1', 'uart1_txd'): pcb.BI,
			(20, '0.20', 'P9_41', 'emu3', 'pru0i16b', 'timer7_1', 'clkout2', 'tclkin', 'xdma_event_intr1', 116, '3.20', 'pru0i6', 'pru0o6', 'mcasp1_axr0', 'eQEP0_index', 'mcasp0_axr1_0'): pcb.BI,	#  (jtag)
			(30, '0.30', 'P9_11', 'uart4_rxd', 'mmc1_sdcd_0', 'rmii2_crs_dv', 'gpmc_csn4', 'mii2_crs', 'gpmc_wait0'): pcb.BI,
			(31, '0.31', 'P9_13', 'uart4_txd', 'mmc2_sdcd_0', 'mii2_rxerr', 'gpmc_csn5', 'gpmc_wpn'): pcb.BI,
			(48, '1.16', 'P9_15', 'ehrpwm1_tripzone_input', 'gpmc_a16', 'mii2_txen', 'rmii2_tctl', 'gmii2_txen', 'gpmc_a0'): pcb.BI,
			(49, '1.17', 'P9_23', 'ehrpwm0_synco_1', 'gpmc_a17', 'mmc2_dat0_1', 'rgmii2_rxdv', 'gmii2_rxdv', 'gpmc_a1'): pcb.BI,
			(50, '1.18', 'P9_14', 'ehrpwm1a_1', 'gpmc_a18', 'mmc2_dat1_1', 'rgmii2_td3', 'mii2_txd3', 'gpmc_a2'): pcb.BI,
			(51, '1.19', 'P9_16', 'ehrpwm1b_1', 'gpmc_a19', 'mmc2_dat2_1', 'rgmii2_td2', 'mii2_txd2', 'gpmc_a3'): pcb.BI,
			(60, '1.28', 'P9_12', 'mcasp0_aclkr_3', 'gpmc_dir', 'mmc2_dat3_1', 'gpmc_csn6', 'mii2_col', 'gpmc_be1n'): pcb.BI,
			(112, '3.16', 'P9_30', 'pru0i2', 'pru0o2', 'mmc2_sdcd_1', 'spi1_d1', 'ehrpwm0_tripzone_0', 'mcasp0_axr0_0'): pcb.BI,	# used by hdmi?
			(115, '3.19', 'P9_27', 'pru0i5', 'pru0o5', 'emu2_2', 'mcasp1_fsx', 'mcasp0_axr3_0', 'eQEP0b_in', 'mcasp0_fsr'): pcb.BI,
		})
		gnd_pins += ['P9_1', 'P9_2', 'P9_43', 'P9_44', 'P9_45', 'P9_46']

	if J1:
		bbb_pins.update({
			(42, '1.10', 'J1_4', 'Rx0', 'pru1i14', 'pru1o14'): pcb.BI,
			(43, '1.11', 'J1_5', 'Tx0', 'pru1i15', 'pru1o15'): pcb.BI,
		})
		gnd_pins += ['J1_1']

	if not hdmi:
		if P8:
			bbb_pins.update({
				(8, '0.8', 'P8_35', 'uart4_ctsn', 'mcasp0_axr2_2', 'mcasp0_aclkr_1', 'eQEP1a_in', 'gpmc_a16', 'lcd_data12'): pcb.BI,	# pull down
				(9, '0.9', 'P8_33', 'uart4_rtsn', 'mcasp0_axr3_1', 'mcasp0_fsr_2', 'eQEP1b_in', 'gpmc_a17', 'lcd_data13'): pcb.BI,		# pull down
				(10, '0.10', 'P8_31', 'uart5_ctsn', 'uart5_rxd_2', 'mcasp0_axr1_1', 'eQEP1_index', 'gpmc_a18', 'lcd_data14'): pcb.BI,	# pull up
				(11, '0.11', 'P8_32', 'uart5_rtsn', 'mcasp0_axr3_2', 'mcasp0_ahclkx', 'eQEP1_strobe', 'gpmc_a19', 'lcd_data15'): pcb.BI,	# pull down
				(70, '2.6', 'P8_45', 'pru1i0', 'pru1o0', 'ehrpwm2a_2', 'gpmc_a0', 'lcd_data0'): pcb.BI,		# pull down
				(71, '2.7', 'P8_46', 'pru1i1', 'pru1o1', 'ehrpwm2b_2', 'gpmc_a1', 'lcd_data1'): pcb.BI,		# pull down
				(72, '2.8', 'P8_43', 'pru1i2', 'pru1o2', 'ehrpwm2_tripzone_in_2', 'gpmc_a2', 'lcd_data2'): pcb.BI,		# pull up, button
				(73, '2.9', 'P8_44', 'pru1i3', 'pru1o3', 'ehrpwm0_synco_3', 'gpmc_a3', 'lcd_data3'): pcb.BI,		# pull up
				(74, '2.10', 'P8_41', 'pru1i4', 'pru1o4', 'eQEP2a_in_2', 'gpmc_a4', 'lcd_data4'): pcb.BI,	# pull up
				(75, '2.11', 'P8_42', 'pru1i5', 'pru1o5', 'eQEP2b_in_2', 'gpmc_a5', 'lcd_data5'): pcb.BI,	# pull up
				(76, '2.12', 'P8_39', 'pru1i6', 'pru1o6', 'eQEP2_index_2', 'gpmc_a6', 'lcd_data6'): pcb.BI,	# pull down
				(77, '2.13', 'P8_40', 'pru1i7', 'pru1o7', 'pru1_edio_data_out7', 'eQEP2_strobe_2', 'gpmc_a7', 'lcd_data7'): pcb.BI,	# pull down
				(78, '2.14', 'P8_37', 'uart2_ctsn', 'uart5_txd', 'mcasp0_aclkx', 'ehrpwm1_tripzone_in', 'gpmc_a12', 'lcd_data8'): pcb.BI,	# pull down
				(79, '2.15', 'P8_38', 'uart2_rtsn', 'uart5_rxd', 'mcasp0_fsx', 'ehrpwm0_synco_2', 'gpmc_a13', 'lcd_data9'): pcb.BI,	# pull down
				(80, '2.16', 'P8_36', 'uart3_ctsn', 'mcasp0_axr0_1', 'ehrpwm1a', 'gpmc_a14', 'lcd_data10'): pcb.BI,			# pull down
				(81, '2.17', 'P8_34', 'uart3_rtsn', 'mcasp0_axr2_1', 'mcasp0_ahclkr', 'ehrpwm1b', 'gpmc_a15', 'lcd_data11'): pcb.BI,	# pull down
				(86, '2.22', 'P8_27', 'pru1i8', 'pru1o8', 'gpmc_a8', 'lcd_vsync'): pcb.BI,
				(87, '2.23', 'P8_29', 'pru1i9', 'pru1o9', 'gpmc_a9', 'lcd_hsync'): pcb.BI,
				(88, '2.24', 'P8_28', 'pru1i10', 'pru1o10', 'gpmc_a10', 'lcd_pclk'): pcb.BI,
				(89, '2.25', 'P8_30', 'pru1i11', 'pru1o11', 'gpmc_a11', 'lcd_ac_bias_en'): pcb.BI,
			})
		if P9:
			bbb_pins.update({
				(110, '3.14', 'P9_31', 'pru0i0', 'pru0o0', 'mmc0_sdcd_1', 'spi1_sclk_1', 'ehrpwm0a_1', 'mcasp0_aclkx'): pcb.BI,
				(111, '3.15', 'P9_29', 'pru0i1', 'pru0o1', 'mmc1_sdcd_1', 'spi1_d0', 'ehrpwm0b_1', 'mcasp0_fsx'): pcb.BI,
				(113, '3.17', 'P9_28', 'pru0i3', 'pru0o3', 'eCAP2_in_pwm2_out', 'spi1_cs0_1', 'mcasp0_axr2_1', 'ehrpwm0_synci_1', 'mcasp0_ahclkr'): pcb.BI,
				(117, '3.21', 'P9_25', 'pru0i7', 'pru0o7', 'emu4_2', 'mcasp1_axr1', 'mcasp0_axr3_1', 'eQEP0_strobe', 'mcasp0_ahclkx'): pcb.BI,	# lcd audio clock (can be disabled with 1_27)
			})

	if not flash:
		if P8:
			bbb_pins.update({
				(32, '1.0', 'P8_25', 'mmc1_dat0_1', 'gpmc_ad0'): pcb.BI,
				(33, '1.1', 'P8_24', 'mmc1_dat1_1', 'gpmc_ad1'): pcb.BI,
				(34, '1.2', 'P8_5', 'mmc1_dat2_1', 'gpmc_ad2'): pcb.BI,
				(35, '1.3', 'P8_6', 'mmc1_dat3_1', 'gpmc_ad3'): pcb.BI,
				(36, '1.4', 'P8_23', 'mmc1_dat4_1', 'gpmc_ad4'): pcb.BI,
				(37, '1.5', 'P8_22', 'mmc1_dat5_1', 'gpmc_ad5'): pcb.BI,
				(38, '1.6', 'P8_3', 'mmc1_dat6_1', 'gpmc_ad6'): pcb.BI,
				(39, '1.7', 'P8_4', 'mmc1_dat7_1', 'gpmc_ad7'): pcb.BI,
				(62, '1.30', 'P8_21', 'pru1i12', 'pru1o12', 'mmc1_clk', 'gpmc_clk', 'gpmc_csn1'): pcb.BI,
				(63, '1.31', 'P8_20', 'pru1i13', 'pru1o13', 'mmc1_cmd', 'gpmc_be1n', 'gpmc_csn2'): pcb.BI,
			})

	bbb_pins[tuple(gnd_pins)] = pcb.POWER_GND
	ret = pcb.group(bbb_pins)
	if P8:
		p8 = pcb.Part('Pin_Headers:Pin_Header_Straight_2x23', 46)('%s_P8' % base)
		for pin in range(1, 47):
			if 'P8_%d' % pin in ret:
				p8[pin] = ret['P8_%d' % pin]
				p8[pin].net.used = False
			else:
				p8[pin] = None
	if P9:
		p9 = pcb.Part('Pin_Headers:Pin_Header_Straight_2x23', 46)('%s_P9' % base)
		for pin in range(1, 47):
			if 'P9_%d' % pin in ret:
				p9[pin] = ret['P9_%d' % pin]
				p9[pin].net.used = False
			else:
				p9[pin] = None
	if J1:
		j1 = pcb.Part('Pin_Headers:Pin_Header_Straight_1x06', 6)('%s_J1' % base)
		for i in (2, 3, 6):
			j1[i] = None
		for i in (1, 4, 5):
			j1[i] = ret['J1_%d' % i]
			j1[i].net.used = False
	return ret
