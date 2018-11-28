from PIL import Image
import os

def get_path(path):
    '''返回目录中所有JPG图像的文件名列表'''
    return [f for f in os.listdir(path) if f.endswith('.jpg')]

def convert(read_path, save_path):
    image_file = Image.open(read_path)  # open colour image
    image_file = image_file.convert('L')  # convert image to black and white
    image_file.save(save_path)

def concat():
    UNIT_SIZE = 256
    TARGET_WIDTH = 2 * UNIT_SIZE
    color_path = "/Users/xinyu/Keras-GAN/pix2pix/images"
    color = get_path(color_path)
    BW_path = "/Users/xinyu/Keras-GAN/pix2pix/convert"
    save_path = "/Users/xinyu/Keras-GAN/pix2pix/merge"
    BW = get_path(BW_path)
    for i in range(len(color)):
        imagefile = []
        #for color_name in color:
        #   if color_name == color_path + '/' + str(i):
        imagefile.append(Image.open(color_path+'/'+color[i]))
        #for BW_name in BW:
        #   if BW_name == BW_path + '/' + str(i):
        imagefile.append(Image.open(BW_path+'/'+BW[i]))
        target = Image.new('RGB', (TARGET_WIDTH, UNIT_SIZE))
        left = 0
        right = UNIT_SIZE
        for image in imagefile:
            target.paste(image, (left, 0, right, UNIT_SIZE))
            left += UNIT_SIZE
            right += UNIT_SIZE
            quality_value = 100
            target.save(save_path + '/' + str(i) + '.jpg', quality=quality_value)

if __name__ == '__main__':
    read_path = "/Users/xinyu/Keras-GAN/pix2pix/images/"
    save_path = "/Users/xinyu/Keras-GAN/pix2pix/convert/"
    nameList = get_path(read_path)
    for name in nameList:
        convert(read_path+name, save_path + name)
    concat()
