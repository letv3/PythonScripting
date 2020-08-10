from PIL import Image, ImageFilter


##filters
img = Image.open('./images/SAS012.jpg')

filtered_image = img.filter(ImageFilter.SHARPEN)

#filtered_image = img.convert('L')
upside = filtered_image.rotate(180)
filtered_image.save('images/sharped_old_sas.png', 'png')



#Resizing
big_img = Image.open('images/astro.jpg')
big_img.thumbnail((400, 200))
big_img.save('images/thumbnail_astro.png', 'png')



