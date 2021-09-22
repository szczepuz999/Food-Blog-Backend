# read sample.txt and print the number of lines
file = open('sample.txt', 'r')

print(len(file.readlines()))
file.close()