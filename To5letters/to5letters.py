# Reduce the number of words by getting only the five lettered words
from time import time
start_time = time()
print("started")

from string import ascii_letters
rules = "-.0123456789'/"

def cro_len(string : str):
    non_en_count = 0
    for letter in string:
        if not (letter in ascii_letters):
            non_en_count += 1
    return len(string) - non_en_count//2


def main(opened_file,writing_file):
    i=1
    temp = ""
    for i in range(624327):
        line = opened_file.readline()
        list_line = [i.strip() for i in line.split()]


        if list_line[-1] == "kratica" or any([c in rules for c in list_line[1]]):
            continue
        

        if cro_len(list_line[1]) == 5 and temp != list_line[1].lower():
            print(f"{i} 5 {list_line[1]}")

            #IMPORTANT HERE
            writing_file.write(f"{list_line[1]} {list_line[-1]}\n")

        temp = list_line[1].lower()
        i+=1

    print("Put all in the file")









if __name__ == "__main__":
    with open("HR_Txt-624.txt","r", encoding = 'cp850') as f, open("HR_5_letters.txt","w", encoding = 'cp850') as f2:
        main(f,f2)



print(f"Took {time()-start_time}")