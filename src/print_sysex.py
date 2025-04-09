from midisport.instructionparser import PortMapSysexParser

from midisport.sysex.midi import AMidiHandler, Device
import presets.preset1

preset = presets.preset1.get()

parser = PortMapSysexParser()
sysex = parser.out(preset)

print(sysex)

device = Device('test device', 'test', 'I')

midi = AMidiHandler()
midi.set_device(device)
midi.print_command(sysex)