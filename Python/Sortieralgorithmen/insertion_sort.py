arr = [6,1,7,4,2,9,8,5,3]

for i in range(1,len(arr)):
	tmp = arr[i]
	j = i - 1

	while j >= 0 and arr[j] > tmp:
		arr[j+1] = arr[j]
		j -= 1

	arr[j+1] = tmp
	
print(arr)