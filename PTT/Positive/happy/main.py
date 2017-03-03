import json, sys
with open(sys.argv[2], 'w', encoding='utf-8') as f:
	for i in json.load(open(sys.argv[1], 'r', encoding='utf-8'))['articles']:
		if i.get('article_title', '')!=None and '[公告]' not in i.get('article_title', '') :
			f.write(i.get('article_title', '').replace('\n', '') + '\n')
			list(map(lambda x:f.write(x + '\n'), i.get('content', '').replace('\n', '').split()))