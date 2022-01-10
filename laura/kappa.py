from sklearn.metrics import cohen_kappa_score
import pandas as pd
import numpy as np
from fleiss import fleissKappa


def cal_kappa(df1,df2):
	#nij i第1位 j第2位
	n11,n10,n01,n00=0,0,0,0

	for i in range(len(df1)):
		if df1[i] == df2[i]:
			if df1[i]==1:
				n11+=1
			else:
				n00+=1
		else:
			if df1[i]==1:
				n10+=1
			else:
				n01+=1
	pa = (n11+n00)/len(df1)
	pe = ((n11+n10)/len(df1))*((n01+n11)/len(df1))+((n01+n00)/len(df1))*((n00+n10)/len(df1))
	score = (pa-pe)/(1-pe)
	return score


def cal_similarity(df1,df2):
	same_count=0
	for i in range(len(df1)):
		if df1[i] == df2[i]:
			same_count+=1
	return same_count/len(df1)


def cal_fleiss_rate(df1,df2,col):
	rate = np.zeros((len(df1), col), dtype=int)
	for i in range(len(df1)):
		for j in range(col):
			if df1[i]==j:
				rate[i,j] += 1
			if df2[i]==j:
				rate[i,j] += 1
			# if df3[i]==j:
			# 	rate[i,j] += 1
	return rate


if __name__ == '__main__':
	df = pd.read_csv(r'C:\Users\GOOD\Desktop\碩班\110-1\IM\final project\code\src\Youtuber道歉事件 - bobo new strategy.csv')
	df = df.fillna(0)
	# print(df)
	people = ['A','B']
	# origin_column = ['_apology1','_apology2','_apology3','_apology4','_apology5','_in_out','_intented','_error_type']
	#
	#
	# for i in people:
	# 	df[i+'_apology23'] = df[[i+'_apology2',i+'_apology3']].max(axis=1)
	# 	df[i+'_apology45'] = df[[i+'_apology4',i+'_apology5']].max(axis=1)
	# 	df[i+'_apology2345'] = df[[i+'_apology2',i+'_apology3',i+'_apology4',i+'_apology5']].max(axis=1)
	#
	# column = ['_apology1','_apology4','_apology23','_apology45','_apology2345','_in_out','_intented','_error_type']
	# # print(df)
	# df.to_csv("apology.csv",index=False, encoding='utf-8 sig')

	# print(df['A_in_out'])
	# print(df['B_in_out'])
	column = ['_error_type', '_thanks', '_compensation', '_apology', '_information', '_reverse', '_excuse']

	kappa = {}
	for col in column:
		score = 0
		for i in range(2):
			for j in range(i+1,2,1):
				# score+=cal_kappa(list(df[people[i]+col]), list(df[people[j]+col]))
				# score+=cal_similarity(list(df[people[i]+col]), list(df[people[j]+col]))
				score+=cohen_kappa_score(df[people[i]+col], df[people[j]+col])


		# kappa[col] = score/3
		# col_num=2
		# if col=='_error_type':
		# 	col_num=4
		# rate = cal_fleiss_rate(list(df['A'+col]),list(df['B'+col]),col_num)
		# if col=='_apology1':
		# 	print(list(rate))
		# score = fleissKappa(rate.tolist(),2)
		kappa[col] = score
	print(kappa)

	#output
	# final_y = np.zeros((df.shape[0], len(column)), dtype=int)
	# for index, row in df.iterrows():
	# 	c = 0
	# 	for col in column:
	# 		counts = np.bincount([row['A'+col],row['B'+col],row['C'+col]])
	# 		final_y[index][c] = np.argmax(counts)
	# 		c += 1
	#
	# final = pd.concat([df.iloc[:,0:2], pd.DataFrame(final_y,columns=column)], axis = 1)
	# final.to_csv("yt_event.csv",index=False, encoding='utf-8 sig')
			