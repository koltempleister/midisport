
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


class Preset():

    def set_name(self, name):
        self.name = name
        self.__check_name()

    def set_value(self, value):
        self.value = value

    def __check_name(self):
        if self.name == "": raise Exception("Name is empty")

    def get_name(self):
        self.__check_name()
        return self.name

    def get_value(self):
        return self.value