class Preset():
    _name: str
    _patch_number: int
    _id: int
    _value: set

    def set_name(self, name: str):
        self._name = name
        self.__check_name()

    def set_patch_number(self, patch_number: int):
        self._patch_number = patch_number

    def get_patch_number(self):
        return self._patch_number

    def set_value(self, value: set):
        self._value = value

    def __check_name(self):
        if self._name == "":
            raise Exception("Name is empty")

    def get_name(self):
        self.__check_name()
        return self._name

    def get_value(self)-> set:
        return self._value

    def set_id(self, id: int):
        self._id = id

    def get_id(self)->int:
        return self._id