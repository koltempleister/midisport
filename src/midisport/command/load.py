
from midisport.instructionparser import PortMapSysexParser
from midisport.preset.preset import Preset
from midisport.sysex.MidisportSysex import MidisportSysex
from midisport.sysex.midi import AMidiHandler, Device, MidiHandlerInterface


class PresetLoader(object):
    _parser: PortMapSysexParser
    _midihandler: MidiHandlerInterface
    _midisport_sysex: MidisportSysex


    def __init__(
            self,
            portmapsysexparser: PortMapSysexParser,
            midihandler: MidiHandlerInterface,
            midisport_sysex: MidisportSysex
            ):
        self._parser = portmapsysexparser
        self._midihandler = midihandler
        self._midisport_sysex = midisport_sysex

    def execute(self, preset: Preset, device: Device):
        sysex = self._parser.out(preset)

        self._midihandler.set_device(device)

        output = self._midihandler.send(self._midisport_sysex.get(sysex))

        print(output)

    @staticmethod
    def factory():
        return PresetLoader(PortMapSysexParser(),AMidiHandler(),MidisportSysex())
