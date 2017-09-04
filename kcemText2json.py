import jieba, json, sys, os
import jieba.posseg as pseg
stopwords = json.load(open('stopwords.json', 'r'))
jieba.load_userdict(os.path.join('dictionary', 'dict.txt.big.txt'))
jieba.load_userdict(os.path.join("dictionary", "NameDict_Ch_v2"))

def removeStopWords(sentence, rmstop=sys.argv[3]):
	def condition(x):
		x = list(x)
		word, flag = x[0], x[1]
		if len(word) > 1 and flag!='eng' and flag != 'm' and flag !='mq' and word not in stopwords:
			return True
		return False

	sentence, label = sentence.rsplit(' ', 1)
	if rmstop == 'True':
		result = filter(condition, pseg.cut(sentence))
		result = list(map(lambda x:list(x)[0], result))
	else:
		result = jieba.lcut(sentence)
		label = jieba.lcut(label.replace('\n', '').strip())
	return {'data':result, 'label':label}

with open(sys.argv[1], 'r') as f:
	result = list(map(removeStopWords, f))

with open(sys.argv[2], 'w') as f:
	json.dump(result, f)