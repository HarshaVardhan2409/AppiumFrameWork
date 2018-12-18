'''
This module contains the path for the supporting files
'''
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

CONFIG_PATH = PATH('../config/config.json')