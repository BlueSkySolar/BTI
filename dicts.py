# we need to finish this
from collections import OrderedDict


name_dict = OrderedDict((
    ('Frame Time (s)', '00F22'),
    ('Sampling Rate (Hz)', '00F23'),
    ('Vehicle Speed (km/h)', '0AF41'),
    ('Target1 Speed (km/h)', '0AF83'),
    ('Target2 Speed (km/h)', '0AF84'),
    ('Motor Velocity (RPM)', '0AF26'),
    ('Vehicle Velocity (m/s)', '0AF27'),
    ('Motor Tourque Const (Nm/A)', '0AF11'),
    ('Motor Thrust (N)', '0AF43'),
    ('Mech Power (W)', '0AF44'),
    ('DC Bus AmpHours (Ah)', '0AF3D'),
    ('Odometer (m)', '0AF3C'),
    ('Odometer (km)', '0AF40'),
    ('bms_batt_map', '01F10'),
    ('bms_batt_map_1', '02F10'),
    ('bms_batt_map_2', '03F10'),
    ('bms_bal_word', '01F20'),
    ('bms_bal_word_2', '01F21'),
    ('Critical Voltage High (V)', '01F13'),
    ('Critical Voltage Low (V)', '01F14'),
    ('Balancing Threshold (V)', '01F12'),
    ('Critical Temp (deg C)', '01F15'),
    ('Cooling Threshold High (deg C)', '01F16'),
    ('Cooling Threshold Low (deg C)', '01F17'),
    ('bms_curr_wa_error_rate', '01F30'),
    ('bms_peak_wa_error_rate', '01F31'),
    ('bms_curr_crc_error_rate', '01F32'),
    ('bms_peak_crc_error_rate', '01F33'),
    ('bms_curr_dis_error_rate', '01F34'),
    ('bms_peak_dis_error_rate', '01F35'),
    ('Module 0 Temp (deg C)', '01F80'),
    ('Module 1 Temp (deg C)', '01F81'),
    ('Module 2 Temp (deg C)', '01F82'),
    ('Module 3 Temp (deg C)', '01F83'),
    ('Module 4 Temp (deg C)', '01F84'),
    ('Module 0 Voltage (V)', '01F40'),
    ('Module 1 Voltage (V)', '01F41'),
    ('Module 2 Voltage (V)', '01F42'),
    ('Module 3 Voltage (V)', '01F43'),
    ('Module 4 Voltage (V)', '01F44'),
    ('Module 5 Voltage (V)', '01F45'),
    ('Module 6 Voltage (V)', '01F46'),
    ('Module 7 Voltage (V)', '01F47'),
    ('Module 8 Voltage (V)', '01F48'),
    ('Module 9 Voltage (V)', '01F49'),
    ('Module 10 Voltage (V)', '01F4A'),
    ('Module 11 Voltage (V)', '01F4B'),
    ('DEV0 Total Stack Voltage (V)', '01F22'),
    ('DEV0 Max Module Voltage (V)', '01F23'),
    ('DEV0 Ave Module Voltage (V)', '01F24'),
    ('DEV0 Min Module Voltage (V)', '01F25'),
    ('Module 12 Voltage (V)', '02F40'),
    ('Module 13 Voltage (V)', '02F41'),
    ('Module 14 Voltage (V)', '02F42'),
    ('Module 15 Voltage (V)', '02F43'),
    ('Module 16 Voltage (V)', '02F44'),
    ('Module 17 Voltage (V)', '02F45'),
    ('Module 18 Voltage (V)', '02F46'),
    ('Module 19 Voltage (V)', '02F47'),
    ('Module 20 Voltage (V)', '02F48'),
    ('Module 21 Voltage (V)', '02F49'),
    ('Module 22 Voltage (V)', '02F4A'),
    ('Module 23 Voltage (V)', '02F4B'),
    ('DEV1 Total Stack Voltage (V)', '02F22'),
    ('DEV1 Max Module Voltage (V)', '02F23'),
    ('DEV1 Ave Module Voltage (V)', '02F24'),
    ('DEV1 Min Module Voltage (V)', '02F25'),
    ('Module 24 Voltage (V)', '03F40'),
    ('Module 25 Voltage (V)', '03F41'),
    ('Module 26 Voltage (V)', '03F42'),
    ('Module 27 Voltage (V)', '03F43'),
    ('Module 28 Voltage (V)', '03F44'),
    ('Module 29 Voltage (V)', '03F45'),
    ('Module 30 Voltage (V)', '03F46'),
    ('Module 31 Voltage (V)', '03F47'),
    ('Module 32 Voltage (V)', '03F48'),
    ('Module 33 Voltage (V)', '03F49'),
    ('Module 34 Voltage (V)', '03F4A'),
    ('Module 35 Voltage (V)', '03F4B'),
    ('DEV2 Total Stack Voltage (V)', '03F22'),
    ('DEV2 Max Module Voltage (V)', '03F23'),
    ('DEV2 Ave Module Voltage (V)', '03F24'),
    ('DEV2 Min Module Voltage (V)', '03F25'),
    ('Module 36 Voltage (V)', '0CF60'),
    ('Module 0 Temp (deg C)', '01F80'),
    ('Module 1 Temp (deg C)', '01F81'),
    ('Module 2 Temp (deg C)', '01F82'),
    ('Module 3 Temp (deg C)', '01F83'),
    ('Module 4 Temp (deg C)', '01F84'),
    ('DEV0 Aux Temp 0 (deg C)', '01F38'),
    ('DEV0 Aux Temp 1 (deg C)', '01F39'),
    ('DEV0 Aux Temp 2 (deg C)', '01F3A'),
    ('DEV0 Aux Temp 3 (deg C)', '01F3B'),
    ('DEV0 Aux Temp 4 (deg C)', '01F3C'),
    ('DEV0 Aux Temp 5 (deg C)', '01F3D'),
    ('DEV0 Max Module Temp (deg C)', '01F26'),
    ('DEV0 Ave Module Temp (deg C)', '01F27'),
    ('DEV0 Min Module Temp (deg C)', '01F28'),
    ('Module 5 Temp (deg C)', '02F80'),
    ('Module 6 Temp (deg C)', '02F81'),
    ('Module 7 Temp (deg C)', '02F82'),
    ('Module 8 Temp (deg C)', '02F83'),
    ('Module 9 Temp (deg C)', '02F84'),
    ('DEV1 Aux Temp 0 (deg C)', '02F38'),
    ('DEV1 Aux Temp 1 (deg C)', '02F39'),
    ('DEV1 Aux Temp 2 (deg C)', '02F3A'),
    ('DEV1 Aux Temp 3 (deg C)', '02F3B'),
    ('DEV1 Aux Temp 4 (deg C)', '02F3C'),
    ('DEV1 Aux Temp 5 (deg C)', '02F3D'),
    ('DEV1 Max Module Temp (deg C)', '02F26'),
    ('DEV1 Ave Module Temp (deg C)', '02F27'),
    ('DEV1 Min Module Temp (deg C)', '02F28'),
    ('Module 10 Temp (deg C)', '03F80'),
    ('Module 11 Temp (deg C)', '03F81'),
    ('Module 12 Temp (deg C)', '03F82'),
    ('Module 13 Temp (deg C)', '03F83'),
    ('Module 14 Temp (deg C)', '03F84'),
    ('DEV2 Aux Temp 0 (deg C)', '03F38'),
    ('DEV2 Aux Temp 1 (deg C)', '03F39'),
    ('DEV2 Aux Temp 2 (deg C)', '03F3A'),
    ('DEV2 Aux Temp 3 (deg C)', '03F3B'),
    ('DEV2 Aux Temp 4 (deg C)', '03F3C'),
    ('DEV2 Aux Temp 5 (deg C)', '03F3D'),
    ('DEV2 Max Module Temp (deg C)', '03F26'),
    ('DEV2 Ave Module Temp (deg C)', '03F27'),
    ('DEV2 Min Module Temp (deg C)', '03F28'),
    ('Batt Curr Crit Up (A)', '0CF10'),
    ('Batt Curr Crit Down (A)', '0CF11'),
    ('Arr Curr Crit Up (A)', '0BFD0'),
    ('Arr Curr Crit Down (A)', '0BFD1'),
    ('Batt Curr Low (A)', '0CF20'),
    ('Batt Curr High (A)', '0CF21'),
    ('Arr Curr Low (A)', '0BFE0'),
    ('Batt Bus Voltage (V)', '0CF22'),
    ('Batt Bus Current (A)', '0CF23'),
    ('Arr Bus Voltage (V)', '0BFE2'),
    ('Arr Bus Current (A)', '0BFE3'),
    ('Main LP Sys Current (A)', '0CF24'),
    ('PPT LP Sys Current (A)', '0BFE4'),
    ('EM_BATT Temp (deg C)', '0CF3A'),
    ('EM_ARR Temp (deg C)', '0BFFA'),
    ('Total Bus Voltage (V)', '01F22'),
    ('Main LP Sys Power (W)', '0CF2A'),
    ('Misc Power (W)', '0CF2C'),
    ('PPT LP Sys Power (W)', '0BFEA'),
    ('local_sw_version', '0AF09'),
    ('local_sw_version', '0BF09'),
    ('1.2V supply (V)', '0AF32'),
    ('1.65V reference (V)', '0AF30'),
    ('2.5V supply (V)', '0AF33'),
    ('15V supply (V)', '0AF31'),
    ('Fan Drive (%*)', '0AF34'),
    ('Fan Speed (RPM)', '0AF35'),
    ('Air Inlet Temp (deg C)', '0AF39'),
    ('Processor Temp (deg C)', '0AF38'),
    ('Capacitor Temp (deg C)', '0AF3A'),
    ('Heatsink Temp (deg C)', '0AF37'),
    ('Air Outlet Temp (deg C)', '0AF3B'),
    ('Motor Temp (deg C)', '0AF36'),
    ('Bus Voltage (V)', '0AF24'),
    ('Bus Current (A)', '0AF25'),
    ('Bus Power (W)', '0AF42'),
    ('Vd (V)', '0AF2B'),
    ('Vq (V)', '0AF2A'),
    ('BEMFd (V)', '0AF2F'),
    ('BEMFq (V)', '0AF2E'),
    ('Id (A)', '0AF2D'),
    ('Iq (A)', '0AF2C'),
    ('Phase A Current (Arms)', '0AF29'),
    ('Phase B Current (Arms)', '0AF28'),
    ('Panel Voltage (V)', '0BF60'),
    ('Panel Power (W)', '0BF61'),
    ('Battery Voltage (V)', '0BF62'),
    ('Battery Current (A)', '0BF63'),
    ('Throttle Position (%)', '0AF80'),
    ('dctrls_cc_throttle_lock (%)', '0AF86'),
    ('Regen Brake Position (%)', '0AF81'),
    ('Bus Current Factor (%)', '0AF82'),
    ('Steering Angle (%)', '06F80'),
    ('Panel0 Power (W)', '0BF61'),
    ('Panel1 Power (W)', '0BF65'),
    ('Panel2 Power (W)', '0BF69'),
    ('Panel3 Power (W)', '0BF6D'),
    ('Panel4 Power (W)', '0BF71'),
    ('Panel5 Power (W)', '0BF75'),
    ('Panel6 Power (W)', '0BF79'),
    ('Panel7 Power (W)', '0BF7D'),
    ('Panel8 Power (W)', '0BF81'),
    ('Panel9 Power (W)', '0BF85'),
    ('Panel0 Voltage (V)', '0BF60'),
    ('Panel1 Voltage (V)', '0BF64'),
    ('Panel2 Voltage (V)', '0BF68'),
    ('Panel3 Voltage (V)', '0BF6C'),
    ('Panel4 Voltage (V)', '0BF70'),
    ('Panel5 Voltage (V)', '0BF74'),
    ('Panel6 Voltage (V)', '0BF78'),
    ('Panel7 Voltage (V)', '0BF7C'),
    ('Panel8 Voltage (V)', '0BF80'),
    ('Panel9 Voltage (V)', '0BF84'),
    ('MPPT0 Panel Voltage (V)', '0BF64'),
    ('MPPT0 Panel Power (W)', '0BF65'),
    ('MPPT0 Battery Voltage (V)', '0BF66'),
    ('MPPT0 Battery Current (A)', '0BF67'),
    ('MPPT1 Panel Voltage (V)', '0BF68'),
    ('MPPT1 Panel Power (W)', '0BF69'),
    ('MPPT1 Battery Voltage (V)', '0BF6A'),
    ('MPPT1 Battery Current (A)', '0BF6B'),
    ('MPPT2 Panel Voltage (V)', '0BF6C'),
    ('MPPT2 Panel Power (W)', '0BF6D'),
    ('MPPT2 Battery Voltage (V)', '0BF6E'),
    ('MPPT2 Battery Current (A)', '0BF6F'),
    ('MPPT3 Panel Voltage (V)', '0BF70'),
    ('MPPT3 Panel Power (W)', '0BF71'),
    ('MPPT3 Battery Voltage (V)', '0BF72'),
    ('MPPT3 Battery Current (A)', '0BF73'),
    ('MPPT4 Panel Voltage (V)', '0BF74'),
    ('MPPT4 Panel Power (W)', '0BF75'),
    ('MPPT4 Battery Voltage (V)', '0BF76'),
    ('MPPT4 Battery Current (A)', '0BF77'),
    ('MPPT5 Panel Voltage (V)', '0BF78'),
    ('MPPT5 Panel Power (W)', '0BF79'),
    ('MPPT5 Battery Voltage (V)', '0BF7A'),
    ('MPPT5 Battery Current (A)', '0BF7B'),
    ('MPPT6 Panel Voltage (V)', '0BF7C'),
    ('MPPT6 Panel Power (W)', '0BF7D'),
    ('MPPT6 Battery Voltage (V)', '0BF7E'),
    ('MPPT6 Battery Current (A)', '0BF7F'),
    ('MPPT7 Panel Voltage (V)', '0BF80'),
    ('MPPT7 Panel Power (W)', '0BF81'),
    ('MPPT7 Battery Voltage (V)', '0BF82'),
    ('MPPT7 Battery Current (A)', '0BF83'),
    ('MPPT8 Panel Voltage (V)', '0BF84'),
    ('MPPT8 Panel Power (W)', '0BF85'),
    ('MPPT8 Battery Voltage (V)', '0BF86'),
    ('MPPT8 Battery Current (A)', '0BF87'),
    ('Set 1 Acc X (Gs)', '06F20'),
    ('Set 1 Acc Y (Gs)', '06F21'),
    ('Set 1 Acc Z (Gs)', '06F22'),
    ('Set 1 Rot X (deg/S)', '06F23'),
    ('Set 1 Rot Y (deg/S)', '06F24'),
    ('Set 1 Rot Z (deg/S)', '06F25'),
    ('Set 1 Mag X (mGauss)', '06F26'),
    ('Set 1 Mag Y (mGauss)', '06F27'),
    ('Set 1 Mag Z (mGauss)', '06F28'),
    ('Set 1 Mag Heading (deg)', '06F61'),
    ('Batt En-Cnt Front (Wh)', '0CF28'),
    ('Arr En-Cnt 1 (Wh)', '0BFEF'),
    ('Motor En-Cnt (Wh)', '0CF2F'),
    ('Batt En-Cnt Back (Wh)', '0CF29'),
    ('Main LP Sys En-Cnt (Wh)', '0CF2B'),
    ('Misc En-Cnt (Wh)', '0CF2D'),
    ('PPT LP Sys En-Cnt (Wh)', '0BFEB'),
    ('Arr En-Cnt 2 (Wh)', '0BFE8'),
    ('Batt Power Front (W)', '0CF25'),
    ('Arr Bus Power 1 (W)', '0BFEE'),
    ('Motor Power (W)', '0CF2E'),
    ('Batt Transfer Eff (%)', '0CF26'),
    ('Batt Power Back (W)', '0CF27'),
    ('Arr Bus Power 2 (W)', '0BFE5'),
    ('Set 2 Rot X (deg/S)', '06F35'),
    ('Set 2 Rot Y (deg/S)', '06F36'),
    ('Set 2 Rot Z (deg/S)', '06F37'),
    ('Set 2 Mag X (mGauss)', '06F38'),
    ('Set 2 Mag Y (mGauss)', '06F39'),
    ('Set 2 Mag Z (mGauss)', '06F3A'),
    ('Set 2 Acc X (Gs)', '06F32'),
    ('Set 2 Acc Y (Gs)', '06F33'),
    ('Set 2 Acc Z (Gs)', '06F34'),
    ('Set 2 Mag Heading (deg)', '06F63'),
    ('Garmin GPS Lat (deg)', '0EF00'),
    ('Garmin GPS Lon (deg)', '0EF01'),
    ('Wind Magnitude (m/s)', '0EF02'),
    ('Wind Direction (deg)', '0EF03'),
    ('bms_curr_dev_errors', ('0FFAA', '00000001')),
    ('---------------------------------', ('0FFAA', '00000002')),
    ('C31.INIT_DEV7_ERROR', ('01F36', '80000000')),
    ('C30.INIT_DEV6_ERROR', ('01F36', '40000000')),
    ('C29.INIT_DEV5_ERROR', ('01F36', '20000000')),
    ('C28.INIT_DEV4_ERROR', ('01F36', '10000000')),
    ('C27.INIT_DEV3_ERROR', ('01F36', '08000000')),
    ('C26.INIT_DEV2_ERROR', ('01F36', '04000000')),
    ('C25.INIT_DEV1_ERROR', ('01F36', '02000000')),
    ('C24.INIT_DEV0_ERROR', ('01F36', '01000000')),
    ('C23.WA_DEV7_ERROR', ('01F36', '00800000')),
    ('C22.WA_DEV6_ERROR', ('01F36', '00400000')),
    ('C21.WA_DEV5_ERROR', ('01F36', '00200000')),
    ('C20.WA_DEV4_ERROR', ('01F36', '00100000')),
    ('C19.WA_DEV3_ERROR', ('01F36', '00080000')),
    ('C18.WA_DEV2_ERROR', ('01F36', '00040000')),
    ('C17.WA_DEV1_ERROR', ('01F36', '00020000')),
    ('C16.WA_DEV0_ERROR', ('01F36', '00010000')),
    ('C15.CRC_DEV7_ERROR', ('01F36', '00008000')),
    ('C14.CRC_DEV6_ERROR', ('01F36', '00004000')),
    ('C13.CRC_DEV5_ERROR', ('01F36', '00002000')),
    ('C12.CRC_DEV4_ERROR', ('01F36', '00001000')),
    ('C11.CRC_DEV3_ERROR', ('01F36', '00000800')),
    ('C10.CRC_DEV2_ERROR', ('01F36', '00000400')),
    ('C9.CRC_DEV1_ERROR', ('01F36', '00000200')),
    ('C8.CRC_DEV0_ERROR', ('01F36', '00000100')),
    ('C7.DIS_DEV7_ERROR', ('01F36', '00000080')),
    ('C6.DIS_DEV6_ERROR', ('01F36', '00000040')),
    ('C5.DIS_DEV5_ERROR', ('01F36', '00000020')),
    ('C4.DIS_DEV4_ERROR', ('01F36', '00000010')),
    ('C3.DIS_DEV3_ERROR', ('01F36', '00000008')),
    ('C2.DIS_DEV2_ERROR', ('01F36', '00000004')),
    ('C1.DIS_DEV1_ERROR', ('01F36', '00000002')),
    ('C0.DIS_DEV0_ERROR', ('01F36', '00000001')),
    ('bms_hold_dev_errors', ('0FFAA', '00000001')),
    ('H31.INIT_DEV7_ERROR', ('01F37', '80000000')),
    ('H30.INIT_DEV6_ERROR', ('01F37', '40000000')),
    ('H29.INIT_DEV5_ERROR', ('01F37', '20000000')),
    ('H28.INIT_DEV4_ERROR', ('01F37', '10000000')),
    ('H27.INIT_DEV3_ERROR', ('01F37', '08000000')),
    ('H26.INIT_DEV2_ERROR', ('01F37', '04000000')),
    ('H25.INIT_DEV1_ERROR', ('01F37', '02000000')),
    ('H24.INIT_DEV0_ERROR', ('01F37', '01000000')),
    ('H23.WA_DEV7_ERROR', ('01F37', '00800000')),
    ('H22.WA_DEV6_ERROR', ('01F37', '00400000')),
    ('H21.WA_DEV5_ERROR', ('01F37', '00200000')),
    ('H20.WA_DEV4_ERROR', ('01F37', '00100000')),
    ('H19.WA_DEV3_ERROR', ('01F37', '00080000')),
    ('H18.WA_DEV2_ERROR', ('01F37', '00040000')),
    ('H17.WA_DEV1_ERROR', ('01F37', '00020000')),
    ('H16.WA_DEV0_ERROR', ('01F37', '00010000')),
    ('H15.CRC_DEV7_ERROR', ('01F37', '00008000')),
    ('H14.CRC_DEV6_ERROR', ('01F37', '00004000')),
    ('H13.CRC_DEV5_ERROR', ('01F37', '00002000')),
    ('H12.CRC_DEV4_ERROR', ('01F37', '00001000')),
    ('H11.CRC_DEV3_ERROR', ('01F37', '00000800')),
    ('H10.CRC_DEV2_ERROR', ('01F37', '00000400')),
    ('H9.CRC_DEV1_ERROR', ('01F37', '00000200')),
    ('H8.CRC_DEV0_ERROR', ('01F37', '00000100')),
    ('H7.DIS_DEV7_ERROR', ('01F37', '00000080')),
    ('H6.DIS_DEV6_ERROR', ('01F37', '00000040')),
    ('H5.DIS_DEV5_ERROR', ('01F37', '00000020')),
    ('H4.DIS_DEV4_ERROR', ('01F37', '00000010')),
    ('H3.DIS_DEV3_ERROR', ('01F37', '00000008')),
    ('H2.DIS_DEV2_ERROR', ('01F37', '00000004')),
    ('H1.DIS_DEV1_ERROR', ('01F37', '00000002')),
    ('H0.DIS_DEV0_ERROR', ('01F37', '00000001')),
    ('31.INIT_DEV7_ERROR', ('01F36', '80000000')),
    ('30.INIT_DEV6_ERROR', ('01F36', '40000000')),
    ('29.INIT_DEV5_ERROR', ('01F36', '20000000')),
    ('28.INIT_DEV4_ERROR', ('01F36', '10000000')),
    ('27.INIT_DEV3_ERROR', ('01F36', '08000000')),
    ('26.INIT_DEV2_ERROR', ('01F36', '04000000')),
    ('25.INIT_DEV1_ERROR', ('01F36', '02000000')),
    ('24.INIT_DEV0_ERROR', ('01F36', '01000000')),
    ('23.WA_DEV7_ERROR', ('01F36', '00800000')),
    ('22.WA_DEV6_ERROR', ('01F36', '00400000')),
    ('21.WA_DEV5_ERROR', ('01F36', '00200000')),
    ('20.WA_DEV4_ERROR', ('01F36', '00100000')),
    ('19.WA_DEV3_ERROR', ('01F36', '00080000')),
    ('18.WA_DEV2_ERROR', ('01F36', '00040000')),
    ('17.WA_DEV1_ERROR', ('01F36', '00020000')),
    ('16.WA_DEV0_ERROR', ('01F36', '00010000')),
    ('15.CRC_DEV7_ERROR', ('01F36', '00008000')),
    ('14.CRC_DEV6_ERROR', ('01F36', '00004000')),
    ('13.CRC_DEV5_ERROR', ('01F36', '00002000')),
    ('12.CRC_DEV4_ERROR', ('01F36', '00001000')),
    ('11.CRC_DEV3_ERROR', ('01F36', '00000800')),
    ('10.CRC_DEV2_ERROR', ('01F36', '00000400')),
    ('9.CRC_DEV1_ERROR', ('01F36', '00000200')),
    ('8.CRC_DEV0_ERROR', ('01F36', '00000100')),
    ('7.DIS_DEV7_ERROR', ('01F36', '00000080')),
    ('6.DIS_DEV6_ERROR', ('01F36', '00000040')),
    ('5.DIS_DEV5_ERROR', ('01F36', '00000020')),
    ('4.DIS_DEV4_ERROR', ('01F36', '00000010')),
    ('3.DIS_DEV3_ERROR', ('01F36', '00000008')),
    ('2.DIS_DEV2_ERROR', ('01F36', '00000004')),
    ('1.DIS_DEV1_ERROR', ('01F36', '00000002')),
    ('0.DIS_DEV0_ERROR', ('01F36', '00000001')),
    ('bms_hold_dev_errors', ('0FFAA', '00000001')),
    ('31.INIT_DEV7_ERROR', ('01F37', '80000000')),
    ('30.INIT_DEV6_ERROR', ('01F37', '40000000')),
    ('29.INIT_DEV5_ERROR', ('01F37', '20000000')),
    ('28.INIT_DEV4_ERROR', ('01F37', '10000000')),
    ('27.INIT_DEV3_ERROR', ('01F37', '08000000')),
    ('26.INIT_DEV2_ERROR', ('01F37', '04000000')),
    ('25.INIT_DEV1_ERROR', ('01F37', '02000000')),
    ('24.INIT_DEV0_ERROR', ('01F37', '01000000')),
    ('23.WA_DEV7_ERROR', ('01F37', '00800000')),
    ('22.WA_DEV6_ERROR', ('01F37', '00400000')),
    ('21.WA_DEV5_ERROR', ('01F37', '00200000')),
    ('20.WA_DEV4_ERROR', ('01F37', '00100000')),
    ('19.WA_DEV3_ERROR', ('01F37', '00080000')),
    ('18.WA_DEV2_ERROR', ('01F37', '00040000')),
    ('17.WA_DEV1_ERROR', ('01F37', '00020000')),
    ('16.WA_DEV0_ERROR', ('01F37', '00010000')),
    ('15.CRC_DEV7_ERROR', ('01F37', '00008000')),
    ('14.CRC_DEV6_ERROR', ('01F37', '00004000')),
    ('13.CRC_DEV5_ERROR', ('01F37', '00002000')),
    ('12.CRC_DEV4_ERROR', ('01F37', '00001000')),
    ('11.CRC_DEV3_ERROR', ('01F37', '00000800')),
    ('10.CRC_DEV2_ERROR', ('01F37', '00000400')),
    ('9.CRC_DEV1_ERROR', ('01F37', '00000200')),
    ('8.CRC_DEV0_ERROR', ('01F37', '00000100')),
    ('7.DIS_DEV7_ERROR', ('01F37', '00000080')),
    ('6.DIS_DEV6_ERROR', ('01F37', '00000040')),
    ('5.DIS_DEV5_ERROR', ('01F37', '00000020')),
    ('4.DIS_DEV4_ERROR', ('01F37', '00000010')),
    ('3.DIS_DEV3_ERROR', ('01F37', '00000008')),
    ('2.DIS_DEV2_ERROR', ('01F37', '00000004')),
    ('1.DIS_DEV1_ERROR', ('01F37', '00000002')),
    ('0.DIS_DEV0_ERROR', ('01F37', '00000001')),
    ('11.BATT EN', ('01F10', '00000800')),
    ('10.BATT EN', ('01F10', '00000400')),
    ('9.BATT EN', ('01F10', '00000200')),
    ('8.BATT EN', ('01F10', '00000100')),
    ('7.BATT EN', ('01F10', '00000080')),
    ('6.BATT EN', ('01F10', '00000040')),
    ('5.BATT EN', ('01F10', '00000020')),
    ('4.BATT EN', ('01F10', '00000010')),
    ('3.BATT EN', ('01F10', '00000008')),
    ('2.BATT EN', ('01F10', '00000004')),
    ('1.BATT EN', ('01F10', '00000002')),
    ('0.BATT EN', ('01F10', '00000001')),
    ('23.BATT EN', ('02F10', '00000800')),
    ('22.BATT EN', ('02F10', '00000400')),
    ('21.BATT EN', ('02F10', '00000200')),
    ('20.BATT EN', ('02F10', '00000100')),
    ('19.BATT EN', ('02F10', '00000080')),
    ('18.BATT EN', ('02F10', '00000040')),
    ('17.BATT EN', ('02F10', '00000020')),
    ('16.BATT EN', ('02F10', '00000010')),
    ('15.BATT EN', ('02F10', '00000008')),
    ('14.BATT EN', ('02F10', '00000004')),
    ('13.BATT EN', ('02F10', '00000002')),
    ('12.BATT EN', ('02F10', '00000001')),
    ('35.BATT EN', ('03F10', '00000800')),
    ('34.BATT EN', ('03F10', '00000400')),
    ('33.BATT EN', ('03F10', '00000200')),
    ('32.BATT EN', ('03F10', '00000100')),
    ('31.BATT EN', ('03F10', '00000080')),
    ('30.BATT EN', ('03F10', '00000040')),
    ('29.BATT EN', ('03F10', '00000020')),
    ('28.BATT EN', ('03F10', '00000010')),
    ('27.BATT EN', ('03F10', '00000008')),
    ('26.BATT EN', ('03F10', '00000004')),
    ('25.BATT EN', ('03F10', '00000002')),
    ('24.BATT EN', ('03F10', '00000001'))
))

test_dict = {
    '03F96': '00000000',
    '0CF26': '42C7F2C5',
    '03F92': '00000000',
    '03F90': '00000000',
    '03F5B': '00000000',
    '01F5C': '00000000',
    '01F4A': '40D1B3D0',
    '03F37': '00000000',
    '01F8E': '00000000',
    '01F3B': '00000000',
    '01F33': '00000000',
    '03F4A': '40664C2F',
    '01F85': '00000000',
    '03F46': '40660AA6',
    '01F3A': '00000000',
    '00F40': 'C0000000',
    '03F9A': '00000000',
    '03F47': '4065AEE6',
    '01F97': '00000000',
    '00F08': '00000000',
    '03F97': '00000000',
    '0CF27': '419DAE4E',
    '01F32': '00000000',
    '03F27': '00000000',
    '00F28': '00000000',
    '01F8C': '00000000',
    '01F30': '00000000',
    '03F99': '00000000',
    '03F43': '40660AA6',
    '00F29': 'C32A6AA9',
    '01F54': '00000000',
    '03F54': '00000000',
    '01F57': '00000000',
    '00F61': 'C0000000',
    '01F38': '00000000',
    '03F30': '00000000',
    '01F0A': '00100108',
    '01F9F': '00000000',
    '03F52': '00000000',
    '03F89': '00000000',
    '01F27': '00000000',
    '03F8F': '00000000',
    '05F0A': '00100101',
    '03F93': '00000000',
    '01F21': '00000000',
    '01F5E': '00000000',
    '01F12': '40800000',
    '03F8C': '00000000',
    '01F39': '00000000',
    '05F0D': '00000000',
    '01F9C': '00000000',
    '01FC0': '429D46DC',
    '0CF09': '3F800000',
    '03F40': '406594AF',
    '05F0C': '00000000',
    '03F4C': '00000000',
    '0CF2B': '4420A0E2',
    '01F9A': '00000000',
    '01FA3': '00000000',
    '03F9E': '00000000',
    '03F85': '00000000',
    '03F23': '40664C2F',
    '03F3D': '00000000',
    '03F4F': '00000000',
    '01F5D': '00000000',
    '00F27': '00001003',
    '03F91': '00000000',
    '01F09': '3F800000',
    '01F22': '429D46DC',
    '01F99': '00000000',
    '01F51': '00000000',
    '01F37': '00000000',
    '00F10': '00001C2F',
    '01F40': '40D1B3D0',
    '03F5E': '00000000',
    '00F26': '00000000',
    '03F4B': '4065E9E1',
    '01F4F': '00000000',
    '01F45': '40D1B3D0',
    '01F8F': '00000000',
    '01F24': '40D1B3D0',
    '0CF29': '4474CFED',
    '03F8D': '00000000',
    '01F4D': '00000000',
    '0CF11': 'C1F00000',
    '01F3C': '00000000',
    '03F80': '0000001C',
    '01FA0': '00000000',
    '01F86': '00000000',
    '01F42': '40D1B3D0',
    '03F31': '00000000',
    '01F94': '00000000',
    '03FA0': '00000000',
    '01F26': '00000000',
    '01F53': '00000000',
    '03F28': '447A0000',
    '03F20': '00000000',
    '01F08': '00000000',
    '03F10': '00000FFF',
    '03F08': '00000000',
    '01F49': '40D1B3D0',
    '03F4D': '00000000',
    '00F0A': '60000108',
    '00F22': '44636135',
    '03F25': '406594AF',
    '01F23': '40D1B3D0',
    '0CF2E': '41664B8A',
    '03F8A': '00000000',
    '01F0D': '00000000',
    '03F9B': '00000000',
    '01F10': '00000FFF',
    '00F24': '00000000',
    '01F50': '00000000',
    '00F23': '3FA8EBBB',
    '01F52': '00000000',
    '01F98': '00000000',
    '03F35': '00000000',
    '01F80': '0000001C',
    '01F95': '00000000',
    '03F48': '4065E354',
    '03F60': '00000000',
    '03F53': '00000000',
    '03F3B': '00000000',
    '01F91': '00000000',
    '03F5D': '00000000',
    '03F86': '00000000',
    '01F88': '00000000',
    '03F55': '00000000',
    '03F51': '00000000',
    '0CF23': '3E17B4CE',
    '03F5C': '00000000',
    '01F55': '00000000',
    '01F81': '0000001C',
    '0CF0D': '00000000',
    '03F9C': '00000000',
    '03F33': '00000000',
    '03F34': '00000000',
    '03F4E': '00000000',
    '01F84': '0000001C',
    '03F11': '00000000',
    '03F3A': '00000000',
    '01F5B': '00000000',
    '03F0A': '00000101',
    '01F43': '40D1B3D0',
    '01F48': '40D1B3D0',
    '01F47': '40D1B3D0',
    '0CF20': '3E17B4CE',
    '0CF31': '00000000',
    '01F46': '40D1B3D0',
    '01F34': '00000000',
    '0CF10': '41F00000',
    '0CF2A': '40A9F86C',
    '03F49': '4065FD8A',
    '0CF2C': '00000000',
    '03F9F': '00000000',
    '01F87': '00000000',
    '03F50': '00000000',
    '0CF22': '430501B2',
    '01F44': '40D1B3D0',
    '03F29': '00000000',
    '03F0D': '00000000',
    '01F9E': '00000000',
    '03F83': '0000001C',
    '01F3D': '00000000',
    '03F38': '00000000',
    '03F94': '00000000',
    '03F3C': '00000000',
    '03F5A': '00000000',
    '01F60': '00000000',
    '00F21': '00000101',
    '01F4B': '40D1B3D0',
    '03F56': '00000000',
    '01F28': '447A0000',
    '01F4C': '00000000',
    '0CF0A': '00020104',
    '0CF21': 'BE360B20',
    '03F44': '4065F06F',
    '0CF60': '430501B2',
    '00F41': 'C0000000',
    '01F63': '00000000',
    '03F81': '0000001C',
    '03F63': '00000000',
    '03F21': '00000000',
    '01F56': '00000000',
    '01F35': '00000000',
    '01F5A': '00000000',
    '01F59': '00000000',
    '01F4E': '00000000',
    '03F95': '00000000',
    '03F32': '00000000',
    '05F09': '3F800000',
    '00F09': '3F800000',
    '00F60': 'C0000000',
    '01F58': '00000000',
    '0CF3A': '41D04443',
    '01F0C': '00000000',
    '01F5F': '00000000',
    '03F87': '00000000',
    '00F42': 'FFFFFFFE',
    '03F22': '422C7248',
    '01F90': '00000000',
    '01F36': '00000000',
    '03F45': '4065A858',
    '01F11': '00000000',
    '01F96': '00000000',
    '03F58': '00000000',
    '03F8B': '00000000',
    '01F93': '00000000',
    '03F0C': '00000000',
    '0CF32': '00000000',
    '05F08': '00000000',
    '03F82': '0000001C',
    '03F09': '3F800000',
    '01F82': '0000001C',
    '03F26': '00000000',
    '03F98': '00000000',
    '03F57': '00000000',
    '03F59': '00000000',
    '00F25': '44636135',
    '01F41': '40D1B3D0',
    '01F8B': '00000000',
    '03F5F': '00000000',
    '0CF0C': '00000000',
    '01F25': '40D1B3D0',
    '0CF2F': '43043570',
    '01F9D': '00000000',
    '01F92': '00000000',
    '00F63': 'C0000000',
    '03F8E': '00000000',
    '03F12': '40800000',
    '01F89': '00000000',
    '03F39': '00000000',
    '03F36': '00000000',
    '0CF28': '4441AE3E',
    '03FA3': '00000000',
    '00F0C': '00000000',
    '01F20': '00000000',
    '0CF24': '3D239288',
    '0CF25': '419DA3E0',
    '01F9B': '00000000',
    '03F84': '0000001C',
    '00F62': 'C0000000',
    '03F41': '40660418',
    '0CF08': '00000000',
    '00F20': '00000C04',
    '03F88': '00000000',
    '03F9D': '00000000',
    '03F24': '4065EDB5',
    '00F0D': '00000000',
    '0CF2D': '00000000',
    '01F29': '00000000',
    '01F31': '00000000',
    '01F8D': '00000000',
    '03F42': '406617C1',
    '01F8A': '00000000',
    '01F83': '0000001C'
}

#######################################################

# raw output from parsing the workspace file, will be edited later
# weird formatting due to text editor's autoformatting lol

#######################################################
[('can_tx_map[0]', '00F00', 'hex string'),
 ('can_tx_map[1]', '00F01', 'hex string'),
 ('can_tx_map[2]', '00F02', 'hex string'),
 ('can_tx_map[3]', '00F03', 'hex string'),
 ('can_tx_map[4]', '00F04', 'hex string'),
 ('can_tx_map[5]', '00F05', 'hex string'),
 ('can_tx_map[6]', '00F06', 'hex string'),
 ('can_tx_map[7]', '00F07', 'hex string'),
 ('can_write_lock', '00F08', 'hex string'),
 ('local_sw_version', '00F09', 'float'),
 ('local_con_stat_word', '00F0A', 'hex string'),
 ('local_con_stat_word_2', '00F0B', 'hex string'),
 ('lcs_write_window', '00F0C', 'hex string'),
 ('can_error_stats', '00F0D', 'hex string'),
 ('can_tx_map[0]', '01F00', 'hex string'),
 ('can_tx_map[1]', '01F01', 'hex string'),
 ('can_tx_map[2]', '01F02', 'hex string'), (
     'can_tx_map[3]', '01F03', 'hex string'), (
         'can_tx_map[4]', '01F04', 'hex string'), (
             'can_tx_map[5]', '01F05', 'hex string'), ('can_tx_map[6]',
                                                       '01F06', 'hex string'),
 ('can_tx_map[7]', '01F07',
  'hex string'), ('can_write_lock', '01F08', 'hex string'), (
      'local_sw_version', '01F09', 'float'), (
          'local_con_stat_word', '01F0A', 'hex string'), (
              'local_con_stat_word_2', '01F0B', 'hex string'), (
                  'lcs_write_window', '01F0C', 'hex string'), (
                      'can_error_stats', '01F0D', 'hex string'), (
                          'can_tx_map[0]', '0CF00', 'hex string'), (
                              'can_tx_map[1]', '0CF01', 'hex string'), (
                                  'can_tx_map[2]', '0CF02', 'hex string'), (
                                      'can_tx_map[3]', '0CF03', 'hex string'),
 ('can_tx_map[4]', '0CF04', 'hex string'), (
     'can_tx_map[5]', '0CF05', 'hex string'), (
         'can_tx_map[6]', '0CF06', 'hex string'), (
             'can_tx_map[7]', '0CF07', 'hex string'), (
                 'can_write_lock', '0CF08', 'hex string'), (
                     'local_sw_version', '0CF09', 'float'), (
                         'local_con_stat_word', '0CF0A', 'hex string'), (
                             'local_con_stat_word_2', '0CF0B', 'hex string'), (
                                 'lcs_write_window', '0CF0C', 'hex string'), (
                                     'can_error_stats', '0CF0D', 'hex string'),
 ('can_tx_map[0]', '06F00', 'hex string'), (
     'can_tx_map[1]', '06F01', 'hex string'), (
         'can_tx_map[2]', '06F02', 'hex string'), (
             'can_tx_map[3]', '06F03', 'hex string'), (
                 'can_tx_map[4]', '06F04', 'hex string'), (
                     'can_tx_map[5]', '06F05', 'hex string'), (
                         'can_tx_map[6]', '06F06', 'hex string'), (
                             'can_tx_map[7]', '06F07', 'hex string'), (
                                 'can_write_lock', '06F08', 'hex string'), (
                                     'local_sw_version', '06F09', 'float'),
 ('local_con_stat_word', '06F0A',
  'hex string'), ('local_con_stat_word_2', '06F0B', 'hex string'), (
      'lcs_write_window',
      '06F0C', 'hex string'), ('can_error_stats', '06F0D', 'hex string'), (
          'can_tx_map[0]', '0AF60', 'hex string'), (
              'can_tx_map[1]', '0AF61', 'hex string'), (
                  'can_tx_map[2]', '0AF62', 'hex string'), (
                      'can_tx_map[3]', '0AF63', 'hex string'), (
                          'can_tx_map[4]', '0AF64', 'hex string'), (
                              'can_tx_map[5]', '0AF65', 'hex string'), (
                                  'can_tx_map[6]', '0AF66', 'hex string'), (
                                      'can_tx_map[7]', '0AF67', 'hex string'),
 ('can_write_lock', '0AF68',
  'hex string'), ('local_sw_version', '0AF69', 'float'), (
      'local_con_stat_word', '0AF6A',
      'hex string'), ('local_con_stat_word_2', '0AF6B', 'hex string'), (
          'lcs_write_window', '0AF6C', 'hex string'), (
              'can_error_stats', '0AF6D', 'hex string'), (
                  'coord_go_map', '00F10', 'hex string'), (
                      'coord_mod_timeout_map', '00F20', 'hex string'), (
                          '=======================', '0FFAA', 'long'), (
                              'Frame Size (# of channels)', '00F21', 'long'), (
                                  'Frame Time (s)', '00F22', 'float'), (
                                      'Sampling Rate (Hz)', '00F23', 'float'),
 ('=======================', '0FFAB',
  'long'), ('Current Mark Num (#)', '00F26', 'long'), (
      'Current Stint Num (#)', '00F24',
      'long'), ('Current Stint Time (s)', '00F25', 'float'), (
          'Previous Stint Time (s)', '00F28', 'float'), (
              '=======================', '0FFAC', 'long'), (
                  'coord_global_error_word', '00F27', 'hex string'), (
                      'bms_batt_map', '01F10', 'hex string'), (
                          'bms_batt_map_1', '02F10', 'hex string'), (
                              'bms_batt_map_2', '03F10', 'hex string'), (
                                  'bms_bal_word', '01F20', 'hex string'), (
                                      'bms_bal_word_2', '01F21', 'hex string'),
 ('=======================', '0FFAA',
  'long'), ('Critical Voltage High (V)', '01F13', 'float'), (
      'Critical Voltage Low (V)', '01F14', 'float'), (
          'Balancing Threshold (V)', '01F12', 'float'), (
              '=======================', '0FFAB', 'long'), (
                  'Critical Temp (deg C)', '01F15', 'float'), (
                      'Cooling Threshold High (deg C)', '01F16', 'float'), (
                          'Cooling Threshold Low (deg C)', '01F17', 'float'), (
                              '=======================', '0FFAC', 'long'), (
                                  'bms_curr_wa_error_rate', '01F30', 'float'),
 ('bms_peak_wa_error_rate',
  '01F31', 'float'), ('bms_curr_crc_error_rate', '01F32', 'float'), (
      'bms_peak_crc_error_rate', '01F33', 'float'), (
          'bms_curr_dis_error_rate', '01F34', 'float'), (
              'bms_peak_dis_error_rate', '01F35', 'float'), (
                  'bms_curr_dev_errors', '01F36', 'hex string'), (
                      'bms_hold_dev_errors', '01F37', 'hex string'), (
                          'Module 4 Temp (deg C)', '01F84', 'float'), (
                              'Module 3 Temp (deg C)', '01F83', 'float'), (
                                  'Module 2 Temp (deg C)', '01F82', 'float'),
 ('Module 1 Temp (deg C)', '01F81', 'float'), (
     'Module 0 Temp (deg C)', '01F80',
     'float'), ('Module 11 Voltage (V)', '01F4B', 'float'), (
         'Module 10 Voltage (V)', '01F4A', 'float'), (
             'Module 9 Voltage (V)', '01F49', 'float'), (
                 'Module 8 Voltage (V)', '01F48', 'float'), (
                     'Module 7 Voltage (V)', '01F47', 'float'), (
                         'Module 6 Voltage (V)', '01F46', 'float'), (
                             'Module 5 Voltage (V)', '01F45', 'float'), (
                                 'Module 4 Voltage (V)', '01F44', 'float'), (
                                     'Module 3 Voltage (V)', '01F43', 'float'),
 ('Module 2 Voltage (V)', '01F42', 'float'), (
     'Module 1 Voltage (V)', '01F41', 'float'), (
         'Module 0 Voltage (V)', '01F40', 'float'), (
             'Batt Curr Crit Up (A)', '0CF10', 'float'), (
                 'Batt Curr Crit Down (A)', '0CF11', 'float'), (
                     'Arr Curr Crit Up (A)', '0BFD0', 'float'), (
                         'Arr Curr Crit Down (A)', '0BFD1', 'float'), (
                             '=======================', '0FFAA', 'long'), (
                                 'Batt Curr Low (A)', '0CF20', 'float'), (
                                     'Batt Curr High (A)', '0CF21', 'float'), (
                                         'Arr Curr Low (A)', '0BFE0', 'float'),
 ('=======================', '0FFAB',
  'long'), ('Batt Bus Voltage (V)', '0CF22', 'float'), (
      'Batt Bus Current (A)', '0CF23', 'float'), (
          'Arr Bus Voltage (V)', '0BFE2', 'float'), (
              'Arr Bus Current (A)', '0BFE3', 'float'), (
                  '=======================', '0FFAE', 'long'), (
                      'Main LP Sys Current (A)', '0CF24', 'float'), (
                          'PPT LP Sys Current (A)', '0BFE4', 'float'), (
                              '=======================', '0FFAC', 'long'), (
                                  'EM_BATT Temp (deg C)', '0CF3A', 'float'), (
                                      'EM_ARR Temp (deg C)', '0BFFA', 'float'),
 ('Max Module Voltage (V)', '01F23', 'float'), (
     'Ave Module Voltage (V)', '01F24',
     'float'), ('Min Module Voltage (V)', '01F25', 'float'), (
         'Max Module Temp (deg C)', '01F26', 'float'), (
             'Ave Module Temp (deg C)', '01F27', 'float'), (
                 'Min Module Temp (deg C)', '01F28', 'float'), (
                     'Total Stack Voltage (V)', '01F22', 'float'), (
                         'Max Module Voltage (V)', '01F23', 'float'), (
                             'Ave Module Voltage (V)', '01F24', 'float'), (
                                 'Min Module Voltage (V)', '01F25', 'float'),
 ('Total Bus Voltage (V)',
  '01F22', 'float'), ('Batt Bus Current (A)', '0CF23', 'float'), (
      'Arr Bus Current (A)', '0BFE3', 'float'), (
          'Main LP Sys Power (W)', '0CF2A', 'float'), (
              'Misc Power (W)', '0CF2C', 'float'), (
                  'PPT LP Sys Power (W)', '0BFEA', 'float'), (
                      'can0_tx_map[0]', '0AF00', 'hex string'), (
                          'can0_tx_map[1]', '0AF01', 'hex string'), (
                              'can0_tx_map[2]', '0AF02', 'hex string'), (
                                  'can0_tx_map[3]', '0AF03', 'hex string'), (
                                      'can0_tx_map[4]', '0AF04', 'hex string'),
 ('can0_tx_map[5]', '0AF05', 'hex string'), (
     'can0_tx_map[6]', '0AF06', 'hex string'), (
         'can0_tx_map[7]', '0AF07', 'hex string'), (
             'can0_write_lock', '0AF08', 'hex string'), (
                 'local_sw_version', '0AF09', 'float'), (
                     'local_con_stat_word', '0AF0A', 'hex string'), (
                         'local_con_stat_word_2', '0AF0B', 'hex string'), (
                             'lcs_write_window', '0AF0C', 'hex string'), (
                                 'can0_error_stats', '0AF0D', 'hex string'),
 ('bbc_can1_error_stats',
  '0AF0E', 'hex string'), ('can0_tx_map[0]', '0BF00', 'hex string'), (
      'can0_tx_map[1]', '0BF01', 'hex string'), (
          'can0_tx_map[2]', '0BF02', 'hex string'), (
              'can0_tx_map[3]', '0BF03', 'hex string'), (
                  'can0_tx_map[4]', '0BF04', 'hex string'), (
                      'can0_tx_map[5]', '0BF05', 'hex string'), (
                          'can0_tx_map[6]', '0BF06', 'hex string'), (
                              'can0_tx_map[7]', '0BF07', 'hex string'), (
                                  'can0_write_lock', '0BF08', 'hex string'), (
                                      'local_sw_version', '0BF09', 'float'),
 ('local_con_stat_word', '0BF0A', 'hex string'), (
     'local_con_stat_word_2', '0BF0B', 'hex string'), (
         'lcs_write_window', '0BF0C', 'hex string'), (
             'can0_error_stats', '0BF0D', 'hex string'), (
                 'bbc_can1_error_stats', '0BF0E', 'hex string'), (
                     'Serial Number (#)', '0AF21', 'long'), (
                         'Active Motor (#)', '0AF23', 'long'), (
                             '=======================', '0FFAA', 'long'), (
                                 '1.2V supply (V)', '0AF32', 'float'), (
                                     '1.65V reference (V)', '0AF30', 'float'),
 ('2.5V supply (V)', '0AF33', 'float'), ('15V supply (V)', '0AF31', 'float'), (
     '=======================', '0FFAC', 'long'),
 ('Fan Drive (%*)', '0AF34', 'float'), ('Fan Speed (RPM)', '0AF35', 'float'), (
     '=======================', '0AFAD', 'long'), (
         'Air Inlet Temp (deg C)', '0AF39', 'float'), (
             'Processor Temp (deg C)', '0AF38', 'float'), (
                 'Capacitor Temp (deg C)', '0AF3A', 'float'), (
                     'Heatsink Temp (deg C)', '0AF37', 'float'), (
                         'Air Outlet Temp (deg C)', '0AF3B', 'float'), (
                             'Motor Temp (deg C)', '0AF36', 'float'), (
                                 'Bus Voltage (V)', '0AF24', 'float'),
 ('Bus Current (A)', '0AF25', 'float'), ('Bus Power (W)', '0AF42', 'float'), (
     '=======================', '0FFAB', 'long'), ('Vd (V)', '0AF2B', 'float'),
 ('Vq (V)', '0AF2A', 'float'), ('=======================', '0FFAC', 'long'), (
     'BEMFd (V)', '0AF2F', 'float'), ('BEMFq (V)', '0AF2E', 'float'), (
         '=======================', '0FFAD',
         'long'), ('Id (A)', '0AF2D', 'float'), ('Iq (A)', '0AF2C', 'float'), (
             '=======================', '0FFAE',
             'long'), ('Phase A Current (Arms)', '0AF29', 'float'), (
                 'Phase B Current (Arms)', '0AF28',
                 'float'), ('Panel Voltage (V)', '0BF60', 'float'), (
                     'Panel Power (W)', '0BF61', 'float'), (
                         'Battery Voltage (V)', '0BF62', 'float'), (
                             'Battery Current (A)', '0BF63', 'float'), (
                                 '1.2V supply (V)', '0AF32', 'float'), (
                                     '1.65V reference (V)', '0AF30', 'float'),
 ('2.5V supply (V)', '0AF33', 'float'), ('15V supply (V)', '0AF31', 'float'), (
     'Air Inlet Temp (deg C)', '0AF39', 'float'), (
         'Processor Temp (deg C)', '0AF38', 'float'), (
             'Capacitor Temp (deg C)', '0AF3A', 'float'), (
                 'Heatsink Temp (deg C)', '0AF37', 'float'), (
                     'Air Outlet Temp (deg C)', '0AF3B', 'float'), (
                         'Motor Temp (deg C)', '0AF36', 'float'),
 ('Fan Drive (%*)', '0AF34', 'float'), ('Fan Speed (RPM)', '0AF35', 'float'), (
     'Bus Voltage (V)', '0AF24', 'float'), (
         'Bus Current (A)', '0AF25',
         'float'), ('Vehicle Speed (km/h)', '0AF41', 'float'), (
             'Target1 Speed (km/h)',
             '0AF83', 'float'), ('Target2 Speed (km/h)', '0AF84', 'float'), (
                 '=======================', '0AFAC',
                 'long'), ('Throttle Position (%)', '0AF80', 'float'), (
                     'dctrls_cc_throttle_lock (%)', '0AF86', 'float'), (
                         'Regen Brake Position (%)', '0AF81', 'float'), (
                             '=======================', '0AFAB', 'long'), (
                                 'Bus Current Factor (%)', '0AF82', 'float'),
 ('=======================', '0FFAA', 'long'), (
     'Driver Int Batt Level (%)', '00F42',
     'long'), ('=======================', '0FFAD', 'long'), (
         'Steering Angle (%)', '06F80',
         'float'), ('Throttle Position (%)', '0AF80', 'float'), (
             'dctrls_cc_throttle_lock (%)', '0AF86',
             'float'), ('Regen Brake Position (%)', '0AF81', 'float'), (
                 'Panel0 Power (W)', '0BF61', 'float'), (
                     'Panel1 Power (W)', '0BF65', 'float'), (
                         'Panel2 Power (W)', '0BF69', 'float'), (
                             'Panel3 Power (W)', '0BF6D', 'float'), (
                                 'Panel4 Power (W)', '0BF71', 'float'), (
                                     'Panel5 Power (W)', '0BF75', 'float'), (
                                         'Panel6 Power (W)', '0BF79', 'float'),
 ('Panel7 Power (W)', '0BF7D', 'float'), (
     'Panel8 Power (W)', '0BF81', 'float'), (
         'Panel9 Power (W)', '0BF85', 'float'), (
             'Panel0 Voltage (V)', '0BF60', 'float'), (
                 'Panel1 Voltage (V)', '0BF64', 'float'), (
                     'Panel2 Voltage (V)', '0BF68', 'float'), (
                         'Panel3 Voltage (V)', '0BF6C', 'float'), (
                             'Panel4 Voltage (V)', '0BF70', 'float'), (
                                 'Panel5 Voltage (V)', '0BF74', 'float'), (
                                     'Panel6 Voltage (V)', '0BF78', 'float'),
 ('Panel7 Voltage (V)', '0BF7C', 'float'), (
     'Panel8 Voltage (V)', '0BF80', 'float'), (
         'Panel9 Voltage (V)', '0BF84', 'float'), (
             'can_tx_map[0]', '05F00', 'hex string'), (
                 'can_tx_map[1]', '05F01', 'hex string'), (
                     'can_tx_map[2]', '05F02', 'hex string'), (
                         'can_tx_map[3]', '05F03', 'hex string'), (
                             'can_tx_map[4]', '05F04', 'hex string'), (
                                 'can_tx_map[5]', '05F05', 'hex string'), (
                                     'can_tx_map[6]', '05F06', 'hex string'),
 ('can_tx_map[7]', '05F07', 'hex string'), (
     'can_write_lock',
     '05F08', 'hex string'), ('local_sw_version', '05F09', 'float'), (
         'local_con_stat_word', '05F0A', 'hex string'), (
             'local_con_stat_word_2', '05F0B', 'hex string'), (
                 'lcs_write_window', '05F0C', 'hex string'), (
                     'can_error_stats', '05F0D', 'hex string'), (
                         'Phone GPS Lat (deg)', '00F40',
                         'float'), ('Phone GPS Lon (deg)', '00F41', 'float'), (
                             '=======================', '0FFAA', 'long'), (
                                 'Garmin GPS Lat (deg)', '0EF00', 'float'), (
                                     'Garmin GPS Lon (deg)', '0EF01', 'float'),
 ('=======================', '0FFAB', 'long'), (
     'Wind Magnitude (m/s)', '0EF02',
     'float'), ('Wind Direction (deg)', '0EF03', 'float'), (
         '=======================', '0FFAC',
         'long'), ('LF Tire Pressure (psi)', '00F60', 'float'), (
             'RF Tire Pressure (psi)', '00F61', 'float'), (
                 'LR Tire Pressure (psi)', '00F62', 'float'), (
                     'RR Tire Pressure (psi)', '00F63', 'float'), (
                         'Wind Magnitude (m/s)', '0EF02', 'float'), (
                             'Wind Direction (deg)', '0EF03', 'float'), (
                                 'Current Mark Num (#)', '00F26', 'long'), (
                                     'Current Stint Num (#)', '00F24', 'long'),
 ('bbc_relay_map', '0AF10', 'hex string'), (
     'bbc_relay_timeout_map', '0AFA0',
     'hex string'), ('bbc_relay_map', '0BF10', 'hex string'), (
         'bbc_relay_timeout_map', '0BFA0', 'hex string'), (
             'Current Stint Time (s)', '00F25',
             'float'), ('Previous Stint Time (s)', '00F28', 'float'), (
                 'Panel Voltage (V)', '0BF64',
                 'float'), ('Panel Power (W)', '0BF65', 'float'), (
                     'Battery Voltage (V)', '0BF66',
                     'float'), ('Battery Current (A)', '0BF67', 'float'), (
                         'Panel Voltage (V)', '0BF68',
                         'float'), ('Panel Power (W)', '0BF69', 'float'), (
                             'Battery Voltage (V)', '0BF6A', 'float'), (
                                 'Battery Current (A)', '0BF6B', 'float'), (
                                     'Panel Voltage (V)', '0BF6C', 'float'), (
                                         'Panel Power (W)', '0BF6D', 'float'),
 ('Battery Voltage (V)', '0BF6E', 'float'), (
     'Battery Current (A)', '0BF6F',
     'float'), ('Panel Voltage (V)', '0BF70', 'float'), (
         'Panel Power (W)', '0BF71', 'float'), (
             'Battery Voltage (V)', '0BF72', 'float'), (
                 'Battery Current (A)', '0BF73', 'float'), (
                     'Panel Voltage (V)', '0BF74', 'float'), (
                         'Panel Power (W)', '0BF75', 'float'), (
                             'Battery Voltage (V)', '0BF76', 'float'), (
                                 'Battery Current (A)', '0BF77', 'float'), (
                                     'Panel Voltage (V)', '0BF78', 'float'), (
                                         'Panel Power (W)', '0BF79', 'float'),
 ('Battery Voltage (V)', '0BF7A', 'float'), (
     'Battery Current (A)', '0BF7B',
     'float'), ('Panel Voltage (V)', '0BF7C', 'float'), (
         'Panel Power (W)', '0BF7D', 'float'), (
             'Battery Voltage (V)', '0BF7E', 'float'), (
                 'Battery Current (A)', '0BF7F', 'float'), (
                     'Panel Voltage (V)', '0BF80', 'float'), (
                         'Panel Power (W)', '0BF81', 'float'), (
                             'Battery Voltage (V)', '0BF82', 'float'), (
                                 'Battery Current (A)', '0BF83', 'float'), (
                                     'Panel Voltage (V)', '0BF84', 'float'), (
                                         'Panel Power (W)', '0BF85', 'float'),
 ('Battery Voltage (V)', '0BF86', 'float'), (
     'Battery Current (A)', '0BF87', 'float'), (
         'Set 1 Acc X (Gs)', '06F20', 'float'), (
             'Set 1 Acc Y (Gs)', '06F21', 'float'), (
                 'Set 1 Acc Z (Gs)', '06F22', 'float'), (
                     'Set 1 Rot X (deg/S)', '06F23', 'float'), (
                         'Set 1 Rot Y (deg/S)', '06F24', 'float'), (
                             'Set 1 Rot Z (deg/S)', '06F25', 'float'), (
                                 'Set 1 Mag X (mGauss)', '06F26', 'float'), (
                                     'Set 1 Mag Y (mGauss)', '06F27', 'float'),
 ('Set 1 Mag Z (mGauss)', '06F28', 'float'), (
     '\t=======================', '0FFAA', 'long'), (
         'Sample Cnt (# of sub-sampl.)', '06F60', 'long'), (
             'Set 1 Mag Heading (deg)', '06F61', 'float'), (
                 'Set 1 Acc X (Gs)', '06F20', 'float'), (
                     'Set 1 Acc Y (Gs)', '06F21', 'float'), (
                         'Set 1 Acc Z (Gs)', '06F22', 'float'), (
                             'Set 1 Rot X (deg/S)', '06F23', 'float'), (
                                 'Set 1 Rot Y (deg/S)', '06F24', 'float'), (
                                     'Set 1 Rot Z (deg/S)', '06F25', 'float'),
 ('Batt En-Cnt Front (Wh)', '0CF28',
  'float'), ('Arr En-Cnt 1 (Wh)', '0BFEF', 'float'), (
      'Motor En-Cnt (Wh)', '0CF2F', 'float'), (
          'Batt En-Cnt Front (Wh)', '0CF28', 'float'), (
              'Batt En-Cnt Back (Wh)', '0CF29', 'float'), (
                  'Main LP Sys En-Cnt (Wh)', '0CF2B', 'float'), (
                      'Misc En-Cnt (Wh)', '0CF2D', 'float'),
 ('PPT LP Sys En-Cnt (Wh)', '0BFEB', 'float'), ('Vd (V)', '0AF2B', 'float'), (
     'Vq (V)', '0AF2A', 'float'), ('BEMFd (V)', '0AF2F', 'float'), (
         'BEMFq (V)', '0AF2E', 'float'), ('Id (A)', '0AF2D', 'float'), (
             'Iq (A)', '0AF2C',
             'float'), ('Phase A Current (Arms)', '0AF29', 'float'), (
                 'Phase B Current (Arms)', '0AF28',
                 'float'), ('Vehicle Speed (km/h)', '0AF41', 'float'), (
                     'Target1 Speed (km/h)', '0AF83',
                     'float'), ('Target2 Speed (km/h)', '0AF84', 'float'), (
                         'Motor Velocity (RPM)', '0AF26', 'float'), (
                             'Vehicle Velocity (m/s)', '0AF27', 'float'), (
                                 '=======================', '0FFAA', 'long'),
 ('Motor Tourque Const (Nm/A)',
  '0AF11', 'float'), ('Motor Thrust (N)', '0AF43', 'float'), (
      '=======================', '0FFAB', 'long'), (
          'Mech Power (W)', '0AF44', 'float'), (
              'Bus Power (W)', '0AF42', 'float'), (
                  '=======================', '0FFAC', 'long'), (
                      'DC Bus AmpHours (Ah)', '0AF3D', 'float'), (
                          'Odometer (m)', '0AF3C', 'float'), (
                              'Odometer (km)', '0AF40', 'float'), (
                                  'Motor Velocity (RPM)', '0AF26', 'float'), (
                                      'Motor Thrust (N)', '0AF43', 'float'),
 ('Mech Power (W)', '0AF44', 'float'), ('Bus Power (W)', '0AF42', 'float'), (
     'DC Bus AmpHours (Ah)', '0AF3D',
     'float'), ('Aux Temp 0 (deg C)', '01F38', 'float'), (
         'Aux Temp 1 (deg C)', '01F39', 'float'), (
             'Aux Temp 2 (deg C)', '01F3A', 'float'), (
                 'Aux Temp 3 (deg C)', '01F3B', 'float'), (
                     'Aux Temp 4 (deg C)', '01F3C', 'float'), (
                         'Aux Temp 5 (deg C)', '01F3D', 'float'), (
                             '=======================', '0FFAA', 'long'), (
                                 'Max Module Temp (deg C)', '01F26', 'float'),
 ('Ave Module Temp (deg C)', '01F27',
  'float'), ('Min Module Temp (deg C)', '01F28', 'float'), (
      'Aux Temp 0 (deg C)', '01F38', 'float'), (
          'Aux Temp 1 (deg C)', '01F39', 'float'), (
              'Aux Temp 2 (deg C)', '01F3A', 'float'), (
                  'Aux Temp 3 (deg C)', '01F3B', 'float'), (
                      'Aux Temp 4 (deg C)', '01F3C', 'float'), (
                          'Aux Temp 5 (deg C)', '01F3D', 'float'), (
                              'LF Tire Pressure (psi)', '00F60', 'float'), (
                                  'RF Tire Pressure (psi)', '00F61', 'float'),
 ('LR Tire Pressure (psi)', '00F62',
  'float'), ('RR Tire Pressure (psi)', '00F63', 'float'), (
      'Driver Int Batt Level (%)', '00F42',
      'long'), ('Batt En-Cnt Front (Wh)', '0CF28', 'float'), (
          'Batt En-Cnt Back (Wh)', '0CF29', 'float'), (
              'Arr En-Cnt 1 (Wh)', '0BFEF', 'float'), (
                  'Arr En-Cnt 2 (Wh)', '0BFE8', 'float'), (
                      'Motor En-Cnt (Wh)', '0CF2F', 'float'), (
                          '=======================', '0FFAA', 'long'), (
                              'Main LP Sys En-Cnt (Wh)', '0CF2B', 'float'), (
                                  'Misc En-Cnt (Wh)', '0CF2D', 'float'),
 ('PPT LP Sys En-Cnt (Wh)', '0BFEB',
  'float'), ('Batt Power Front (W)', '0CF25', 'float'), (
      'Arr Bus Power 1 (W)', '0BFEE', 'float'), (
          'Motor Power (W)', '0CF2E', 'float'), (
              'Batt Bus Voltage (V)', '0CF22', 'float'), (
                  'Arr Bus Voltage (V)', '0BFE2', 'float'), (
                      'Batt Power Front (W)', '0CF25', 'float'), (
                          'Batt Transfer Eff (%)', '0CF26', 'float'), (
                              'Batt Power Back (W)', '0CF27', 'float'), (
                                  'Arr Bus Power 1 (W)', '0BFEE', 'float'), (
                                      'Arr Bus Power 2 (W)', '0BFE5', 'float'),
 ('Motor Power (W)', '0CF2E',
  'float'), ('=======================', '0FFAD', 'long'), (
      'Main LP Sys Power (W)', '0CF2A', 'float'), (
          'Misc Power (W)', '0CF2C', 'float'), (
              'PPT LP Sys Power (W)', '0BFEA', 'float'), (
                  'Main LP Sys Current (A)', '0CF24', 'float'), (
                      'PPT LP Sys Current (A)', '0BFE4', 'float'), (
                          'EM_BATT Temp (deg C)', '0CF3A', 'float'), (
                              'EM_ARR Temp (deg C)', '0BFFA', 'float'), (
                                  'Batt Power Front (W)', '0CF25', 'float'), (
                                      'Batt Power Back (W)', '0CF27', 'float'),
 ('Batt Transfer Eff (%)', '0CF26', 'float'), (
     'Steering Angle (%)', '06F80',
     'float'), ('can_tx_map[0]', '0BFC0', 'hex string'), (
         'can_tx_map[1]', '0BFC1', 'hex string'), (
             'can_tx_map[2]', '0BFC2',
             'hex string'), ('can_tx_map[3]', '0BFC3', 'hex string'), (
                 'can_tx_map[4]', '0BFC4', 'hex string'), (
                     'can_tx_map[5]', '0BFC5', 'hex string'), (
                         'can_tx_map[6]', '0BFC6', 'hex string'), (
                             'can_tx_map[7]', '0BFC7', 'hex string'), (
                                 'can_write_lock', '0BFC8', 'hex string'), (
                                     'local_sw_version', '0BFC9', 'float'),
 ('local_con_stat_word', '0BFCA', 'hex string'), (
     'local_con_stat_word_2',
     '0BFCB', 'hex string'), ('lcs_write_window', '0BFCC', 'hex string'), (
         'can_error_stats', '0BFCD', 'hex string'), (
             'Module 23 Voltage (V)', '02F4B',
             'float'), ('Module 22 Voltage (V)', '02F4A', 'float'), (
                 'Module 21 Voltage (V)', '02F49',
                 'float'), ('Module 20 Voltage (V)', '02F48', 'float'), (
                     'Module 19 Voltage (V)', '02F47',
                     'float'), ('Module 18 Voltage (V)', '02F46', 'float'), (
                         'Module 17 Voltage (V)', '02F45', 'float'), (
                             'Module 16 Voltage (V)', '02F44', 'float'), (
                                 'Module 15 Voltage (V)', '02F43', 'float'),
 ('\tModule 14 Voltage (V)',
  '02F42', 'float'), ('Module 13 Voltage (V)', '02F41', 'float'), (
      'Module 12 Voltage (V)', '02F40', 'float'), (
          'Module 35 Voltage (V)', '03F4B', 'float'), (
              'Module 34 Voltage (V)',
              '03F4A', 'float'), ('Module 33 Voltage (V)', '03F49', 'float'), (
                  'Module 32 Voltage (V)', '03F48', 'float'), (
                      'Module 31 Voltage (V)', '03F47', 'float'), (
                          'Module 30 Voltage (V)', '03F46', 'float'), (
                              'Module 29 Voltage (V)', '03F45', 'float'), (
                                  'Module 28 Voltage (V)', '03F44', 'float'),
 ('Module 27 Voltage (V)', '03F43', 'float'), (
     'Module 26 Voltage (V)', '03F42',
     'float'), ('Module 25 Voltage (V)', '03F41', 'float'), (
         'Module 24 Voltage (V)', '03F40', 'float'), (
             'Module 9 Temp (deg C)',
             '02F84', 'float'), ('Module 8 Temp (deg C)', '02F83', 'float'), (
                 'Module 7 Temp (deg C)', '02F82', 'float'), (
                     'Module 6 Temp (deg C)', '02F81', 'float'), (
                         'Module 5 Temp (deg C)', '02F80', 'float'), (
                             'Module 14 Temp (deg C)', '03F84', 'float'), (
                                 'Module 13 Temp (deg C)', '03F83', 'float'),
 ('Module 12 Temp (deg C)', '03F82', 'float'), (
     'Module 11 Temp (deg C)', '03F81',
     'float'), ('Module 10 Temp (deg C)', '03F80', 'float'), (
         'Set 1 Mag X (mGauss)', '06F26', 'float'), (
             'Set 1 Mag Y (mGauss)', '06F27', 'float'), (
                 'Set 1 Mag Z (mGauss)', '06F28', 'float'), (
                     'Set 2 Rot X (deg/S)', '06F35', 'float'), (
                         'Set 2 Rot Y (deg/S)', '06F36', 'float'), (
                             'Set 2 Rot Z (deg/S)', '06F37', 'float'), (
                                 'Set 2 Mag X (mGauss)', '06F38', 'float'), (
                                     'Set 2 Mag Y (mGauss)', '06F39', 'float'),
 ('Set 2 Mag Z (mGauss)', '06F3A', 'float'), (
     'Set 2 Acc X (Gs)', '06F32', 'float'), (
         'Set 2 Acc Y (Gs)', '06F33', 'float'), (
             'Set 2 Acc Z (Gs)', '06F34',
             'float'), ('Set 2 Acc X (Gs)', '06F32', 'float'), (
                 'Set 2 Acc Y (Gs)', '06F33', 'float'), (
                     'Set 2 Acc Z (Gs)', '06F34', 'float'), (
                         'Set 2 Rot X (deg/S)', '06F35', 'float'), (
                             'Set 2 Rot Y (deg/S)', '06F36', 'float'), (
                                 'Set 2 Rot Z (deg/S)', '06F37', 'float'), (
                                     'Set 2 Mag X (mGauss)', '06F38', 'float'),
 ('Set 2 Mag Y (mGauss)', '06F39', 'float'), (
     'Set 2 Mag Z (mGauss)', '06F3A',
     'float'), ('\t=======================', '0FFAA', 'long'), (
         'Sample Cnt (# of sub-sampl.)', '06F60',
         'long'), ('Set 2 Mag Heading (deg)', '06F63', 'float'), (
             'Set 1 Mag Heading (deg)', '06F61', 'float'), (
                 'Set 2 Mag Heading (deg)', '06F63', 'float'), (
                     'Total Stack Voltage (V)', '02F22', 'float'), (
                         'Max Module Voltage (V)', '02F23', 'float'), (
                             'Ave Module Voltage (V)', '02F24', 'float'), (
                                 'Min Module Voltage (V)', '02F25', 'float'),
 ('Total Stack Voltage (V)', '03F22', 'float'), (
     'Max Module Voltage (V)', '03F23', 'float'), (
         'Ave Module Voltage (V)', '03F24', 'float'), (
             'Min Module Voltage (V)', '03F25', 'float'), (
                 'Aux Temp 0 (deg C)', '02F38', 'float'), (
                     'Aux Temp 1 (deg C)', '02F39', 'float'), (
                         'Aux Temp 2 (deg C)', '02F3A', 'float'), (
                             'Aux Temp 3 (deg C)', '02F3B', 'float'), (
                                 'Aux Temp 4 (deg C)', '02F3C', 'float'), (
                                     'Aux Temp 5 (deg C)', '02F3D', 'float'),
 ('=======================', '0FFAA',
  'long'), ('Max Module Temp (deg C)', '02F26', 'float'), (
      'Ave Module Temp (deg C)', '02F27', 'float'), (
          'Min Module Temp (deg C)', '02F28', 'float'), (
              'Aux Temp 0 (deg C)', '03F38', 'float'), (
                  'Aux Temp 1 (deg C)', '03F39', 'float'), (
                      'Aux Temp 2 (deg C)', '03F3A', 'float'), (
                          'Aux Temp 3 (deg C)', '03F3B', 'float'), (
                              'Aux Temp 4 (deg C)', '03F3C', 'float'), (
                                  'Aux Temp 5 (deg C)', '03F3D', 'float'),
 ('=======================', '0FFAA', 'long'), (
     'Max Module Temp (deg C)', '03F26',
     'float'), ('Ave Module Temp (deg C)', '03F27',
                'float'), ('Min Module Temp (deg C)', '03F28', 'float'), (
                    'Module 36 Voltage (V)', '0CF60', 'float')]
