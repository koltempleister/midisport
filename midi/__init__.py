class Parser:
    n_ports = 8

    def config_2_hex(self, config):

        out = []
        # return '00 04 00 04 03 00 0C 00 00 02 01 00 00 06 00 00'

        for in_port in config.keys():
            print('PORT' + str(in_port))
            str1 = ''
            str2 = ''

            for port in range(self.n_ports):
                # print('checking' + str(port))
                if port < 4:
                    # str1 = str1 + str(int(str(port) in in_port))
                    str1 = str1 + str(int(port in config.get(in_port)))
                    # print('ok' + str1)
                else:
                    str2 = str2 + str(int(port in config.get(in_port)))

            # apply hex to the reverse of the string ([::-1]) turned into int
            print('str1:' + str1)
            print('str2:' + str2)
            out.append(str(int(str1[::-1], 2)) + str(int(str2[::-1], 2)))
            # out.append(hex(int(str1[::-1], 2)) + hex(int(str2[::-1], 2)))

        return ' '.join(out)

    def convert(self, bin):
        # print "0x%x" % int(bin, 2)
        hex = "0x%x" % int(bin, 2)

        return hex.upper()
        # return hex(int(bin, 2))

    def strip(self, hex):
        return hex[:1] + hex[-1]

    # # WIP
    # def parse_port(self, input):
    #     for i in input:
    #         if i < 4:
    #             # str1 = str1 + str(int(str(port) in in_port))
    #             str1 = str1 + str(int(port in config.get(in_port)))
    #             # print('ok' + str1)
    #         else:
    #             str2 = str2 + str(int(port in config.get(in_port)))