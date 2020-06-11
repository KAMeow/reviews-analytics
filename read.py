data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:  # %这个符号，求余数，1000的倍数才印出来
			print(len(data))
print('档案读取完了，总共有', len(data), '笔资料')

sum_len = 0 # sum 是加总的意思
for d in data:
	sum_len = sum_len + len(d)

print('留言评价长度', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '笔留言少于100')
print(new[0])