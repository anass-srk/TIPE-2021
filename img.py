from PIL import Image
import numpy as np

w, h = 200, 200

with open('data.bin', mode='rb') as f:
  d = np.fromfile(f,dtype=np.uint8,count=w*h).reshape((h,w))
  PILimage = Image.fromarray(d)
  PILimage.save('result.png',"PNG")
