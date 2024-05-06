'''
M269 22J TMA03 Q2

'''

def read_file(filename : str)-> list:
    """Return the words occurring in filename as a list
    
    filename is a string with the name of a text file
    """
    # You do not need to understand the file handling code in detail
    words = []
    # open the file in read-only mode
    with open(filename, 'r', encoding ='utf-8') as file:
        # go through the file line by line
        for line in file: 
            # use space to separate the words in a line
            for word in line.split():
                if not(word ==''):
                    words.append(word)
    file.close()
    return words



def read_and_clean_file(filename : str) -> list:
    """Return the words occurring in filename as a list,
       removing any line punctuation and also leading or
       trailing punctuation of words.
    
       filename is a string with the name of a text file
    """
    # You do not need to understand the file handling code in detail
    words = []
    # open the file in read-only mode
    with open(filename, 'r', encoding ='utf-8') as file:
        # go through the file line by line
        for line in file:
            # transform line punctuation into space
            line = clean_line(line)
            
            # use space to separate the words in a line
            for word in line.split():
                # remove leading and trailing punctuation from word
                word = clean_word(word)
                if not(word ==''):
                    words.append(word) 
    return words




def clean_line(line : str) -> str:
    """ transform any line punctuation characters into spaces
        returns the transformed line
    """
    for p in ['(','[', '{',')', ']','}', '.',',',';',':','_'] :
        line = line.replace(p, ' ')
    return line


def clean_word(word : str) -> str:
    """ removes any leading or trailing punctuation characters in word
        embedded punctuation such as apostrophes or hyphens is not affected
        returns the transformed word in lower case
    """
    word = word.strip("'\"!?+-*/#‘’—")
    return word.lower()

