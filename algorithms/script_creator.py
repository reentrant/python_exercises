import re

def generate_auto_cal_points_and_cal_samples():
    """
    AUTO_CAL_POINTS = {6, 12, 24, 48} and DAC_CAL_SAMPLES = {1, 2, 4, 8, 16, 32, 64}
    """
    # AUTO_CAL_POINTS bits 8:6
    # 000:	6-point LSF	(6_POINT_LSF)
    # 001:	12-point LSF	(12_POINT_LSF)
    # 010:	24-point LSF	(24_POINT_LSF)
    # 011:	48-point LSF	(48_POINT_LSF)
    # 100:	96-point LSF	(96_POINT_LSF)
    # 101:	192-point LSF	(192_POINT_LSF)
    for m in range(4):
        # print("\tAUTO_CAL_POINTS", i)
        for n in range(8):
            #  DAC_CAL_SAMPLES bits 11:9
            print("tAUTO_CAL_POINTS:\tDAC_CAL_SAMPLES:", m, n)


def generate_calibrations():
    cals = []
    for i in range(4):  # AF_CAL_CTRL: 5:4
        for j in range(4):  # B2_CAL_CTRL bit 3:2
            for k in range(4):  # B1_CAL_CTRL bit 1:0
                cal = [i, j, k]
                if i == j == k:
                    "It already has been tested in DOM-7973"
                else:
                    # print(cal)
                    cals.append(cal)
                    # generate_auto_cal_points_and_cal_samples()
                    for m in range(6):
                        # print("\tAUTO_CAL_POINTS", i)
                        points = 6 * 2 ** m
                        for n in range(8):
                            # DAC_CAL_SAMPLES bits 11:9
                            samples = 2 ** n
                            yield cal + [m, n]


def dom7962(template, cals):
    class_name = "Dom7973VerifyOutputDriverAutoCalibration06points001samples"
    str_af = "cal_ctrl1.AF_CAL_CTRL = "
    str_b1 = "cal_ctrl1.B1_CAL_CTRL = "
    str_b2 = "cal_ctrl1.B2_CAL_CTRL = "
    str_points = "AUTO_CAL_POINTS = "
    str_samples = "DAC_CAL_SAMPLES = "
    af, b1, b2, points, samples = cals
    f_out = open(get_new_file_name(cals), 'w')
    with open(template, "r") as f:
        for line in f:
            if line.find(class_name) > -1:
                f_out.write(line.replace(class_name, update_class_name(cals)))
            elif re.search(str_af, line):
                pattern = str_af + ".+"
                match = re.search(pattern, line)
                if match:
                    new_info = str_af + str(af)
                    f_out.write(line.replace(match.group(), new_info))
            elif re.search(str_b1, line):
                pattern = str_b1 + ".+"
                match = re.search(pattern, line)
                if match:
                    new_info = str_b1 + str(b1)
                    f_out.write(line.replace(match.group(), new_info))
            elif re.search(str_b2, line):
                pattern = str_b2 + ".+"
                match = re.search(pattern, line)
                if match:
                    new_info = str_b1 + str(b2)
                    f_out.write(line.replace(match.group(), new_info))
            # self.cal_ctrl1.AUTO_CAL_POINTS = 0
            elif re.search(str_points, line):
                pattern = str_points + ".+"
                match = re.search(pattern, line)
                if match:
                    new_info = str_points + str(points)
                    f_out.write(line.replace(match.group(), new_info))
            # self.cal_ctrl1.DAC_CAL_SAMPLES = 0
            elif re.search(str_samples, line):
                pattern = str_samples + ".+"
                match = re.search(pattern, line)
                if match:
                    new_info = str_samples + str(samples)
                    f_out.write(line.replace(match.group(), new_info))
            else:
                f_out.write(line)
        f_out.close()


def get_new_file_name(cals):
    i, j, k, m, n = cals
    points = 6 * 2 ** m
    samples = 2 ** n
    string = f"DOM7962_afcal0{i}_B1cal0{j}_B2cal0{k}_Ctrls_Points{points:03}_Samples{samples:03}.py"
    return string


def update_class_name(cals):
    i, j, k, m, n = cals
    points = 6 * 2 ** m
    samples = 2 ** n
    string = f"Dom7962Afcal0{i}B1cal0{j}B2cal0{k}CtrlsPoints{points:03}Samples{samples:03}"
    return string


if __name__ == '__main__':
    template_path = "template.py"
    for cal in generate_calibrations():
        # dom7962(template_path, cal)
        print(update_class_name(cal))
