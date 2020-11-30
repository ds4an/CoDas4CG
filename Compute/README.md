1、
ComputeBLEU.py：包含ComputeBLEU和ComputeBLEU2两个函数
2、
preprocess.py：包含PreProcessALL、PreProcessReq、PreProcessImp三个函数

3、
CompilerErrors.py

必须先运行以下脚本（将生成代码的py文件放与脚本同目录，不得置放除生成代码以外的py文件）
detect.sh :静态语法检测
(使用动态检测之前将对应id的输入用例和输出用例文件放于pre文件夹下)
run.sh:动态运行编译检测
使用命令：
. detect.sh >resultE.txt
. run.sh 2>resultR.txt