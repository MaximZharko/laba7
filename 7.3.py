from PIL import Image, ImageFilter


img_1 = Image.open("1.jpeg")
img_2 = Image.open("2.jpeg")
img_3 = Image.open("3.jpeg")
img_4 = Image.open("4.jpeg")
img_5 = Image.open("5.jpeg")

img_1.load()
img_2.load()
img_3.load()
img_4.load()
img_5.load()

sharp_img_1 = img_1.filter(ImageFilter.SHARPEN)
sharp_img_2 = img_2.filter(ImageFilter.SHARPEN)
sharp_img_3 = img_3.filter(ImageFilter.SHARPEN)
sharp_img_4 = img_4.filter(ImageFilter.SHARPEN)
sharp_img_5 = img_5.filter(ImageFilter.SHARPEN)

img_1.close()
img_2.close()
img_3.close()
img_4.close()
img_5.close()

sharp_img_1.save("7.3/sharped_1.jpeg")
sharp_img_2.save("7.3/sharped_2.jpeg")
sharp_img_3.save("7.3/sharped_3.jpeg")
sharp_img_4.save("7.3/sharped_4.jpeg")
sharp_img_5.save("7.3/sharped_5.jpeg")
