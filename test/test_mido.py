import mido


def test_show_ports():

   names = mido.get_output_names()

   print(names)