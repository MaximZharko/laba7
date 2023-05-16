from PIL import Image


print("Введите количество изображений:")
num = int(input())

watermark = Image.open("watermark.jpeg")
watermark.load()
watermark = watermark.reduce(5)

for i in range(num):
    print("Введите название изображения:")
    filename = input()
    with Image.open(filename) as img:
        img.load()
        img.paste(watermark, (img.width // 2, img.height // 2))
        new_filename = "new_" + filename
        img.save(new_filename)