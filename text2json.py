import pyspark
import jieba, json, sys, os
import jieba.posseg as pseg
conf = pyspark.SparkConf().setAll([('spark.driver.memory', '30g'), ('spark.driver.host', '172.17.0.21'), ('spark.app.id', 'local-1492693477461'), ('spark.rdd.compress', 'True'), ('spark.serializer.objectStreamReset', '100'), ('spark.master', 'local[*]'), ('spark.executor.id', 'driver'), ('spark.submit.deployMode', 'client'), ('spark.driver.port', '39274'), ('spark.app.name', 'PySparkShell')])
sc = pyspark.SparkContext(conf=conf)
stopwords = json.load(open('stopwords.json', 'r'))
jieba.load_userdict(os.path.join('dictionary', 'dict.txt.big.txt'))
jieba.load_userdict(os.path.join("dictionary", "NameDict_Ch_v2"))

def removeStopWords(sentence):
	def condition(x):
		x = list(x)
		word, flag = x[0], x[1]
		if len(word) > 1 and flag!='eng' and flag != 'm' and flag !='mq' and word not in stopwords:
			return True
		return False

	result = filter(condition, pseg.cut(sentence))
	result = map(lambda x:list(x)[0], result)
	return list(result)
# with open(sys.argv[1], 'r') as f:
# 	result = list(map(removeStopWords, f))
# 	ff = open('p.json', 'w')
# 	json.dump(result, ff)
# 	ff.close()

t = sc.textFile(sys.argv[1])
result = t.map(removeStopWords).collect()
ff = open(sys.argv[2], 'w')
json.dump(result, ff)
ff.close()