class Preset():

    def set_name(self, name):
        self.name = name
        self.__check_name()

    def set_patch_number(self, patch_number):
        self.patch_number = patch_number

    def get_patch_number(self):
        return self.patch_number

    def set_value(self, value):
        self.value = value

    def __check_name(self):
        if self.name == "":
            raise Exception("Name is empty")

    def get_name(self):
        self.__check_name()
        return self.name

    def get_value(self):
        return self.value

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id