# import struct
"""
reference: http://www.cse.hcmut.edu.vn/~hungnq/courses/501120/docthem/Single%20precision%20floating-point%20format%20-%20Wikipedia.pdf
"""

def decode_ieee_754_format(value):
    # <----------------------------- 32 bits ------------------------------------->
    # |   sign     |          exponent       |             mantissa               |
    # <-- 1 bit --> <------- 8 bits --------> <-----------  23 bits  ------------->
    sign = decode_sign(value)
    exponent = decode_exponent(value)
    mantissa = decode_mantissa(value)
    return sign * mantissa * 2.0 ** exponent


def decode_sign(value):
    # bit 31
    sign_mask = 0x80000000
    sign = -1 if value & sign_mask else 1
    return sign


def decode_exponent(value):
    # bits 30 - 23
    start_bit = 23
    exponent_mask = 0x7f800000
    bias = 127
    raw_exponent = (value & exponent_mask) >> start_bit
    decoded_exponent = raw_exponent - bias
    return decoded_exponent


def decode_mantissa(value):
    # Convert the mantissa into decimal using the last 23 bits (bit 22 - 0)
    mantissa_mask = 0x7fffff
    mantissa = value & mantissa_mask
    implicit_24th_bit = 0x800000
    decoded_mantissa = implicit_24th_bit | mantissa
    msb_bit = 23
    decoded_mantissa /= 2.0 ** msb_bit
    return decoded_mantissa


# getBin = lambda x: x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]
#
# def floatToBinary64(value):
#     val = struct.unpack('Q', struct.pack('d', value))[0]
#     return getBin(val)
#
# def binary_to_float(value):
#     hx = hex(value)
#     return struct.unpack("d", struct.pack("q", int(hx, 16)))[0]
#     return hx




if __name__ == "__main__":
    print("decode_ieee_754_format: ", decode_ieee_754_format(0x41c80000))
    print("decode_ieee_754_format: ", decode_ieee_754_format(0x41460000))
    print("decode_ieee_754_format: ", decode_ieee_754_format(0x3f800000))
    print("decode_ieee_754_format: ", decode_ieee_754_format(0x3ec00000))
    print("decode_ieee_754_format: ", decode_ieee_754_format(0x42883EFa))

    # print("binary_to_float: ", binary_to_float(0x41c80000))

    # binstr = floatToBinary64(19.5).zfill(64)
    # print('Binary equivalent of 19.5:')
    # print(binstr + '\n')
