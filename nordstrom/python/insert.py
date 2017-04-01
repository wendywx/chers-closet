import csv


f = open("filtered.csv", 'r')
reader = csv.reader(f)
count = 0
for row in reader:
	print(row)

print(a)
