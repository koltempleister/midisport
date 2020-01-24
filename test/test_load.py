from midisport.command.load import Load
from midisport.instructionparser import PortMapSysexParser
from midisport.preset.preset import Preset


def test_it_loads_a_preset():
    preset = Preset()

    preset.set_id(1)
    preset.set_name('port 1')
    preset.set_value({
        '1': [2],
        '2': [2, 4],
        '3': [3, 4, 5],
        '4': [7],
        '5': [2, 3, 4],
        '6': [4, 5, 6],
        '7': [8],
        '8': [1, 8],
    })

    command = Load(preset, PortMapSysexParser())
    assert command.execute() == '02 00 0A 00 0C 01 00 04 0E 00 08 03 00 08 01 08'
