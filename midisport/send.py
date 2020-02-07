from midisport.instructionparser import PortMapSysexParser
from midisport.preset.preset import Preset
from midisport.command.load import Load
from midisport.sysex.midi import MidiHandler

if __name__ == '__main__':


    preset = Preset()
    preset.set_id(1)
    preset.set_name('port1')
    preset.set_value(
        {
            '1': [],
            '2': [],
            '3': [],
            '4': [7],
            '5': [7],
            '6': [4, 5, 6],
            '7': [],
            '8': [],
        }
    )

    load = Load(preset, PortMapSysexParser(), 'MidiSport 8x8 Control', MidiHandler())
    load.execute()
