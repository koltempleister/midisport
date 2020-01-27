import os

import mido
import rtmidi


class MidiHandler(object):

    def get_devices(self):

        devices = []
        lines = os.popen('amidi -l').read().splitlines()

        for line in lines[1:]:
            mode, device, name = line.strip().split(None, 2)

            devices.append({'name': name.strip(),
                            'device': device,
                            'is_input': 'I' in mode,
                            'is_output': 'O' in mode,
                            })

        return devices

    def set_device(self, device):
        self.device = device

    def get_device(self, name):
        for device in self.get_devices():
            if name == device['name']:
                return device

        raise Exception('Device not found')

        return False

    def send(self, message):
        command = 'amidi -p ' + self.device + ' -S ' + message + ' -d -t 1'
        response = os.popen(command)
        return response
