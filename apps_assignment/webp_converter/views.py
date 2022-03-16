from io import BytesIO
from tkinter.tix import IMAGE
from django.shortcuts import render
from PIL import Image
import os
import base64


# Create your views here.
def get_converter_page(response):
    return render(response,"webp_converter/converter.html", {})


def convert_image(response):
    if response.method=="POST":

        picture = response.FILES ['image']
        img = Image.open(picture)
        img.convert("RGB")
        
        with BytesIO() as f:
            img.save(f, format="webp")
            
            context = {
                'img_str': base64.b64encode(f.getvalue()).decode('utf-8'),
            }

    return render(response,"webp_converter/converter.html", context=context)