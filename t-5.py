#Program corse -python Advence S01 +++REVIEW+++ - T-5 Day-2 % 1400-03~17

#this function remove ',' and '.'
def remove_char (string):
    postion=None
    while ',' in string or '.' in string:
        if ',' in string:
            postion =(string.find(','))
        else:
            postion =(string.find('.'))
        string = string[:postion]+string[(postion+1):]
    return(string)

#body
my_string = (input()).split(' ') #give string from user and splite with ' ' and convert to list
sentence_Counter = 0 
string_counter = 1
for words in my_string:
    #print(words,string_counter,sentens_Counter)
    if sentence_Counter != 0 and len(words) > 0: #cheking word is not first word in sentence and not blanck
        pure_words = remove_char(words)
        if pure_words[0] ==pure_words[0].upper(): #chek for main condition
            print('%s:%s' %(string_counter,pure_words))  #print output string
    string_counter +=1
    sentence_Counter +=1
    if words[-1] == '.' : 
        sentence_Counter = 0