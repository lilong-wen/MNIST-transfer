# %%
import PIL
import os
import random
import os
# %%

# %%
ROOT_DIR = 'D://projects//MNIST-JPG//output//'
IMAGE_SAVE_PATH = 'D://projects//MNIST-JPG//data//'
train_or_test = ['training', 'testing']
# class_name = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
IMAGE_COLUMN = 6
IMAGE_ROW = 6

# %%

# %%

# TODO
def get_size(path):
    print(path)
    img = PIL.Image.open(path)
    return img.size[0], img.size[1]

# %%

# %%

# %%
def image_concate(is_Train, num):
    
    if is_Train == True:
        file_path = ROOT_DIR + train_or_test[0]
    else:
        file_path = ROOT_DIR + train_or_test[1]
    
    class_name = os.listdir(file_path)[2:]

# TODO
    sample_path = file_path + '//1//3.jpg'

    IMAGE_SIZE, _ = get_size(sample_path)
    for item in range(num):
        to_image = PIL.Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE))
        
        file_name = ''
        for y in range(1, IMAGE_ROW + 1):
            for x in range(1, IMAGE_COLUMN + 1):
                
                class_random = random.randint(0, 9)
                file_name = file_name + (str(class_random))
                tmp_path = file_path + '//' + str(class_random)
                full_path = random.sample(os.listdir(tmp_path), 1)[0]
                print(tmp_path + '//' + full_path)
                from_image = PIL.Image.open(tmp_path + '//' + full_path)
                to_image.paste(from_image, ((x-1) * IMAGE_SIZE, (y-1) * IMAGE_SIZE))
        
        print(IMAGE_SAVE_PATH + file_name + '.jpg')
        to_image.save(IMAGE_SAVE_PATH + file_name + '.jpg')
        
# %%
image_concate(True, 1000)

# %%
