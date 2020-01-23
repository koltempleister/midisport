import pytest

from midisport_config.midisport_config import Preset


def test_it_has_a_name():
    preset = Preset()

    preset.set_name('name')

    assert preset.get_name() == 'name'


def test_a_name_should_be_set():
    preset = Preset()

    with pytest.raises(Exception):
        preset.get_name('')


def test_name_cannot_be_empty():
    preset = Preset()

    with pytest.raises(Exception):
        preset.set_name('')

def test_it_has_a_value():
    preset = Preset()

    preset.set_value('value')

    assert preset.get_value() == 'value'