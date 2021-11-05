compress_dt = {}
decompress_dt = {}

def preprocess():
	for letter in range(256):
		compress_dt[chr(letter)] = letter
	for letter in range(256):
		decompress_dt[letter] = chr(letter)

def compress(str):
	temp = str[0]
	ans = []
	count = 256
	for i in range(1, len(str)):
		temp += str[i]
		if temp in compress_dt:
			continue
		else:
			ans.append(compress_dt[temp[:-1]])
			compress_dt[temp] = count
			temp = str[i]
			count += 1
	ans.append(compress_dt[temp])
	return ans
	
def decompress(arr):
	count = 256
	curr = decompress_dt[arr[0]]
	ans = curr
	prev = curr
	index = arr[0]
	for i in range(1, len(arr)):
		temp = arr[i]
		if temp in decompress_dt:
			curr = decompress_dt[temp]
		else:
			curr = decompress_dt[index]
			curr += prev
		ans += curr
		prev = curr[0]
		decompress_dt[count] = decompress_dt[index] + prev
		count += 1
		index = temp
	return ans	

preprocess()
instring = input("enter a string : ")
ans = compress(instring)
print(f'compressed : {ans}')
ans = decompress(ans)
print(f'decompressed : {ans}')