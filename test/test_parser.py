from midisport import instructionparser
from midisport.preset.preset import Preset


def convert(input):
    parser = instructionparser.PortMapSysexParser()
    return parser.convert(input)


def strip(input):
    parser = instructionparser.PortMapSysexParser()
    return parser.strip(input)


def test_port_map_to_sysex():
    config = {
        '1': [2],
        '2': [2, 4],
        '3': [3, 4, 5],
        '4': [7],
        '5': [2, 3, 4],
        '6': [4, 5, 6],
        '7': [8],
        '8': [1, 8],
    }

    preset = Preset()
    preset.set_value(config)

    expected = '02 00 0A 00 0C 01 00 04 0E 00 08 03 00 08 01 08'

    midi_convert = instructionparser.PortMapSysexParser()

    assert midi_convert.out(preset) == expected


# def test_output:


def test_binary_to_hex():
    assert convert("0101") == "0X5"
    assert convert("1110") == "0XE"

    parser = instructionparser.PortMapSysexParser()
    assert parser.bin2hex('0101') == '05'
    assert parser.bin2hex('1110') == '0E'
    assert parser.bin2hex('0010') == '02'
    assert parser.bin2hex('0100') == '04'


def test_short_hex():
    assert strip("0X5") == "05"
    assert strip("0XE") == "0E"


def test_parse_port():
    parser = instructionparser.PortMapSysexParser()

    assert parser.parse_port([]) == ['0000', '0000']
    assert parser.parse_port([1]) == ['0001', '0000']
    assert parser.parse_port([2, 3, 4, 7]) == ['1110', '0100']
    assert parser.parse_port([1, 8]) == ['0001', '1000']
