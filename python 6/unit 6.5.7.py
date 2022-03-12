def calc_words(text:str)->dict:
    alphabet_str = 'abcdefghijklmnopqrstuvwxyz'
    letters_dict = {letter: 0 for letter in alphabet_str}
    words_lst = text.lower().split()
    
    """  
    for i in range(len(words_lst)):
        words_lst[i] = words_lst[i][0]
    
    for each in letters_dict:
        letters_dict[each] = words_lst.count(each)
    """
    
    for each in words_lst:
        letters_dict[each[0]] += 1
    
    return letters_dict

text = 'The try block lets you test a block of code for errors. The except block lets you handle the error. The finally block lets you execute code, regardless of the result of the try- and except blocks.'
print(calc_words(text))