API:

实现平台	API及其功能	
数据库
（sql文件夹）	RetrieveTasks(): 返回所有task的描述（需求），每个需求是一个文本字符串	
	RetrieveTask（ID）: 返回指定ID的task描述	
	RetreiveImplementations（）：返回所有的代码，每个代码对应一个java文件。	
	RetreiveImplementations（ID）：返回指定题目id所有对应的所有代码，每个代码对应一个python文件。	
	RetreiveTestCasess（ID）：返回指定题目id对应的的测试用例。	
编程语言
(compute文件夹)	ComputeBLEU（pred, refer）:计算生成代码pred和参考代码refer之间的BLEU	
	ComputeBLEU2（pred,refers）:依照一系列refers计算生成代码pred的BLEU	
	hasCompilerErrors（File name）:检测代码是否存在静态检测和动态编译错误	
	PreProcessALL(File requirements， File implements): 对相关的需求和代码进行预处理后返回	
	PreProcessReq(File requirements， File implements): 对相关的需求进行预处理后返回	
	PreProcessImp(File requirements， File implements): 对相关代码进行预处理后返回	

