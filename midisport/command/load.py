
class Load(object):

    def __init__(self, preset, portmapsysexparser, device_name, midihandler):
        self.preset = preset
        self.parser = portmapsysexparser
        self.device_name = device_name
        self.midihandler = midihandler

    # self.preset = preset

    def execute(self):
        sysex = self.parser.out(self.preset)

        print(sysex)

        device = self.midihandler.get_device(self.device_name)

        self.midihandler.set_device(
            device['device']
        )
        output = self.midihandler.send(sysex)

        print(output)

