import jieba, json, sys

with open(sys.argv[1], 'r') as f:
	result = [jieba.lcut(i) for i in f]
	ff = open('p.json', 'w')
	json.dump(result, ff)
	ff.close()
with open(sys.argv[2], 'r') as f:
	result = [jieba.lcut(i) for i in f]
	ff = open('n.json', 'w')
	json.dump(result, ff)
	ff.close()