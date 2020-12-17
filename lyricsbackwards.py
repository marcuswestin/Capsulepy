import os 
dir_path = os.path.dirname(__file__)

file = open(dir_path + "/Whatcomesnext.txt", 'r')
lyrics = file.read()


###this reverses the text three ways and then does something fun### 
#1) First the characters are reversed
#2) Then the words are reversed with line breaks removed, but punctuation remains intact
#3) Then the lines are reversed
#4) Then the words on each line are reversed
#5) Then the text is garbled. On each line , the line breaks remain intact but the words are scrambled up and the punctuation in removed

def reverse_letters(lyrics):#why do I have to put something in the parentheses?
    characters_reversed = ''.join(reversed(lyrics))
    return characters_reversed

print("##### these are the letters reversed #####")
print(reverse_letters(lyrics))

def reverse_words(lyrics):
    words = lyrics.split()
    space_separated_reversed = ' '.join(reversed(words))
    return space_separated_reversed # do I have to do this?

print("##### these are the words reversed #####")
print(reverse_words(lyrics))

def reverse_lines(lyrics):
    lines = lyrics.splitlines() #I'm curious about putting things before the period
    for line in reversed(lines):
        print(line)

print("##### these are the lines reversed #####")
print(reverse_lines(lyrics))

def reverse_words_per_line(lyrics):
    # 'they say ...'
    lines = lyrics.splitlines()
    # ['they say', ...]
    reversed_lines = []
    # []
    for line in lines:
        words = line.split(' ')
        #['they','say']
        #['oceans','rise']
        words.reverse()
        #['say','they']
        #['rise','oceans']
        reverse_line = ' '.join(words)
        #'say they'
        #'rise oceans'
        reversed_lines.append(reverse_line)
        #['say they']
        #['say they','rise oceans']
    lines_joined = '\n'.join(reversed_lines)
    return lines_joined

print("##### these are the words on each line reversed #####")
print(reverse_words_per_line(lyrics))


#This next part isn't quite working and I'm not sure why. The capitalize funciton is not working and I also want to move the punctuation
import random
import string
def randomize_words_per_line(lyrics):
    #You're on your own
    #Do you know how hard it is to lead?
    lines = lyrics.splitlines()
    # ['You're on your own', 'Do you know how hard it is to lead?']
    random_lines = []
    # []
    for line in lines:
        words = line.split(' ')
        #['You're','on'. '...']
        #['Do','you' '...']
        random.shuffle(words)
        #['own','You're']
        #['lead?','Do']
        random_line = ' '.join(words)
        #'own You're ...'
        #'lead Do ...'
        random_line.lower()
        #'own you're ...'
        #'lead do ...'
        random_line.capitalize() 
        #'Own you're ...'
        #'Lead do ...'
        random_lines.append(random_line)
        #['Own you're ...']
        #['Lead do']
     
    lines_joined = '\n'.join(random_lines)
    return lines_joined

print("##### these are the words on each line randomized #####")
print(randomize_words_per_line(lyrics))
