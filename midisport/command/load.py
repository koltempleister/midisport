class Load(object):

    def __init__(self, preset, portmapsysexparser):
        self.preset = preset
        self.parser = portmapsysexparser

    # self.preset = preset

    def execute(self):
        return self.parser.out(self.preset)
