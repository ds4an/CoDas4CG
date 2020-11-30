1、
ComputeBLEU.py：contains ComputeBLEU和ComputeBLEU2
2、
preprocess.py：contains PreProcessALL、PreProcessReq、PreProcessImp

3、
CompilerErrors.py

The following script must be run first (put the py file of the generated code in the same directory as the script, and no py file other than the generated code must be placed)
detect.sh :Static grammar checking
(Before using dynamic detection, put the input use case and output use case files corresponding to the id under the pre folder)
run.sh:Run compilation check dynamically

Use the command:
. detect.sh >resultE.txt
. run.sh 2>resultR.txt