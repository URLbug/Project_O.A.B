import os
import json
import warnings
import torch

import tensorflow as tf

from transformers import TrOCRProcessor, VisionEncoderDecoderModel


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

warnings.filterwarnings("ignore")

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

if keys['auto']:
        processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-stage1")
        pipe = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-stage1")
        
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        pipe.to(device)