import string

text = input()




def manipulate_title(article_title):
    updated_article_title = ''
    punctuation_chars = string.punctuation
    # punctuation_chars = punctuation_chars + "’" + '‘'

    temp_string = list(
        article_title)  # because string is not mutable we need to convert it to list and later join it

    for i in range(len(temp_string)):

        # checking whether the char is punctuation.
        if temp_string[i] in punctuation_chars:
            # Printing the punctuation values
            # print("Punctuation: " + i)
            temp_string[i] = ''
            # print(updated_article_title)
        # if last char is space
        if temp_string[i] == ' ' and i == (len(temp_string) - 1):
            temp_string[i] = ''

    updated_article_title = "".join(temp_string)
    return updated_article_title

text_no_punction = manipulate_title(text)
text_lowercase = text_no_punction.lower()
print(text_lowercase)
