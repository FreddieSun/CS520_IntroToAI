## codes
1. convet.py 数据集预处理，以及测试结果整理
2. data_loader.py 训练测试模型load数据
3. Gan.py 训练测试

## 模型训练部分
1. datasets 
   1. test 测试集
   2. train 训练集
2. saved_model 训练后保存的模型

## 模型测试部分
1. test_result 训练每一个epoch后的测试结果 文件夹数字代表epoch数
   1. contrast 对比图 （用原彩图+生成图+灰度图 进行对比）
   2. fake 生成图  （单独把测试过程中生成给的图片拿出来，为concat做准备）
   3. concat_fake 拼接图（将训练每一个epoch后的同一个测试图片拼接起来，显示训练过程过程）
2. selt_test TA自测图 灰度图/彩图（无尺寸要求）
3. self_result TA测试结果 只有生成图

## 图片预处理部分
1. data_preprocessing
   1. orig 原彩图（未经裁剪的图片，google批量下载的）
   2. images1 裁剪尺寸后的彩图（256 X 256) 
   3. convert 裁剪好的彩图转化为的灰度图 
   4. merge 裁剪好的彩图和灰度图的拼接图(彩图+灰度图)

## 其他
1. resources 两篇pdf

