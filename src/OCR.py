import keyboard
import os

from PIL import Image

from __init__ import processor, pipe, device, keys


def OCR(img):
    img = Image.open(img).convert("RGB")

    pixel_values = processor(images=img, return_tensors="pt").pixel_values.to(device)

    generated_ids = pipe.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return generated_text

def resize(imgs, x1, y1, x2, y2):
    size = (600, 600)
    
    img = Image.open(imgs)

    img.thumbnail(size, Image.Resampling.LANCZOS)

    x1, y1 = x1, img.height - y1
    x2, y2 = x2, img.height - y2

    img = img.crop((x1, y1, x2, y2))

    img.save('./sanity.png')

def OCR_sanity():
    keyboard.press('ctrl+shift+s')
    
    imgs = f"{keys['dirs']}/{os.listdir(keys['dirs'])[-1]}"
    
    resize(imgs, x1=520, y1=325, x2=552, y2=300)

    text = OCR('./sanity.png')

    number = int(text.split('/')[0])

    resize(imgs, x1=550, y1=16, x2=580, y2=4)

    text = OCR('./sanity.png')
    
    number_2 = int(text)
    
    os.remove(imgs)

    return number, number_2