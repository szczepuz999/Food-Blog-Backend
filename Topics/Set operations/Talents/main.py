# work with these variables
violinists = set(input().split(', '))
german_speakers = set(input().split(', '))

result = violinists.intersection(german_speakers)
print(result)
