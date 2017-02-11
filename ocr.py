#!/usr/bin/env python

from wand.image import Image as wImage
from PIL import Image as pImage
#import pyocr
import pyocr.builders
import io
import os
import cv2
from matplotlib import pyplot as plt


tess = pyocr.tesseract
lang = 'deu'
if not lang in tess.get_available_languages():
    raise BaseException(
        'Tesseract '+lang+' Sprachpaket nicht gefunden!')

req_image = []
filename = "./data/set1.pdf"
filename_png = "./data/page1.png"

image_pdf = wImage(filename=filename, resolution=300)
image_png = image_pdf.convert('png')


for img in image_png.sequence:
    img_page = wImage(image=img)
    req_image.append(img_page.make_blob('png'))
    img_page.colorspace = 'rgb'
    img_page.strip()
    img_page.save(filename=filename_png)

    break  # only first page of PDF

for img in req_image:
    txt = tess.image_to_string(
        pImage.open(io.BytesIO(img)),
        lang=lang,
        builder=pyocr.builders.TextBuilder()
    )
    """word_boxes = tess.image_to_string(
        pImage.open(io.BytesIO(img)),
        lang=lang,
        builder=pyocr.builders.WordBoxBuilder()
    )"""
    # list of box objects. For each box object:
    #   box.content is the word in the box
    #   box.position is its position on the page (in pixels)
    #
    # Beware that some OCR tools (Tesseract for instance)
    # may return empty boxes

    line_and_word_boxes = tess.image_to_string(
        pImage.open(io.BytesIO(img)),
        lang=lang,
        builder=pyocr.builders.LineBoxBuilder()
        # list of line objects. For each line object:
        #   line.word_boxes is a list of word boxes (the individual words in
        #        the line)
        #   line.content is the whole text of the line
        #   line.position is the position of the whole line on the page
        #       (in pixels)
        #
        # Beware that some OCR tools (Tesseract for instance)
        # may return empty boxes
    )

    # Digits - Only Tesseract (not 'libtesseract' yet !)
    digits = tess.image_to_string(
        pImage.open(io.BytesIO(img)),
        lang=lang,
        builder=pyocr.tesseract.DigitBuilder()
    )
    # digits is a python string

img = cv2.imread(filename_png, cv2.IMREAD_COLOR)

with open('ocr_out.txt', 'w+') as f:
        lines = txt.splitlines()
        f.writelines(lines)


for linebox in line_and_word_boxes:
    cv2.rectangle(img, linebox.position[0], linebox.position[1],
                  (200,0,0), 5)
    for wordbox in linebox.word_boxes:
        cv2.rectangle(img, wordbox.position[0],
                      wordbox.position[1], (0,200,0), 3)

plt.imshow(img)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()



