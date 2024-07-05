def isLandscape(image_width,image_height):
    if image_width > image_height:
        print('Landscape')
    else:
        print('Portrait')

image_width = int(input('Enter the width of the image: '))
image_height = int(input('Enter the height of the image: '))
isLandscape(image_width,image_height)
