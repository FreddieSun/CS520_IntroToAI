## 模型训练部分
* datasets 训练集 测试集 
* saved_model 保存模型

## 模型测试部分
* images 训练每一个epoch后的测试结果 文件夹数字代表epoch数
  1. myset 对比图 （用原彩图+生成图+灰度图 进行对比）
  2. fake 生成图  （单独把测试过程中生成给的图片拿出来，为concat做猪呢比）
  3. concat 拼接图（将训练每一个epoch后的同一个测试图片拼接起来，显示训练过程过程）
* test 自测试的测试集（要用saved_model下已经训练好的model进行测试，前提是已经裁剪好尺寸并完成图片拼接）
* result 自测试结果（用saved_model下已经训练好的model进行测试的结果）

* test1 TA自测图 前提：灰度图/彩图（无尺寸要求）
* result1 TA测试结果 只有生成图
## 图片预处理部分
* orig 原彩图（未经裁剪的图片，google批量下载的）
* images1 裁剪尺寸后的彩图（256 X 256) 
* convert 裁剪好的彩图转化为的灰度图 
* merge 裁剪好的彩图和灰度图的拼接图(彩图+灰度图)

## 其他
* resources 两篇pdf
