import pytest

from sysex.MidisportSysex import MidisportSysex


class TestSysex:

    def test_has_manufacturer_id(self):
        sysex = MidisportSysex('')
        assert sysex.get_manufacturer_id() == '00 01 05'

    def test_has_device_id(self):
        sysex = MidisportSysex('')
        assert sysex.get_device_id() == '7F 00 00 04 00 01'

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ("", ""),
            ('12345', 'F0 00 01 05 7F 00 00 04 00 01 12345 F7')

        ]
    )
    def test_get_correct_sysex_for_body(self, test_input, expected):
        sysex = MidisportSysex(test_input)

        assert sysex.get() == expected
