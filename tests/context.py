import os
import sys

abspath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print(abspath)
sys.path.insert(0, abspath)

import midi