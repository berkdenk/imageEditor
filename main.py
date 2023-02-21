from PIL import Image

Image.open("nature.jpg").show() #open file and show

fg=Image.open("nature.jpg")
#Information
print(fg.format)
print(fg.filename)
print(fg.mode)
print(fg.size)

#function rotate and save
fg.rotate(90).save("rotate.jpg")#rotate 90 degree and save

Image.open("rotate.jpg").show()

fg.transpose(Image.FLIP_LEFT_RIGHT).save("transpose.jpg")#transpoze

Image.open("transpose.jpg").show()

#resize

fg.thumbnail((200,200))
fg.save("thumbnail.jpg")
Image.open("thumbnail.jpg")

r,g,b=fg.split()
fg=Image.merge("RGB",(b,g,r))
fg.save("merged.jpg")
fg.show()

#crop
range=(400,500,1000,1400)
fg.crop(range).save("crop.jpg")
Image.open("crop.jpg").show()

