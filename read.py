data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:  # %这个符号，求余数，1000的倍数才印出来
			print(len(data))
print(len(data))
print(data[0])
pring('-----------------------')
print(data[1])
