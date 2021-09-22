text = input()
words = text.split()
keywords = ["https://", "http://", "www."]
for word in words:
    # finish the code here
     if word.lower().startswith("www."):
        print(word)
     elif word.lower().startswith("http"):
        print(word)


    # for subword in word:

