class MidisportSysex:
    _manufacturer_id: str = '00 01 05'
    _device_id: str = '7F 00 00 04 00 01'

    def get_manufacturer_id(self) -> str:
        return self._manufacturer_id

    def get_device_id(self) -> str:
        return self._device_id

    def get(self, body) -> str:
        if len(body) == 0: return ""
        return "F0 " + self.get_manufacturer_id() + " " + self.get_device_id() + " " + body + " F7"
