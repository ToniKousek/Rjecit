# wordle game logic

from os import getcwd

# the check_words function is the most important
# returns -1 if word is not in the file
# returns 1 if word is correct
# it returns a tuple with two elements
# a list of the given words
# a list with the coloring lists
# example:
#(['aaaaa', 'ameba'], [['g', ' ', ' ', ' ', ' '], ['g', ' ', 'y', ' ', ' ']])
# when the answer is "aeiou"
# the 'g' is green
# the 'y' is yellow

len_of_words = 5

# the lookup table
lookup = []
with open(f"{getcwd()}\\HR_5_letters.txt", "r", encoding="utf-8") as file:
    for line in file:
        lookup.append(line.split()[0])

# print(lookup[:100])


def check_coloring(answer: str, word: str):

    word_col = [" " for i in range(len_of_words)]
    temp_answer = [answer[i] for i in range(len_of_words)]
    # set all green
    for i in range(len_of_words):
        if word[i] == temp_answer[i]:
            word_col[i] = "g"
            temp_answer[i] = " "

    # set all yellow
    for i in range(len_of_words):
        print(f"{(word[i] in answer)=} {word[i]=} {answer=} ")
        if word[i] in temp_answer:
            word_col[i] = "y"
            # find the index of the letter
            temp_answer[temp_answer.index(word[i])] = " "

    return word_col


def check_words(answer: str, words: list[str]):

    # check if last word is in the lookup table
    if not (words[-1] in lookup):
        return -1

    # see if the word is the answer
    if words[-1] == answer:
        return 1

    # calculate the coloring
    else:
        colored_words = []
        for word in words:
            colored_words.append(check_coloring(answer, word))
    return (colored_words)


# example
# words_to = ["aaaaa", "Aaaaa"]
# print(check_words("aeiou", words_to))
