import os
i=0
for file in os.listdir('.'):
	if file.endswith(".jpg"):
		j = f'0000{i}.jpg'
		if i>=10:
			j = j[1:]
		if i>=100:
			j = j[1:]
		os.rename(file, j)
		i += 1