#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PIL import Image
import pytesseract
import glob


# In[ ]:


texts = []
path = '/example_path/' # type your own path here.

# get image files one by one from a folder. In this example, images with .jpg extensions were used.
# If your images are in another format, change .jpg part appropriately
for file in glob.glob(path+'*.jpg'): 
    image = Image.open(file)    
    config = ("-l eng --oem 1 --psm 6") # configuration of ocr engine. Refer to documentation for details
    text = pytesseract.image_to_string(image, config=config)    
    texts.append(text) # store detected texts

# print results    
for text in texts:
    print('OCR TEXT')
    print('========')
    print(text,'\n')


# In[ ]:




