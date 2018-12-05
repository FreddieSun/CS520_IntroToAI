from PIL import Image
import os

'''
return jpg name
'''
def get_path(path):
    return [f for f in os.listdir(path) if f.endswith('.jpg')]

'''
return dir name 
'''
def get_dir(filename):
    for root, dirs, files in os.walk(filename):
        array = dirs
        if array:
            return array

'''
convert color jpg to gray jpg
'''
def convert(path, save_path):
    list = get_path(path)
    for name in list:
        image_file = Image.open(path + name)
        image_file = image_file.convert('L')
        image_file.save(save_path + name)

'''
reshape color jpg to 256*256
'''
def reshape(path, save_path):
    list = get_path(path)
    for name in list:
        image_file = Image.open(path + name)
        image_file = image_file.resize((256, 256))
        image_file.save(save_path + name)

'''
concat color jpg and gray jpg
'''
def concat(color_path, BW_path, save_path):
    UNIT_SIZE = 256
    TARGET_WIDTH = 2 * UNIT_SIZE
    color = get_path(color_path)
    BW = get_path(BW_path)
    for i in range(len(color)):
        imagefile = [Image.open(color_path + color[i]), Image.open(BW_path + BW[i])]
        target = Image.new('RGB', (TARGET_WIDTH, UNIT_SIZE))
        left = 0
        right = UNIT_SIZE
        for image in imagefile:
            target.paste(image, (left, 0, right, UNIT_SIZE))
            left += UNIT_SIZE
            right += UNIT_SIZE
            quality_value = 100
            target.save(save_path + str(i) + '.jpg', quality=quality_value)

'''
concat jpg in test_result/fake/
'''
def concat_n(path, save_path):
    dir1 = get_dir(path)
    dir_int = [int(i) for i in dir1]
    dir_int.sort()
    dir1 = [str(i) for i in dir_int]
    fake = get_path(path + dir1[0])
    UNIT_SIZE = 256
    TARGET_WIDTH = len(dir1) * UNIT_SIZE
    for i in range(len(fake)):
        image = []
        for dirs in dir1:
            picture_name_list = get_path(path + dirs)
            for picture_name in picture_name_list:
                if picture_name == fake[i]:
                    image.append(Image.open(path + dirs + '/' + picture_name))
                    break
        target = Image.new('RGB', (TARGET_WIDTH, UNIT_SIZE))
        left = 0
        right = UNIT_SIZE
        for image in image:
            target.paste(image, (left, 0, right, UNIT_SIZE))
            left += UNIT_SIZE
            right += UNIT_SIZE
            quality_value = 100
            target.save(save_path + str(i) + '.png', quality=quality_value)
        print(str(i) + 'finish')


if __name__ == '__main__':
    path = ''
    save_path = ''
    BW_path = ''
    color_path = ''

    reshape(path, save_path)
    convert(path, save_path)
    concat(color_path, BW_path, save_path)
    concat_n(path, save_path)
