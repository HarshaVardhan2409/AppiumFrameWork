'''
This module contains the path for the supporting files
'''
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

config_path = PATH('../config/config.json')
classification_path = PATH('../features/games/templates/classification/classification.json')
mcq_path = PATH('../features/games/templates/mcq/mcq.json')