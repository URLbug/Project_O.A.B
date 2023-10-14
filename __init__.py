import os
import json

import tensorflow as tf


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

IMG_WIDTH = 64
IMG_HEIGHT = 64

dirs = ['battle',
        'battle_end', 
        'battle_load_color',
        'battle_load_gray',
        'black', 
        'end',
        'end_icon',
        'main', 
        'sanity', 
        'team']

keys = json.load(open('./keyboards.json', 'rb'))
