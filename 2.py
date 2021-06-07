
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

# input string from user and splite with ' ' and convert to list
a = 'The Persian League is the largest sport event dedicated to the deprived areas of Iran. The Persian League promotes peace and friendship. This video was captured by one of our heroes who wishes peace.'
my_string = (a).split(' ')
flag = True
par_word_counter = 0
for words in my_string:

    if flag == True :
        if words[-1] != '.' :
            flag = True
        words = remove_char(words)
        par_word_counter +=1
        if len(words) > 0 :
            if words[0] ==words[0].upper() and par_word_counter>1:
                print('%s:%s' %(par_word_counter,words))
        
        