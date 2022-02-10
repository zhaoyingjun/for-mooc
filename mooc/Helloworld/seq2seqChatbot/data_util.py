# coding=utf-8
import os
import re
import jieba
from zhon.hanzi import punctuation
from config import getConfig

gConfig = {}
gConfig= getConfig.get_config()
conv_path = gConfig['resource_data']
if not os.path.exists(conv_path):
	print("找不到需要处理的文件，请确认在train_data文件中是否存在该文件")
	exit()
convs = []
with open(conv_path,encoding='utf-8') as f:
	one_conv = "" # 存储一次完整对话
	for line in f:
		line = line.strip('\n')
		line=re.sub(r"[%s]+" %punctuation, "",line)#去除标点符号
		if line == '':
			continue
		if line[0] == gConfig['e']:
			if one_conv:

				convs.append(one_conv[:-1])
			one_conv = ""
		elif line[0] == gConfig['m']:
			one_conv=one_conv+str(" ".join(jieba.cut(line.split(' ')[1])))+'\t'#存储一次问或答


seq_train = open(gConfig['seq_data'],'w')
for i in range(len(convs)):
   seq_train.write(convs[i]+'\n')
   if i % 1000 == 0:
      print(len(range(len(convs))), '处理进度：', i)
seq_train.close()



