import imp
from PIL import Image
import base64
import io
import numpy as np
import ast

img= Image.open('ss.jpg')

img=np.array(img)
img=img.tolist()


img=str(img)
image=ast.literal_eval(img)


img=np.array(image)

print(img)

img=Image.fromarray((img).astype(np.uint8)).show()

