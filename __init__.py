import os

import tensorflow as tf


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

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

keys = {
    'battle': None,
    'battle_end': None,
    'battle_load_color': None,
    'battle_load_gray': None,
    'black': None,
    'end': 'z',
    'end_icon': None,
    'main': 'x',
    'sanity': None,
    'team': 'a'
    }
