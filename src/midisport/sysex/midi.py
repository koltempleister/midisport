import os

class Device:
    _name: str
    _device: str
    _mode: str

    def __init__(self, name:str, device: str, mode:str):
        self._name = name
        self._device = device
        self._mode = mode

    def getName(self) -> str:
        return self._name

    def getDevice(self) -> str:
        return self._device

    def getMode(self) -> str:
        return self._mode

class MidiHandlerInterface:
    def get_devices(self)-> list:
        pass

    def set_device(self, device: Device):
        pass

    def get_device(self, name:str)-> Device:
        pass

    def send(self, message: str)->str:
        pass

class AMidiHandler(MidiHandlerInterface):
    _device: Device
    _message: str

    def get_devices(self)-> list:

        devices = []
        lines = os.popen('amidi -l').read().splitlines()

        for line in lines[1:]:
            mode, device, name = line.strip().split(None, 2)
            devices.append(Device(name.strip(), device, mode))
        return devices

    def _deviceExists(self, Device) -> bool:

        for device_from_list in self.get_devices():
            if device_from_list == Device:
                return True

        return False

    def set_device(self, device: Device):

        if not self._deviceExists(device):
            raise Exception('There is no device called \'' + device.getName() + '\'')

        self._device = device

    def get_device(self, name:str)-> Device:
        for device in self.get_devices():
            if name == device.getName():
                return device

        raise Exception('Device \'' + device.getName() + '\' not found')

        return False

    def send(self, message: str)->str:
        command = self._build_command(message)

        response = os.popen(command)
        return response

    def print_command(self, message: str):
        print('executing command', self._build_command(message))

    def _build_command(self, message)->str:

        if not message:
            raise Exception('message is empty')

        if not type(self._device) is Device:
            raise Exception('No device set')

        command = 'amidi -p ' + self._device.getDevice() + ' -S ' + message + ' -d -t 1'
        return command
