import re
import os
import requests
import fileinput
from PIL import Image
from io import BytesIO

# Open EML file and retrieve HTML content
eml_contents = open("test.eml", "r").read()
html_string = re.search(r'^(<!DOCTYPE.*</html>[,\s])', eml_contents, re.MULTILINE | re.DOTALL)

# Writing HTML content to a file
f1 = open("test.html", "w")
f1.write(html_string.group(0))
f1.close()

f2 = open("test.html", "r")
m = f2.read()

links = []

# All img src links will be appended to this list
links = re.findall("src=[\"\'](.*?)[\"\']", m)
os.mkdir("images")

for i in range(len(links)):
    image_url = links[i]
    img_name = image_url.split("/")[-1]

    # To successfully return the stream content set stream to True
    r = requests.get(image_url, stream=True)
    img = Image.open(BytesIO(r.content))
    
    # Set PNG as an extension if image mode is 1 else set it as JPG
    if img.mode in ("RGBA", "P"):
        path = (f'./images/{i}.png')
    else:
        path = (f'./images/{i}.jpg')
        
    img.save(path)
    
    # Replacing img links with the path of images
    with fileinput.FileInput("test.html", inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(image_url, path), end='') 