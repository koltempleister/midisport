class MidisportSysex:
    manufacturer_id = '00 01 05'
    device_id = '7F 00 00 04 00 01'

    def __init__(self, body):
        self.body = body

    def get_manufacturer_id(self):
        return self.manufacturer_id

    def get_device_id(self):
        return self.device_id

    def get(self):
        if len(self.body) == 0: return ""
        return "F0 " + self.get_manufacturer_id() + " " + self.get_device_id() + " " + self.body + " F7"
