dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

text = input()
list_of_words = text.split()
counter = 0
for word in list_of_words:
    if word in dictionary:
        counter += 1

    else:
        print(word)

if counter == len(list_of_words):
    print("OK")
