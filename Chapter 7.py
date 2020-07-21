#Chapter 7 Exercise 1
#Solution to Programming Exercise 1 of Chapter 7 of Python For Everybody:
#Python For Everybody, Dr. Charles R. Severance
fname = input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	print("File cannot be opened: ", fname)
	exit()
for line in fhand:
	line = line.upper()
	print(line)


#Chapter 7 Exercise 2
#Solution to Programming Exercise 2 of Chapter 7 of Python For Everybody:
#Python For Everybody, Dr. Charles R. Severance
fname = input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	print("File cannot be opened: ", fname)
	exit()
count = 0
sum = 0.0
for line in fhand:
	if line.startswith("X-DSPAM-Confidence: "):
		num = float(line[21:])
		sum += num
		count += 1
average = sum / count
print("Average spam confidence: ", average)

#Chapter 7 Exercise 3
#Solution to Programming Exercise 3 of Chapter 7 of Python For Everybody:
#Python For Everybody, Dr. Charles R. Severance
fname = input('Enter the file name: ')
if fname == "na na boo boo":
	print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
	try:
		fhand = open(fname)
	except:
		print("File cannot be opened: ", fname)
		exit()

	count = 0
	for line in fhand:
		count += 1

	print("There were ", count, "subject line in ", fname)
