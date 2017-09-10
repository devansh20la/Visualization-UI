import csv
import numpy as np 
import torch
from torch.autograd import Variable


A = np.load('submission.npy').item()

submission = np.zeros((3321,1),dtype=float)
scores = np.zeros((3321,3),dtype=float)
path = []

for i in range(0,len(A)):
	_,_,label,score,p = A[i]
	if i == len(A)-1:
		submission[50*i:,0] = label.numpy()
		scores[50*i:,:] = score.data.numpy()
	else:
		submission[50*i:50*i+50,0] = label.numpy()
		scores[50*i:50*i+50,:] = score.data.numpy()
	for pathname in p:
		path.append(pathname)

ofile  = open('image_train.csv', "wb")
writer = csv.writer(ofile)
# print scores[0,:]
# scores_tensor = torch.from_numpy(scores)

# mm = torch.nn.Softmax()
# _,a = torch.max(mm(Variable(scores_tensor)),1)
# print a[0:20]
# print np.argmax(scores[0:20,:],1)

for i in range(len(submission)):
	row = (path[i],submission[i,0],np.argmax(scores[i,:],0))
	writer.writerow(row)





 
# ofile.close()