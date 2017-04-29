# -*- coding: utf-8 -*-
import json, sys, csv
from gensim import models
import numpy as np
model = models.KeyedVectors.load_word2vec_format('med400.model.bin', binary=True)
ptrain, ntrain, ptest, ntest = json.load(open(sys.argv[1], 'r')), json.load(open(sys.argv[2], 'r')), json.load(open(sys.argv[3], 'r')), json.load(open(sys.argv[4], 'r'))
ptraintxt, ntraintxt, ptesttxt, ntesttxt = open(sys.argv[5], 'r'), open(sys.argv[6], 'r'), open(sys.argv[7], 'r'), open(sys.argv[8], 'r')

ptrainvec = []
for i, k in zip(ptrain, ptraintxt):
	sum = np.zeros(400)
	for j in i:
		try:
			sum = np.add(sum, model[j])
		except Exception as e:
			pass
	ptrainvec.append(['p'] + sum.tolist() + [i] + [k.replace('\n', '')])
# export as csv
with open("ptrain.csv","w") as f:
	w = csv.writer(f)
	w.writerows(ptrainvec)

ntrainvec = []
for i, k in zip(ntrain, ntraintxt):
	sum = np.zeros(400)
	for j in i:
		try:
			sum = np.add(sum, model[j])
		except Exception as e:
			pass
	ntrainvec.append(['p'] + sum.tolist() + [i] + [k.replace('\n', '')])
# export as csv
with open("ntrain.csv","w") as f:
	w = csv.writer(f)
	w.writerows(ntrainvec)

ptestvec = []
for i, k in zip(ptest, ptesttxt):
	sum = np.zeros(400)
	for j in i:
		try:
			sum = np.add(sum, model[j])
		except Exception as e:
			pass
	ptestvec.append(['p'] + sum.tolist() + [i] + [k.replace('\n', '')])
# export as csv
with open("ptest.csv","w") as f:
	w = csv.writer(f)
	w.writerows(ptestvec)
# export as json

ntestvec = []
for i, k in zip(ntest, ntesttxt):
	sum = np.zeros(400)
	for j in i:
		try:
			sum = np.add(sum, model[j])
		except Exception as e:
			pass
	ntestvec.append(['p'] + sum.tolist() + [i] + [k.replace('\n', '')])
# export as csv
with open("ntest.csv","w") as f:
	w = csv.writer(f)
	w.writerows(ntestvec)