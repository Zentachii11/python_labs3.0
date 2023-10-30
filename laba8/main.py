from PIL import Image

def Transpose_img(img_path, img_name, new_img_name):
    img = Image.open(img_path + '\\' + img_name)
    img_transpose = img.transpose(Image.FLIP_LEFT_RIGHT)
    img_transpose.save(img_path + '\\' + new_img_name)

img_path = r"C:\Users\kalin\Desktop\images"
img_name = 'volt.jpg'
new_img_name = 'volt2.jpg'
Transpose_img(img_path, img_name, new_img_name)
