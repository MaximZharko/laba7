from PIL import Image


with Image.open("owl.jpeg") as img:
    resized_img = img.reduce(3)
    resized_img.save("resized_owl.jpeg")
    inverted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    inverted_img.save("inverted_owl.jpeg")
    mirrored_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    mirrored_img.save("mirrored_owl.jpeg")
    