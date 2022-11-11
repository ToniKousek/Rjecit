from main import check_words, random_word, num_of_tries, len_of_words


# for colors
def yellow(s):
    return f"\033[93m {s}\033[00m"


def green(s):
    return f"\033[92m {s}\033[00m"

# calculate the needed coloring


def print_words(words: list[str], colors: list[str]):
    for i in range(len(words)):
        for j in range(len_of_words):
            # calculate the needed coloring
            if colors[i][j] == "y":
                print(yellow(words[i][j]), end="\t")

            elif colors[i][j] == "g":
                print(green(words[i][j]), end="\t")

            else:
                print(words[i][j], end="\t")
        print()


def main(answer):
    words = []

    # main game loop
    while True:
        # player input
        print("Tvoja riječ:")
        inputed_word = input()

        # check the input
        if len(inputed_word) != 5:
            print("Upiši riječ koja ima duljinu 5 slova!")
            continue
        else:
            words.append(inputed_word)

        res_color = check_words(answer, words)

        if type(res_color) == int:
            print("Ta riječ nije u našoj databazi!")
            print("Molim pokušajte ponovno!")
            words.pop()
            continue
        elif type(res_color[0]) == int:
            print(f"Bobijedio si u {len(words)}. pokušaju!")
            print("Bravo!")
            # 1 because the function returns a 1 in the 0th position
            print_words(words, res_color[1])

            # again
            print("Ponovo!\n\n")
            main(random_word())

        else:
            # print the words
            print_words(words, res_color)

        # If 6 tries
        if len(words) >= num_of_tries:
            print("Izgubio si!")
            print(f"Riječ je bila {answer}")
            print("Ponovno!\n\n")
            main(random_word())


if __name__ == "__main__":
    main(random_word())
