# import os
# import pygame.midi

# source = '/usr/share/alsa/alsa.conf'
# dest = '/usr/local/share/alsa/alsa.conf'




# def create_symlink(source,dest):

#     def check_symlink(link):
#         result = os.path.islink(dest)
#         print('checking if ', dest, 'exists:', result)
#         return result

#     def check_file(file):
#         result = os.path.isfile(file)
#         print('checking if ', file, 'exists:', result)
#         return result

#     if not check_symlink(dest):
#         if not os.path.isdir('/usr/local/share/alsa/'):
#             os.makedirs('/usr/local/share/alsa/')

#         if not check_file(source):
#             raise FileNotFoundError(source, 'not found')

#         print('creating symlink from', source, 'to', dest)
#         os.symlink(source,dest)

# # create_symlink(source, dest)
# pygame.midi.init()
# # ports = pygame.midi.get_count()
# print(pygame.midi.get_default_input_id())

import mido
import mido.backends.rtmidi

print(mido.get_output_names())