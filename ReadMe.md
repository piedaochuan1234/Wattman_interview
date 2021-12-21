#题目1：

1. 将json文件里面的name为"box_b"的“rectangle”字段打印出来。
2. 写一个小工具，可以将任意一张图像填充到另一张图像的box_b所指定的区域中，并需要通过传参来支持“拉伸填充”和“保持原比例填充”两种模式。 
3. 将完成后的代码上传到github中（可以上传到其它git仓库）。



### 通过`opencv`实现填充图片功能，使用时需要设置`fill_img.py`中的填充图片路径的如下参数：

- imgFill_path    填充图片的路径；
- imgTarget_path  填充目标图片的路径；
- js_path         包含填充目标图片路径`label`信息的`json`文件路径；
- resize_mode     填充图片时是否保留填充图片的形状；
然后终端运行：
```commandline
python fill_img.py
```


其中在`resize`填充图片时对于缩小和放大两种情况，分别采用`INTER_AREA`和`INTER_LINEAR`插值方法。


#题目2：


要求：
1. 写一个linux shell脚本统计指定目录下文件名满足' *_gt.json*'要求的文件数量，需要注意的是指定目录下的文件夹层数可能不一定。
2. 将完成后的代码上传到github中（可以上传到其它git仓库）。

### 终端运行`get_file_num.sh`脚本:
```commandline
sh get_file_num.sh
```
即可打印出文件数量。