from PIL import Image


with Image.open("owl.jpeg") as img:
    img.show()
    print("Размер изображения: " + str(img.size[0]) + "x" + str(img.size[1]))
    print("Формат изображения: " + img.format)
    print("Цветовая модель: " + img.mode)
