import scipy.misc
from glob import glob
import numpy as np

class DataLoader():
    def __init__(self, img_res=(128, 128)):
        self.img_res = img_res

    def load_train_batch(self, batch_size=1, is_testing=False):
        path = glob('./datasets/train/*')
        self.n_batches = int(len(path) / batch_size)
        for i in range(self.n_batches):
            batch = path[i*batch_size:(i+1)*batch_size]
            imgs_A, imgs_B = [], []
            for img in batch:
                img = self.imread(img)
                h, w, _ = img.shape
                half_w = int(w/2)
                img_A = img[:, :half_w, :]
                img_B = img[:, half_w:, :]

                img_A = scipy.misc.imresize(img_A, self.img_res)
                img_B = scipy.misc.imresize(img_B, self.img_res)

                if not is_testing and np.random.random() > 0.5:
                        img_A = np.fliplr(img_A)
                        img_B = np.fliplr(img_B)

                imgs_A.append(img_A)
                imgs_B.append(img_B)

            imgs_A = np.array(imgs_A)/127.5 - 1.
            imgs_B = np.array(imgs_B)/127.5 - 1.

            yield imgs_A, imgs_B

    def load_test_batch(self, batch_size):
        path = glob('./datasets/test/*' )
        self.n_batches = int(len(path) / batch_size)
        for i in range(self.n_batches):
            batch = path[i*batch_size:(i+1)*batch_size]
            imgs_A, imgs_B = [], []
            for img in batch:
                img = self.imread(img)
                h, w, _ = img.shape
                half_w = int(w/2)
                img_A = img[:, :half_w, :]
                img_B = img[:, half_w:, :]

                img_A = scipy.misc.imresize(img_A, self.img_res)
                img_B = scipy.misc.imresize(img_B, self.img_res)

                imgs_A.append(img_A)
                imgs_B.append(img_B)

            imgs_A = np.array(imgs_A)/127.5 - 1.
            imgs_B = np.array(imgs_B)/127.5 - 1.

            yield imgs_A, imgs_B

    def load_self_test_batch(self, batch_size):
        path = glob('./self_test/*')
        self.n_batches = int(len(path) / batch_size)
        for i in range(self.n_batches):
            batch = path[i * batch_size:(i + 1) * batch_size]
            imgs_A, imgs_B = [], []
            for img in batch:
                img = self.imread(img)
                h, w, _ = img.shape
                img_A = img[:, :w, :]
                img_A = scipy.misc.imresize(img_A, self.img_res)
                imgs_A.append(img_A)
            imgs_A = np.array(imgs_A) / 127.5 - 1.
            yield imgs_A

    def imread(self, path):
        return scipy.misc.imread(path, mode='RGB').astype(np.float)

