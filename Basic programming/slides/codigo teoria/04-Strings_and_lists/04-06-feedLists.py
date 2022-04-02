writers = []
writer = input("Tell me one of your favourite writers")
while writer != "":
	writers.append(writer)
	writer = input("Tell me one of your favourite writers")
writers.sort()
print(writers)