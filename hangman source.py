import random
import time
def count_line():
    file_text = open(r"E:\hangman\word_base.txt", "r")
    count=0
    for line in file_text:
        if line!="\n":
            count+=1
    file_text.close()
    return count

def take_word():
    file_text=open(r"E:\hangman\word_base.txt","r")
    n=random.randint(1,count_line())
    i=0
    while i<n:
        word=file_text.readline()
#        print(word)
        i+=1
    #filter word
    i=len(word)-1
    while word[i].islower()==False:
        word=word[:i]
        i-=1
    return word

def create_quiz(word):
    n=random.randint(2,4)
    loc=[]
    key=[]
    for i in range (n):
        location=random.randint(0,len(word)-1)
        while location in loc:
            location = random.randint(0, len(word) - 1)
        key.append(word[location])
        word=word[:location] + "_" + word[location+1:] #replace key word by _
        loc.append(location)
    return word,key,loc

def answer(word_not,key,loc,guess_word):
    count=0
    i=0
    while i<len(key):
        if key[i] == guess_word:
            word_not = word_not[:loc[i]] + key[i] + word_not[loc[i] + 1:] #if answer correctly, replace _ by character
            count+=1
            loc.pop(i)
            key.pop(i)
        else:
            i+=1
    return count,word_not

Y="y"
while Y=="y":
    print("--Start--")
    i_health=5
    word_original = take_word()
    word_not,key,loc =create_quiz(word_original)
    print(word_not)
    while i_health>0 and len(loc)>0:
        guess=str(input())
        dem,word_not=answer(word_not , key , loc ,guess)
        if dem == 0:
            i_health -= 1
            print("No exist    health: ",i_health*"|")
            print(word_not)
        else:
            print("character",guess,"exist", dem,"times")
            print(word_not)
    if i_health == 0:
        print("LOSE")
        print("word is:",word_original)
    else:
        print("WIN")
    print()
    time.sleep(2)
    Y = str(input("Start_game? y/n "))
print()
print("End game,bye")
exit()


