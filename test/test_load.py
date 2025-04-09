import pytest

from midisport.command.load import PresetLoader
from midisport.instructionparser import PortMapSysexParser
from midisport.preset.preset import Preset
from midisport.sysex.MidisportSysex import MidisportSysex
from midisport.sysex.midi import AMidiHandler, Device



@pytest.fixture
def preset():
    preset = Preset()

    preset.set_id(1)
    preset.set_name('port 1')
    preset.set_patch_number(1)
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

    return preset

@pytest.fixture
def device() -> Device:
    return  Device('test device', 'device-0' ,'I')

def test_it_fails_with_unknown_device(preset, device):

    command = PresetLoader(PortMapSysexParser(),AMidiHandler(), MidisportSysex())

    with pytest.raises(Exception):
        command.execute(preset, device)


def test_it_executes_sysex(mocker, preset, device):
    midi = AMidiHandler()
    mock_command = '12345'
    print('device',device.getName(), 'preset', preset)

    # make sure device is recognized
    mocker.patch.object(midi,'get_devices',return_value=[device])


    command = PresetLoader(PortMapSysexParser(),midi, MidisportSysex())

    command.execute(preset, device)
