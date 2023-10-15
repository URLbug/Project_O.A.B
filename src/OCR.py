from PIL import Image

from __init__ import processor, pipe, device


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

def OCR_sanity(imgs):

    resize(imgs, x1=517, y1=333, x2=560, y2=300)

    text = OCR('./sanity.png')

    print(text)

    number = int(text.split('/')[0])

    resize(imgs, x1=536, y1=15, x2=561, y2=3)

    text = OCR('./sanity.png')

    number_2 = int(text)

    return number, number_2