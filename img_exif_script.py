try:
    from PIL import Image, ExifTags
except Exception:
    print('pillow library not founded')
    inp = input('do you want to install it? Y or N: ')
    if inp == "Y" or install == "y":
          os.system('pip install pillow')
          from PIL import Image, ExifTags
    else:
        quit()


print("enter directory of the pic you want to get exif data from\nfor example: /Users/User/Desktop/pic.jpg\n")
pic_location = input('enter the directory of the pic: ')
img = Image.open(f'{pic_location}')
img_exif = img.getexif()


for key, val in img_exif.items():
    if key in ExifTags.TAGS:
        print(f'{ExifTags.TAGS[key]} : {val}')

