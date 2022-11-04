# EasyFusion
用于编写达芬奇（davinci）的fusion表达式

https://github.com/tdccj/EasyFusion/tree/master/dist

0.1.6 之前支持线性和二次函数
0.1.6 支持正弦函数

0.2 支持自动缓动（自动生成iif语句）
0.2.2 修复当参数为负数时输出无法被fusion识别的bug
0.2.3 略微重构代码，使用upx压缩打包，体积减半

未来功能：fusion表达式查询表、函数图像显示、更多函数

请不要将程序文件夹放置在程序无法访问到的地方
如nas、网盘等挂载分区上，否则可能不会显示GUI窗口

!!!暂时请绝对不要使用exponential(指数)函数，有可能导致fusion无法启动(重装达芬奇无解，可能是vc库或别的地方出现了问题)