import sys
fin1 = open("in.txt", 'r')
attending = []
left = []
for line in fin1:
	temp = list(map(str, line.rstrip().split()))
	attending += temp

fin2 = open("out.txt", 'r')
for line in fin2:
	temp = list(map(str, line.rstrip().split()))
	left += temp

for student in left:
	if student in attending:
		attending.remove(student)