## CS 520 Final Project
#### By Weijia Sun, Yi Wu , Xun Tang, Xinyu Lyu 

### Environment :  
Python 3.6  
Extra Library : 
1. Keras 2.2.4
2. Tensorflow 1.11.0
3. Pillow 5.2.0

### How to test the colorization?
1. First you need to install all the extra libraries. 
2. Before run the Gan.py to test the result, you need to put the grayscale images with JPG format in ./self_test folder.
3. You can use the grayscale image provided by ourselves in ./dataset_preprocessing/original folder, or you can use your own test dataset.
4. Then run the Gan.py following the instructions on the console.
5. Finally, you can get the test results in the in the ./self_result folder.

### What is the role od each codes file?
1. Gan.py : Include the model training part and the testing part.
2. data_loader.py : Provide data for model training and testing.
3. convert.py : Some prepossessing operations for the dataset.
What does each folder include in our project?
1. dataset_preproccessing :
    1. original : original colourful image with JPG format without prepossessing.
    2. grayscale : grayscale image converted from the colourful image in original folder.
    3. cropped : crop grayscale images from grayscale folder into 256*256 size.
    4. concat : 512*256 image concatenated by 256*256 colorful image together its corresponding 256*256 grayscale image
2. datasets: divide the images in concat folder into train and test with the scale as 4:1.
    1. test : test dataset used in cross validation. 
    2. train : train dataset used in model training.
3. saved_model: the saved colorization model by 50 epoch training on the training datset. If you want to test our model by yourself, this is the model you are using to test. 
4. test_result : we test the model with the test dataset in the end of each epoch. And we output the test result in such three kinds which is intuitive to show the test result.
    1. fake : Images in each folder stand for the images colorized from the test dataset in each training epoch. 
    2. contrast : We concat the grayscale(BW), generated, original image together from the test at the end of each training epoch.
    3. concat_fake : We concatenate the test result from 50 epochs to see the gradual process of model tranining.
5. Final_test_result: Show some colorization results against the real colorful images.