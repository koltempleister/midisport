import midi


def convert(input):
    parser = midi.Parser()
    return parser.convert(input)


def strip(input):
    parser = midi.Parser()
    return parser.strip(input)


# def test_config_2_hex():
#     config = {
#         '1': [2],
#         '2': [2, 4],
#         '3': [3, 4, 5],
#         '4': [7],
#         '5': [2, 3, 4],
#         '6': [4, 5, 6],
#         '7': [8],
#         '8': [1, 8],
#     }
#
#     expected = '02 00 0A 00 0C 01 00 04 0E 00 08 03 00 08 01 08'
#
#     midi_convert = midi.Parser()
#
#     assert midi_convert.config_2_hex(config) == expected


# def test_output:


def test_binary_to_hex():
    assert convert("0101") == "0X5"
    assert convert("1110") == "0XE"
    # assert convert("0001") == "0x5"
    # assert convert("0011") == "0x6"
    # assert convert("0100") == "0x1"


def test_short_hex():
    assert strip("0x5") == "05"
    assert strip("0xe") == "0e"

# #WIP
# def test_parse_port():
#    parser = midi.Parser()
#    assert parser.parse_port([]) == ['0000', '0000']
#    assert parser.parse_port([1]) == ['1000', '0000']