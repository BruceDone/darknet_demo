# darknet
<img src="https://camo.githubusercontent.com/e69d4118b20a42de4e23b9549f9a6ec6dbbb0814/687474703a2f2f706a7265646469652e636f6d2f6d656469612f66696c65732f6461726b6e65742d626c61636b2d736d616c6c2e706e67" alt="Darknet Logo" data-canonical-src="http://pjreddie.com/media/files/darknet-black-small.png" style="max-width:100%;">

#### 项目介绍
refer from the https://github.com/pjreddie/darknet, use the yolov3-tiny.cfg prototxt to train own captche detector
本项目使用https://github.com/pjreddie/darknet, 基于darknet yolov3-tiny.cfg

#### 软件架构
基于深度学习框架darknet，使用darknet训练的模型，自由切换cpu模型或者gpu模式处理代码


#### 文件夹说明
* cfg  - 模型定义文件所在，类似网络的结构定义
    * deploy.cfg - 部署的模型定义文件
    * train.cfg  - 训练的模型网络定义文件
    * yolov3-tiny.cfg - 原始小网络定义文件
    * yolov3.cfg - 大网络文件
* data - 训练配置，实际训练数据所有
    * char.names - 分类列表文件
    * train.data - 训练的配置文件，包含各种选项
    * train.txt  - 实际训练数据,整体数据的80%
    * val.txt    - 验证数据集,一般整体数据的20%
* imgs - 训练图片所在
    * 1.jpg - 图片实际地址
    * 1.txt - 图片标的框
        * 0 0.2984375 0.553125 0.115625 0.24375000000000002 - 类别 x,y ,w ,h
* label - xml 文件，标的那些框所在
* session - 训练保存的文件夹所在
* weights - 迁移学习的原始框架所在，原始的训练的权重文件
* config.py - data.py的配置文件
* data.py - 输入 image , label 文件夹，输出train.txt 训练文件

#### 使用说明
1. 准备原始的验证码数据图片文件
2. 下载 https://github.com/tzutalin/labelImg 标注工具，生成到本地的label文件夹下，图片文件要与标注的xml文件一致
3. 使用`data.py` 生成训练文件
4. 进入`weights`文件夹，`sh darknet53.sh `下载好预训练的权重文件
5. 使用`train.sh` 开始训练

