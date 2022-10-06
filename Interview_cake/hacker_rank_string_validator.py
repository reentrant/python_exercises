def isValid(s):
    counter = {}
    freq = {}
    for c in s:
        if c in counter.keys():
            counter[c] += 1
        else:
            counter[c] = 1

    for c in counter.keys():
        if counter.get(c) in freq.keys():
            freq[counter.get(c)] += 1
        else:
            freq[counter.get(c)] = 1

    if len(freq.keys()) == 1:

        return "YES"

    elif len(freq.keys()) == 2:
        print(counter.items())
        print(max(freq.keys()) - min(freq.keys()))
        if freq.get(max(freq.keys())) == 1:
            print(max(freq.keys()))
            print(min(freq.keys()))
            if (max(freq.keys()) - min(freq.keys())) == 1:
                return "YES"
            else:
                return "NO"
        else:
            return "NO"

    else:
        return "NO"


list_of_test_cases = [("aabbcd", "NO"),
                          ("aabbccddeefghi", "NO"),
                          ("abcdefghhgfedecba", "YES"),
                          ("aaaabbcc", "NO")]
#
#     @pytest.mark.parametrize("test_input, expected", list_of_test_cases)
#     def test_int32_to_float_power_of_two(self, test_input, expected):
#         dut = ShadowBuffer()
#         assert expected == dut.decode_ieee_754_format(test_input)


def test_1(test_input="aabbcd", expected="NO"):
    assert expected == isValid(test_input)


def test_2(test_input="aabbccddeefghi", expected="NO"):
    assert expected == isValid(test_input)


def test_3(test_input="abcdefghhgfedecba", expected="YES"):
    assert expected == isValid(test_input)


def test_4(test_input="aaaabbcc", expected="NO"):
    assert expected == isValid(test_input)


def test_5(test_input="aabbc", expected="YES"):
    assert expected == isValid(test_input)
