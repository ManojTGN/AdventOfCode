import sys
import os

python_dir = os.path.dirname(__file__)
utils_dir = os.path.join(python_dir, os.pardir) + os.sep + 'utils'
root_dir = os.path.abspath(utils_dir)

if root_dir not in sys.path: 
    sys.path.append(root_dir)
