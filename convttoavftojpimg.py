from PIL import Image
import pillow_avif

JPGimg = Image.open('ar34' + '.AVIF')
JPGimg.save('ar34' + '.jpg')