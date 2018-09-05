import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

config_path = PATH('../config/config.json')
classification_path = PATH('../features/json/classification.json')
mcq_path = PATH('../features/json/classification.json')