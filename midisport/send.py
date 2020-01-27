from midisport.command.load import Load
from midisport.instructionparser import PortMapSysexParser
from midisport.preset.preset import Preset
from midisport.sysex.midi import MidiHandler

preset = Preset()
preset.set_id(1)
preset.set_name('port1')
preset.set_value(
    {
        '1': [2],
        '2': [2, 4],
        '3': [3, 4, 5],
        '4': [7],
        '5': [2, 3, 4],
        '6': [4, 5, 6],
        '7': [8],
        '8': [1, 8],
    }
)

load = Load(preset, PortMapSysexParser(), 'UM-2 MIDI 1', MidiHandler())
load.execute()
