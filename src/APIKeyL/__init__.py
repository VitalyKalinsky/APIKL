"""

Application Programming Interface Key Locator (APIKeyL) v.0.0.0

2025 Vitaly Kalinsky

"""
import xml.etree.ElementTree as ET
from os import listdir
from os.path import isfile, join, splitext
import math
import re
from pathlib import Path