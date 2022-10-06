import sys
from unified_modules.test_support.testbaseclass import dut_types
from unified_modules.test_support.testresults import TestResults
from domino_tests.base_output_driver_offset_shift import BaseOutputDriverOffsetShift
from framework.domino_framework import DominoFramework
from framework.firmware_baseclass import FW_TARGET_DEVICES, FW_PROJECTS


@dut_types(FW_TARGET_DEVICES[FW_PROJECTS.Domino])
class Dom7973VerifyOutputDriverAutoCalibration06points001samples(BaseOutputDriverOffsetShift):

    def __init__(self, result=None, test_system=None):
        super(Dom7973VerifyOutputDriverAutoCalibration06points001samples,
              self).__init__(result, test_system)
        # xx_CAL_CTRL Settings
        self.cal_ctrl1.AF_CAL_CTRL = 0
        self.cal_ctrl1.B1_CAL_CTRL = 0
        self.cal_ctrl1.B2_CAL_CTRL = 0

        self.cal_ctrl1.AUTO_CAL_POINTS = 0

        self.cal_ctrl1.DAC_CAL_SAMPLES = 0

        # settling time = 100 us
        self.cal_ctrl1.CAL_SETTLING_TIME = 4
        # Fine 2-bit trims adjusted such that mean DNL is 0.25 LSB
        self.cal_ctrl2.AF_DNL_BIAS = 0
        self.cal_ctrl2.B1_DNL_BIAS = 0
        self.cal_ctrl2.B2_DNL_BIAS = 0


if __name__ == "__main__":
    TEST = Dom7973VerifyOutputDriverAutoCalibration06points001samples(TestResults(),
                                                                      DominoFramework())
    RETURN_CODE, _ = TEST.run()
    sys.exit(RETURN_CODE)
