
class Config:

    midisport_config = None

    def listPorts(self):

        for port in self.midisport_config.keys():

            print('connections for port ' + str(port))

            connections = self.midisport_config.get(port)
            print(connections)


    def getPorts(self):
        print ("getports")
        # config dictionary
        self.midisport_config = {
            8: [1, 5],
            2: [3, 5],
            3: [2, 3]
        }


print("ok")
#Config.getPorts(Config)
Config.listPorts(Config)
