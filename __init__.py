import os
import json
import warnings
import torch

import tensorflow as tf

from transformers import TrOCRProcessor, VisionEncoderDecoderModel


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

warnings.filterwarnings("ignore")

# tf.config.set_soft_device_placement(True)
# tf.debugging.set_log_device_placement(True)

IMG_WIDTH = 64
IMG_HEIGHT = 64

dirs = ['end',
        'black',
        'sanity',
        'team',
        'battle',
        'end_icon',
        'battle_load_gray',
        'battle_end',
        'main',
        'battle_load_color']

keys = json.load(open('./keyboards.json', 'rb'))

if keys['auto']:
        processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-stage1")
        pipe = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-stage1")
        
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        pipe.to(device)