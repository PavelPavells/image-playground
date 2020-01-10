from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.convert('L')
filtered_img.save('blur.png', 'png')
crooked = filtered_img.rotate(180)
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
#resize = filtered_img.resize(100, 100)
region.save('grey.png', 'png')
#filtered_img.show()
print(img)

img2 = Image.open('./astro.jpg')
new_img = img2.resize((400, 400))
new_img.save('thumbnail.jpg')
print(img2.size)