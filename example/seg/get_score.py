#encoding=gbk

from sklearn.metrics import f1_score,accuracy_score
import sys

file_path = sys.argv[1]

with open(file_path, 'r') as fin:
	y_true, y_pre = [],[]
	tag2id = {'O':0,'B':1,'M':2,'E':3}
	for line in fin:
		if line != '\n':
			word, true, pre = line.strip('\n').split('\t')
			y_true.append(tag2id[true])
			y_pre.append(tag2id[pre])
	score = f1_score(y_true, y_pre, [0,1,2,3], average=None)
	print(score)
	print('avg_f1_score',sum(score)/len(score))
	print('accuracy',accuracy_score(y_true, y_pre))
	print(f1_score(y_true, y_pre, [0,1,2,3],average='macro'))
