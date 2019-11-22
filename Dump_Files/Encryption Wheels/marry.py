'''
   takes a liste in as vertical list and converts it to a linier one.  
'''
def marry(notepad):
    fo = open(notepad, 'r')
    letters = fo.readlines()
    fo.close()

    word = ''
    for i in letters:
        word = word+i
    word= word.replace('\n', '')

    return word 
