# Testing docker setup

import numpy as np
from pathlib import Path

print('the current folder is {}'.format(Path.cwd()))
data = np.arange(1, 55)
print('the average is {}'.format(np.average(data)))
