from PIL import Image
import os

def get_path(path):
    '''返回目录中所有JPG图像的文件名列表'''
    return [f for f in os.listdir(path) if f.endswith('.jpg')]

def convert(read_path, save_path):
    image_file = Image.open(read_path)  # open colour image
    image_file = image_file.convert('L')  # convert image to black and white
    image_file.save(save_path)
def reshape():
    path = "/Users/xinyu/Keras-GAN/pix2pix/orig/"
    save_path = "/Users/xinyu/Keras-GAN/pix2pix/images1/"
    list = get_path(path)
    for name in list:
        if name == '15.jpg':
            continue
        im = Image.open(path + name)
        out = im.resize((256, 256))
        out.save(save_path + name)
def concat():
    UNIT_SIZE = 256
    TARGET_WIDTH = 2 * UNIT_SIZE
    color_path = "/Users/xinyu/Keras-GAN/pix2pix/images1"
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
def getfilename(filename):
    for root, dirs, files in os.walk(filename):
        array = dirs
        if array:
            return array

def concat1():
    save_path ='/Users/xinyu/Keras-GAN/pix2pix/images/concat/'
    path = '/Users/xinyu/Keras-GAN/pix2pix/images/fake/'
    dir1 = getfilename(path)#'0,1,2'
    fake = get_path(path+dir1[0])#0.png 1.png
    UNIT_SIZE = 256
    TARGET_WIDTH = len(dir1) * UNIT_SIZE
    for i in range(len(fake)):
        image = []
        for dirs in dir1:
            picture_name_list = get_path(path+dirs)
            for picture_name in picture_name_list:
                if picture_name == fake[i]:
                    image.append(Image.open(path+dirs+'/'+picture_name))
        target = Image.new('RGB', (TARGET_WIDTH, UNIT_SIZE))
        left = 0
        right = UNIT_SIZE
        for image in image:
            target.paste(image, (left, 0, right, UNIT_SIZE))
            left += UNIT_SIZE
            right += UNIT_SIZE
            quality_value = 100
            target.save(save_path + str(i) + '.png', quality=quality_value)


if __name__ == '__main__':
    #reshape()
    #read_path = "/Users/xinyu/Keras-GAN/pix2pix/images1/"
    #save_path = "/Users/xinyu/Keras-GAN/pix2pix/convert/"
    #nameList = get_path(read_path)
    #for name in nameList:
    #    convert(read_path+name, save_path + name)


    #concat()
    concat1()
