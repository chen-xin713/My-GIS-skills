**MRT批量处理hdf数据文件**

1、安装jdk以及MRT

2、进入MRT安装目录，bin文件夹下双击“ModisTool.jar"文件，打开界面如下：

<img src="https://mmbiz.qpic.cn/mmbiz_png/s10FkKtzXayg3Wopb0cU1vELQvwkeiaaA47BWCunicqJZxt2pstmTMG7X6ic0xG3HVjHFwFk2icK1fKMCTsUjtAUqw/640?wx_fmt=png" title="" alt="" width="319">

3、点击![](C:\Users\GF\AppData\Roaming\marktext\images\2025-05-04-11-32-46-image.png)按键按钮导入待处理的.hdf文件

<img src="file:///C:/Users/GF/AppData/Roaming/marktext/images/2025-05-04-11-32-19-image.png" title="" alt="" width="405">

4、选择要保留的波段

<img src="file:///C:/Users/GF/AppData/Roaming/marktext/images/2025-05-04-11-34-59-image.png" title="" alt="" width="297">

5、选择输出的文件名与路径

![](C:\Users\GF\AppData\Roaming\marktext\images\2025-05-04-11-37-38-image.png)

6、选择输出图像的投影类型

![](C:\Users\GF\AppData\Roaming\marktext\images\2025-05-04-11-38-37-image.png)

7、点击![](C:\Users\GF\AppData\Roaming\marktext\images\2025-05-04-11-39-13-image.png)按钮进行选择投影

<img src="file:///C:/Users/GF/AppData/Roaming/marktext/images/2025-05-04-11-40-29-image.png" title="" alt="" width="301">

8、在左下角输入裁剪的范围

<img src="file:///C:/Users/GF/AppData/Roaming/marktext/images/2025-05-04-11-41-39-image.png" title="" alt="" width="300">

<img src="file:///C:/Users/GF/AppData/Roaming/marktext/images/2025-05-04-11-46-34-image.png" title="" alt="" width="304">

9、点击![](C:\Users\GF\AppData\Roaming\marktext\images\2025-05-04-11-46-01-image.png)按钮将prm文件进行保存

<img src="file:///C:/Users/GF/AppData/Roaming/marktext/images/2025-05-04-11-45-39-image.png" title="" alt="" width="312">

10、点击"Run"按钮既可以对单张进行波段提取

11、在MRT目录下bin文件夹中唤出cmd命令行窗口

<img src="file:///C:/Users/GF/AppData/Roaming/marktext/images/2025-05-04-11-54-20-image.png" title="" alt="" width="354">

12、输入"java -jar MRTBatch.jar -d E:\GF\Desktop\测试 -p E:\GF\Desktop\测试\1.prm -o E:\GF\Desktop\测试\output1"命令

<img src="file:///C:/Users/GF/AppData/Roaming/marktext/images/2025-05-04-11-52-15-image.png" title="" alt="" width="366">

    其中：

        -d后面是待批处理数据所在文件夹

        -p后面是先前生成的.prm文件所的位置

        -o后面是待批量输出数据所在文件夹

    点击回车运行再输入：MRTBatch.bat 即可开始批处理

<img src="file:///C:/Users/GF/AppData/Roaming/marktext/images/2025-05-04-11-56-13-image.png" title="" alt="" width="358">

13、在输出文件夹即可找到批量提取并裁剪后的波段图像

<img src="file:///C:/Users/GF/AppData/Roaming/marktext/images/2025-05-04-11-57-21-image.png" title="" alt="" width="363">

14、利用python代码进行批量波段合成并输出

![](C:\Users\GF\AppData\Roaming\marktext\images\2025-05-04-12-01-25-image.png)
