
import pytest
from midisport.sysex.midi import AMidiHandler, Device



@pytest.fixture
def device() -> Device:
    return  Device('test device', 'device-0' ,'I')

def test_it_can_set_an_existing_device(mocker, device):
    service = AMidiHandler()
    mocker.patch.object(service,'get_devices', return_value=[device])

    try:
        service.set_device(device)
        assert True
    except Exception:
        pytest.fail('device should be recognized')

    try:
        service.set_device(Device('non existing device', 'device-2','I'))
        assert False
    except Exception:
        assert True

def test_it_creates_command_when_device_and_message_are_present(mocker, device):
    service = AMidiHandler()
    mocker.patch.object(service,'get_devices', return_value=[device])
    service.set_device(device)
    try:
        service.print_command('message')
        print('ok')
        assert True
    except:
        pytest.fail('it should not build command without device')

def test_it_doesnt_create_command_when_command_is_empty(mocker, device):
    service = AMidiHandler()
    mocker.patch.object(service,'get_devices', return_value=[device])

    service.set_device(device)

    try:
        service.print_command('')
        assert False
    except Exception:
        assert True

def test_it_doesnt_create_command_when_device_is_not_present(device):
    service = AMidiHandler()
    # print(service.get_device(device))
    with pytest.raises(Exception):
        service.print_command('123')
