class PortMapSysexParser:
    n_ports = 8

    def out(self, config):

        out = []

        for in_port in config.keys():

            for binary_string in self.parse_port(config.get(in_port)):
                out.append(self.bin2hex(binary_string))

        return ' '.join(out)

    def bin2hex(self, binstring):
        return self.strip(self.convert(binstring))

    def convert(self, binstring):
        hexstring = "0x%x" % int(binstring, 2)

        return hexstring.upper()

    def strip(self, hex):
        return hex[:1] + hex[-1]

    # # WIP
    def parse_port(self, input):
        str1 = ''
        str2 = ''
        port = 1
        while port <= 8:

            if port <= 4:
                str1 = str1 + str(int(port in input))

            else:
                str2 = str2 + str(int(port in input))
            port += 1

        return [str1[::-1], str2[::-1]]
