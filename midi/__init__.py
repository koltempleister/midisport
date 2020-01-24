class Parser:
    n_ports = 8

    def config_2_hex(self, config):

        out = []
        # return '00 04 00 04 03 00 0C 00 00 02 01 00 00 06 00 00'

        for in_port in config.keys():
            print('PORT' + str(in_port))
            str1 = ''
            str2 = ''

            for binary_string in self.parse_port(config.get(in_port)):
                out.append(self.bin2hex(binary_string))
            # for port in range(self.n_ports):
            #     # print('checking' + str(port))
            #     if port < 4:
            #         # str1 = str1 + str(int(str(port) in in_port))
            #         str1 = str1 + str(int(port in config.get(in_port)))
            #         # print('ok' + str1)
            #     else:
            #         str2 = str2 + str(int(port in config.get(in_port)))
            #
            # # apply hex to the reverse of the string ([::-1]) turned into int
            # print('str1:' + str1)
            # print('str2:' + str2)
            # out.append(str(int(str1[::-1], 2)) + str(int(str2[::-1], 2)))
            # # out.append(hex(int(str1[::-1], 2)) + hex(int(str2[::-1], 2)))

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

        return [str1, str2]
