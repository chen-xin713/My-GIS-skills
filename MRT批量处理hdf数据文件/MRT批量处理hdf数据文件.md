**MRT批量处理hdf数据文件**

1、安装jdk以及MRT

2、进入MRT安装目录，在bin文件夹下双击“ModisTool.jar"
![](assets/MRT批量处理hdf数据文件/file-20251211120139029.png)

打开界面如下：
![](assets/MRT批量处理hdf数据文件/file-20251211120234069.png)

3、点击"Open lnput File..."按键按钮导入待处理的.hdf文件
![](assets/MRT批量处理hdf数据文件/file-20251211120248262.png)

4、将不想要输出的波段选择并点击"<<"按钮移动至左边
![](assets/MRT批量处理hdf数据文件/file-20251211120302851.png)

5、点击'Specify Output File...'按钮选择输出的文件类型与路径，在'Resampling Type'中选择重采样类型
![](assets/MRT批量处理hdf数据文件/file-20251211120317357.png)

6、点击'Out普通 Projection Type'选择输出图像的投影类型
![](assets/MRT批量处理hdf数据文件/file-20251211120340279.png)

7、点击'Edit Projection ParaMeters...'按钮修改投影参数
![](assets/MRT批量处理hdf数据文件/file-20251211120353880.png)

8、在左下角输入裁剪的范围
![](assets/MRT批量处理hdf数据文件/file-20251211120406859.png)
![](assets/MRT批量处理hdf数据文件/file-20251211120434024.png)

9、点击'Save Parameter File'按钮将prm文件进行保存
![](assets/MRT批量处理hdf数据文件/file-20251211120448886.png)

10、点击"Run"按钮既可以对单张进行波段提取 

11、在MRT目录下bin文件夹中唤出cmd命令行窗口
![](assets/MRT批量处理hdf数据文件/file-20251211120508320.png)
12、输入"java -jar MRTBatch.jar -d E:\GF\Desktop\测试 -p E:\GF\Desktop\测试\1.prm -o E:\GF\Desktop\测试\output1"命令
![](assets/MRT批量处理hdf数据文件/file-20251211120531575.png)
    其中：

        -d后面是待批处理数据所在文件夹

        -p后面是先前生成的.prm文件所的位置

        -o后面是待批量输出数据所在文件夹

    点击回车运行再输入：MRTBatch.bat 即可开始批处理
![](assets/MRT批量处理hdf数据文件/file-20251211120547894.png)

13、在输出文件夹即可找到批量提取并裁剪后的波段图像
![](assets/MRT批量处理hdf数据文件/file-20251211120559110.png)


14、利用python代码进行批量波段合成并输出
![](assets/MRT批量处理hdf数据文件/file-20251211120608427.png)

