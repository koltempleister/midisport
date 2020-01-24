
class Load(object):

    def __init__(self, Preset, PortMapSysexParser):
        self.preset = Preset
        self.parser = PortMapSysexParser

    # self.preset = preset

    def execute(self):

        return self.parser.out(self.preset)