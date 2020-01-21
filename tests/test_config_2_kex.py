from context import midi


def test_config_2_hex():

   config = {
      '1' :  [7],
      '2' :  [7],
      '3' :  [1,2],
      '4' : [3,4],
      '5' : [6],
      '6' : [1],
      '7' : [6,7],
      '8' : [],
   }

   expected = '00 04 00 04 03 00 0C 00 00 02 01 00 00 06 00 00'

   midi_convert = midi.Midi()
   assert midi_convert.config_2_hex(config) == expected