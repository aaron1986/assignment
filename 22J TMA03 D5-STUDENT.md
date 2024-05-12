### Edit this cell to enter your name and PI. Then run the JavaScript cell below to identify answer and feedback cells.
**Name: Aaron Bruce Smith**\
**PI: abs247** 



```javascript
%%javascript
var head=document.getElementsByTagName('head')[0],style = document.createElement('style'),css = '.answercell{background-color: #ffffcc;}.feedbackcell{background-color: #c8ecff;}.guidancecell{background-color: #f2c0d4;}';head.appendChild(style);style.type = 'text/css';style.appendChild(document.createTextNode(css));Jupyter.notebook.get_cells().map(function(cell) {if (cell.metadata['cellcol']!= undefined) {cell.element.addClass(cell.metadata['cellcol']);}});
```


    <IPython.core.display.Javascript object>


# TMA 03
M269 requires all assignments to be submitted electronically, by following the
link(s) from your StudentHome page to the online TMA/EMA service.

If you foresee any difficulty with submitting your assignment on time then you
should contact your tutor well in advance of the cut-off date.

For further information about policy, procedure and general submission of
assignments please refer to the
[Assessment Handbook](https://help.open.ac.uk/documents/policies/assessment-handbook),
which can also be accessed via your StudentHome page.

The learning outcomes assessed by each questions are outlined at the head of
the question.

If you use an algorithm, data structure or operation that is not allowed in a
part of a question, your answer to that part will be awarded zero marks.

Your TMA should be opened and edited in Jupyter notebooks. Ensure you put your
name and PI at the top of this document. You should run the second cell to
highlight the answer cells in yellow.

All of TMA 02 is in this document. There are five questions worth 100 marks.



## PART 1


### Question 1 (34 marks)

You should be able to answer this question after you have studied Chapter 8.

This question tests the following learning outcomes:

- Develop and apply algorithms and data structures to solve computational problems.
- Explain how an algorithm or data structure works, in order to communicate with relevant stakeholders.
- Analyse the complexity of algorithms to support software design choices.
- Write readable, tested, documented and efficient Python code.

This question is about the set and bag ADTs, and the corresponding Python classes `set` and `Counter`, introduced in Sections 8.4, 8.5 and 8.6.  The operations for the set ADT and the bag ADT are listed in Chapter 8 along with details of their Python implementations.

In answering this TMA, remember that you can only use the Python data types, methods and functions listed in the chapter summaries, unless specified otherwise in this TMA.

**The files `m269_tma03_filehandling.py` and `m269_util.py` should be in the folder with this TMA notebook.**



#### Q1(a) (3 marks)

We wish to explore the differences between sets and bags, and in particular the effect of operators on these ADTs.

In Python the main operators that can be used on sets and bags are as follows (Y and N indicate whether a given operator is available for that ADT).

| Operator | Python | sets | bags |
| :--- | :-- |:-- |:-- |
| Intersection | `&` | Y  |  Y |
| Union        | `\|` |Y  |  Y |
| Difference   | `-`  |Y  |  Y |
| Sum   | `+`  | N  |  Y |

Where an operator can be used for both sets and bags the effect may be slightly different in some cases.  The Sum operator for bags in Python, implemented using the `Counter` class, adds the counts of corresponding elements in the two bags. See [here](https://docs.python.org/3/library/collections.html#collections.Counter) for details and examples.

The following code defines a simple test function and several sets whose members are individual characters, derived from character strings.

Run this code to set up the test function and initialise the sets.




```python
def one_test(name, actual, expected, details:bool=False) -> None:
    """Report if test passed or failed.
       Final argument is optional- if True, then details of failed test are displayed
    """
    if actual == expected:
        print(name, 'OK')
    else:
        print(name, 'FAILED')
        if (details):
            print(' got', actual, '\n instead of', expected)

# Examples of using the one_test function, with and without details.
# If the "details" argument is True then a FAILED test gives information
# about the expected and actual results of the test.
one_test('1 and 1 makes 2', 1 + 1, 2)
one_test('1 and 1 makes 2', 1 + 1, 2, details = True)
one_test('2 and 2 makes 4', 2 + 2, 5)
one_test('2 and 2 makes 4', 2 + 2, 5, details = True)


PARLIAMENT = 'parliament'
ARIAN = 'arian'
PARLIAMENTARIAN ='parliamentarian'

set_P  = set(PARLIAMENT)
set_A  = set(ARIAN)
set_PA = set(PARLIAMENTARIAN)


```

    1 and 1 makes 2 OK
    1 and 1 makes 2 OK
    2 and 2 makes 4 FAILED
    2 and 2 makes 4 FAILED
     got 4 
     instead of 5
    

#### Q1(a)(i) (1 mark)

Run the following test to explore use of set operators.




```python
one_test('set_PA - set_P = set_A : ',  set_PA - set_P, set_A)

```

    set_PA - set_P = set_A :  FAILED
    

Given the way these sets were defined, you might have expected this test to pass. Explain briefly below why it fails. We want a general explanation, not a list of the elements of each set, for example.



Add your answer for Q1(a)(i) here: <br><br>
The test will fail because set _PA is not equal to either set _P or Set_A. 

This problem can be further explained, if we were to subtract the word ARIAN from PARLIAMENT, this will mean that we are still left with the letter’s ‘A’, and ‘R’ (the letters A and R appear twice in the word PARLIAMENT). Additionally, the word ‘PARLIAMENTARIAN’ has the letter ‘A’ printed three times, which means ’set_A’ is not equal to either set.




#### Q1(a)(ii) (2 marks)
The tests below will also fail (run them to confirm this).  Edit the code below to change one operator in each test so that the tests pass. You should also change the operator in the test title (the first argument of the `one_test` function so that it matches your change to the test).




```python
one_test('set_P  - set_A = set_PA: ',  set_P  - set_A, set_PA)
one_test('set_PA - set_A = set_A : ',  set_PA - set_A, set_A)

```

    set_P  - set_A = set_PA:  FAILED
    set_PA - set_A = set_A :  FAILED
    

Explain below why each of your changed tests works. We want a general explanation, not a list of the elements of each set. You will get no marks here if you do not provide explanations.



Add your answer for Q1(a)(ii) here:<br>
To pass the test use the code: one_test('set_P | set_A = set_PA: ', set_P | set_A, set_PA) one_test('set_PA & set_A = set_A : ', set_PA & set_A, set_A)

To pass the first test, change the ‘Difference’ operator (-) to a ‘Union’ (|) operator; this will output the different sets without the duplicate letters.

To pass the second test, change the ‘Difference’ operator (-) to an ‘Intersection’ (&) operator, this will output the sets which share letters that are common in both sets. 



#### Q1(b) (4 marks)

The following code defines several bags whose members are individual characters, derived from character strings.  The bags are implemented using the Python Counter class.

Run this code and then answer the questions in the section following the code.




```python
from collections import Counter

bag_P  = Counter(PARLIAMENT)
bag_A  = Counter(ARIAN)
bag_PA = Counter(PARLIAMENTARIAN)

one_test('bag_P union bag_A = bag_PA: ',  bag_P | bag_A, bag_PA)
one_test('bag_PA intersection bag_A = bag_P: ',  bag_PA & bag_A, bag_P)
one_test('bag_PA intersection bag_P = bag_A: ',  bag_PA & bag_P, bag_A)

```

    bag_P union bag_A = bag_PA:  FAILED
    bag_PA intersection bag_A = bag_P:  FAILED
    bag_PA intersection bag_P = bag_A:  FAILED
    

#### Q1(b)(i) (2 marks)
You should have found that all the tests in the previous code have failed.  Explain briefly below why this is so. We want a general explanation, not a list of the elements of each bag.



Add your answer for Q1(b)(i) here:<br>
The tests failed, because, in the first test, bag_P (PARLIAMENT) contains a different number (count) of the same letters than either bag_PA (PARLIAMENTARIAN) or bag_A (ARIAN). Additionally, bag_PA contains the letter ‘A’ four times while bag_P only contains the letter ‘A’ twice.<br><br> The second test also failed, because, it will return false as the count value doesn’t exist (is not the same) in both sets. Moreover, the set’ bag_P’ is different from set bag_A, because the letters in bag_P contains letters that are not present in bag_A. 




#### Q1(b)(ii) (2 marks)
Edit the code below to change one operator in each test so that all the tests pass.  You should also change the test title (the first argument of the `one_test` function so that it matches your change to the test).




```python
one_test('bag_P union bag_A = bag_PA: ', bag_P + bag_A, bag_PA)
one_test('bag_PA intersection bag_A = bag_P: ', bag_PA - bag_A, bag_P)
one_test('bag_PA difference bag_P = bag_A: ', bag_PA - bag_P, bag_A) 
```

    bag_P union bag_A = bag_PA:  OK
    bag_PA intersection bag_A = bag_P:  OK
    bag_PA difference bag_P = bag_A:  OK
    

Then explain below why your changed operations work correctly. We want a general explanation, not a list of the elements of each bag. You will get no marks here if you do not provide explanations.



Add your answer for Q1(b)(ii) here:<br><br>
Changing the original operator from a union operator to an addition operator allows us to combine (concatenate) the elements of both bags, thus, ensuring that the two bags include all the unique elements which are needed to work.  <br><br>
The second line of code was changed from the ‘intersection’ operator to a ‘difference’ operator, the difference operator subtracted the elements that were not present in both bags. <br><br>
Lastly, in the original code we used the intersection operator for the test, by changing the operator to a ‘difference’ operator, the elements that were not present in both bags were subtracted.   





#### Q1(c) (4 marks)



#### Q1(c)(i) (1 mark)
Run the following code that tests the use of the `len` function on strings, sets and bags and explain below why the second and third tests  fail.  We want a general explanation, not a list or a count of the elements of each set or bag.




```python
one_test('len(PARLIAMENT) + len(ARIAN) == len(PARLIAMENTARIAN) : ',  len(PARLIAMENT) + len(ARIAN) == len(PARLIAMENTARIAN), True)
one_test('len(set_P) + len(set_A) == len(set_PA) : ',  len(set_P) + len(set_A) == len(set_PA), True)
one_test('len(bag_P) + len(bag_A) == len(bag_PA) : ',  len(bag_P) + len(bag_A) == len(bag_PA), True)

```

    len(PARLIAMENT) + len(ARIAN) == len(PARLIAMENTARIAN) :  OK
    len(set_P) + len(set_A) == len(set_PA) :  FAILED
    len(bag_P) + len(bag_A) == len(bag_PA) :  FAILED
    

Enter your answer for Q1(c)(i) here<br><br>
The first test will satisfy the condition because Strings are an ordered sequence of characters (Strings are sequence types).
<br><br>
The second test will fail because the ‘sets’ (a set is unordered with no duplicates) are unordered elements. Moreover, there are duplicates of letters in the words ‘Parliament’ and ‘Arian’ which will show the sum (‘Parliamentarians’) as ten. As a set is unordered with no duplicates it will return fail.<br><br> The third test will also fail, bags are also unordered but allow duplicates, which means that the words ‘Parliament’ and ‘Arian’ when combined will add up to 12 letters. This will result in a test fail.




#### Q1(c)(ii) (3 marks)
For a more useful measure of the size of a bag, we need a function to calculate how many items are in a bag, counting multiple occurrences of any characters that occur more than once.  Write a function called `size`, that does this and carry out a revised version of the bag length test above to check that it works.  Also add the code as indicated below to further test the `size` and `len` functions,

Recent versions of Python have added a function like our `size` function to the `Counter` class, but you will only get marks here if you write your own function.

The `Counter` class has a useful method `most_common` that can be used to find the `n` most common items in a bag and their multiplcities, for any positive integer `n`.  Run the following code for the standard documentation showing how to use this method.




```python
help(bag_A.most_common)

```

    Help on method most_common in module collections:
    
    most_common(n=None) method of collections.Counter instance
        List the n most common elements and their counts from the most
        common to the least.  If n is None, then list all element counts.
        
        >>> Counter('abracadabra').most_common(3)
        [('a', 5), ('b', 2), ('r', 2)]
    
    

You may also want to look up this method online [here](https://docs.python.org/3/library/collections.html#collections.Counter) .  You will find it useful in the following exercise and also later in this question.




```python
def size(bag : Counter)-> int:
    """ returns the total number of items in a bag """
    # Replace the following with your code
    return sum(bag.values())
    pass

# Use this test to check if your `size` function works as expected
one_test('size(bag_P) + size(bag_A) == size(bag_PA) : ',  size(bag_P) + size(bag_A) == size(bag_PA), True, details=True)

def one_test(test_name, result, expected, details=False):
    print(test_name)
    if details:
        print(f"Result: {result}, Expected: {expected}")
    assert result == expected

# Create a new bag here containing the characters of your full name and your OU PI, all in lower case with no spaces.
pass   # replace this line  with your code
namePI_bag = Counter("aaronbrucesmithabs247")

# Display the number of distinct characters and the total number of characters in your namePI bag (counting any multiple occurrences).
pass   # replace this line with your code
print("Number of distinct characters:", len(namePI_bag))
print("Total number of characters:", size(namePI_bag))

# Use the `Counter` method `most_common` to find and display the 5th most common character in your namePI bag and its frequency of occurrence.
pass   # replace this line with your code
common_chars = namePI_bag.most_common()
if len(common_chars) >= 5:
    fifth_common_char = common_chars[4]
    print("5th most common character:", fifth_common_char[0])
    print("Frequency of occurrence:", fifth_common_char[1])
else:
    print("Not enough characters for 5th most common.")

```

    size(bag_P) + size(bag_A) == size(bag_PA) :  OK
    Number of distinct characters: 16
    Total number of characters: 21
    5th most common character: o
    Frequency of occurrence: 1
    

#### Q1(d) (11 marks)

We want to be able to carry out an analysis of words in long documents to find the most frequently used words. This can be used for example to identify the most important words for language learning or to try to identify authors in literary works.   Later on we will ask you to analyse two Shakespeare plays, Hamlet and The Merchant of Venice, to find the 20 most frequent words and the number of times each word occurs.  Because the most common words are mainly stop words (articles, prepositions, etc.) and the play's characters (e.g. Hamlet, Horatio, Portia etc.) we will also want the ability to exclude certain words from the analysis.

First we want to explore the problem in a more general abstract form.

Given the name (string) of a text file containing words, a positive integer `m` and a text file containing excluded words (strings), find the `m` most frequent words in the file (apart from the excluded words) and their frequencies, given in descending order of frequency.

We define this more formally, as follows:

**Operation**: Most common in file\
**Inputs**: *filename*, a string; *excluded-words-filename*, a string; *m*, integer\
**Preconditions**: Files of names *filename* and *excluded-words-filename* are text files; *m* > 0\
**Outputs**: *most-common-words*, a list of at most *m* items, where each item is a tuple\
**Postconditions**: Each item of *most-common-words*, is a tuple containing a word from the file *filename* together with its frequency, with the list being in descending order of frequency, and no tuples for words from *excluded-words-filename* are in the list.\
The frequency component of each tuple in *most-common-words* is greater than or equal to the frequency of occurrence for any other words in *filename*, ignoring any words in *excluded-words-filename*.




#### Q1(d)(i) (3 marks)
The main ADT to use for storing the text should be a bag.  You will also need to choose a suitable ADT for the excluded words, and you can also use other standard simple built-in data structures of Python such as lists or strings, if necessary.

State what sort of ADTs and data structures you would use for this problem and explain what is stored in these ADTs. Do not explain your choices at this stage - we will ask about that later.



Add your answer for Q1(d)(i) here:<br><br>
The ADT(s) and data structures I would use to solve this problem are as followed.

(1) If I were to store word(s) from a text file, I would use the ADT entitled Bag, moreover, this process will allow each word within the text file to be added to the bag. Moreover, allowing the user to iterate through an array with its frequency represented by the number of occurrences; in this example the int variable 'm'.

(2) If I were to use the most efficient ADT for checking whether a word or unique element should be excluded from an analysis I would use the ADT entitled set. I could therefore, store unique elements ensuring that each excluded word is only stored once. 

(3) I would use the Data Structure entitled Lists. Lists are an ordered collection of data or items. The Data Structure Lists will provide a simple way to maintain an ordered collection of items; which will allow the most common words and their frequencies to be stored. Moreover, the user can retrieve and manipulation items that are stored from the list. 





#### Q1(d)(ii) (3 marks)

Give a step-by-step explanation, showing how your solution would work.

You can make use of any of the bag ADT operations listed in Chapter 8.




Write your answer to Q1(d)(ii) here

The following steps are my explanation for the question ‘How would I implement the solution’.

(1) Process the words from the text file provided. I would instruct the computer to read the contents of the text file and then create a bag to store the words from the text file along with their frequencies.

(2) Sort the bag by frequency, I would create a set to store each of the words to the set of excluded words. The next step would to be to convert the bag into a list of tuples, where each tuple contains a word and its frequency. The user could iterate through the bag and then sort this list based on the frequency each tuple. 

(3) Lastly, retrieve the most common words and return the result. Take the first m from the sorted list, m being the most frequent words in the text file, return the list of m most common words along with their frequencies. In this example the user could take the first ‘m’ tuples from the List and return the result.






#### Q1(d)(iii) (5 marks)
Now explain your chosen approach by outlining the characteristics and the expected performance of the operations on bags and other ADTs/data structures you have used, in standard Python implementations. You should reference the performance discussions for bags in Chapter 8 and relevant performance discussions elsewhere in the module text for other ADTs/data structures.




Write your answer to Q1(d)(iii) here 
<br>

<table style="width: 100%; background-color: #f2f2f2;">
    <tr>
        <th>Operation</th>
        <th>Effect</th>
        <th>Algorithm In English</th>
    </tr>
      <tr>
        <th>New </th>
        <th>Creates a new empty bag.</th>
        <th>Initialize an empty bag.</th>
    </tr>
       <tr>
        <th>Size</th>
        <th>Returns the number of items (words) in the bag.</th>
        <th>Count the number of items in the bag.</th>
    </tr>
         <tr>
        <th>membership</th>
        <th>Checks if a given word is present in the bag.</th>
        <th>Check if the word exists in the bag.</th>
    </tr>
         <tr>
        <th>associate</th>
        <th>Associates a value (frequency) to a word in the bag.</th>
        <th>Store the frequency of the word in the bag.</th>
    </tr>
       <tr>
        <th>lookup</th>
        <th>Retrieves the frequency associated with a word in the bag.</th>
        <th>Retrieve the frequency of the word from the bag.</th>
    </tr>
       <tr>
        <th>delete</th>
        <th>Removes a word-frequency pair from the bag.</th>
        <th>Remove the word-frequency pair from the bag.</th>
    </tr>
    <tr>
        <th>(In)equality</th>
        <th>Compares two bags to check if they are the same or different.</th>
        <th>Check if two bags contain the same word-frequency pairs.</th>
    </tr>
    
    
    


#### Q1(e) (12 marks)

Implement your approach from part (d) to solve the abstract problem introduced in part (d) and extended somewhat here:

Analyse two given literary texts to find the 20 most frequent words and the number of times each word occurs.  Exclude from the analysis the words that are often most common but less important to the analysis: so-called stop words (articles, prepositions, etc.) and words naming the text's characters. The original files for the two texts may contain line punctuation and extraneous characters at the start or end of words such as apostrophes, dashes etc and these should be removed before further processing. The excluded words relevant to each text are listed in a given text file - and this has been cleaned so that it just contains the relevant words, without any punctuation or extraneous characters.

In this case the first text is Shakespeare's Hamlet (in the given text file ```hamlet.txt```) with excluded words listed in the given text file ```hamlet_excluded_words.txt```.  The second text is Shakespeare's Merchant of Venice (in the given text file ```merchant.txt```) with excluded words listed in the given text file ```merchant_excluded_words.txt```.

We also want you to find the words that occur in both these texts and the number of occurrences in common for these words  e.g. if `dog` occurs 10 times in the first text and 25 times in the second text, then there are 10 occurrences in common.

We have provided code frameworks for your solution below. We have split the problem and the code framework into two parts so you can do one bit at a time and check each part is working.

The first framework includes functions that handle reading data from files into lists and "cleaning" data to remove punctuation when necessary, as file handling is not covered in M269.

Remember that you can only use the Python data types, methods and functions listed in the chapter summaries, unless specified otherwise in this TMA.



#### Q1(e)(i) (5 marks)
The first part of the problem requires reading a text from a file, eliminating excluded words, and storing the results in a bag.

As in part(d), we define this more formally, as follows:

**Operation**: Get bag from file\
**Inputs**: *filename*, a string; *excluded-words-filename* \
**Preconditions**: Files of names *filename* and *excluded-words-filename* are text files\
**Outputs**: *text*, a bag of words\
**Postconditions**: The bag *text* contains all words from the file *filename* together with their frequency of occurrence, except that any words from *excluded-words-filename* are omitted.

Here is the code framework for this first part of the problem.  We have included some simple test code, to let you check if your code seems to be working so far.

Please make the required changes as indicated by comments. When you have finished run your code to view the output.




```python
# Change this code in the places indicated
# in order to implement and test your solution

%run -i m269_util

# Import the functions read_file and read_and_clean_file
%run -i m269_tma03_filehandling


#  You will need to amend this function so that the excluded
#  words extracted from the list are added to the data structure
#  that is returned. You should also set the type annotation
#  for the function return value

def get_excluded_words(word_list : list) :
    """Returns the excluded words occurring in word_list
       in a suitable data structure.  Here we use a set.
    """
    #  replace the following with your code to initialise the data structure
    words = set()
    #words = None

    #  replace the following with your code to add words from the list if not blank
    for item in word_list:
        if item.strip() =="":
            continue
        words.add(item.strip())
        return words


#  You will need to amend this function so that the words from the list are
#  added to the data structure that is returned, apart from the excluded words.
#  You should also set the type annotations for the excluded_words argument

def bag_of_words(word_list : list, excluded_words)-> Counter:
    """Return the words occurring in word_list as a bag-of-words,
       omitting any excluded words
    """
    words = Counter()

    #  replace the following with your code to add words from the list if not
    #  an excluded word
    
    for word in word_list:
        if not word in words:
            words[word.strip()] +=1
            return words


# You should not need to change this function
def get_bag_from_file(filename : str, excluded_words_file : str) -> Counter:
    """ Return list of "m" most frequent words and their percentage frequencies
        in the text of file "filename", excluding all the words in file "excluded_words"
    """
    excluded_words_list= read_file(excluded_words_file)
    excluded_words = get_excluded_words(excluded_words_list)

    text_list = read_and_clean_file(filename)

    text = bag_of_words(text_list, excluded_words)

    return text


# We have provided the following code here to allow you to check if your
# code is working so far.  You should not need to change it unless you wish
# to add more tests of your own.

print("Collecting words in text...")

text = get_bag_from_file('hamlet.txt', 'hamlet_excluded_words.txt')

test(size, [['Size of text', text, 20635 ]])
test(text.most_common, [['Most common word in text', 1, [('lord', 223)] ]])
```

    Collecting words in text...
    Size of text FAILED: 1 instead of 20635
    Tests finished.
    Most common word in text FAILED: [('project', 1)] instead of [('lord', 223)]
    Tests finished.
    

#### Q1(e)(ii) (7 marks)
The second part of the problem requires reading both texts from files, eliminating excluded words, and storing the results in bags, finding the overlap between the texts and displaying the top 20 most common words and their **relative frequencies** from each text.

[Note the slight refinement from the part (d) problem to use relative rather than absolute frequencies.  The absolute frequency is an integer representing the number of times a word appears in a text.  The relative frequency is a fraction or decimal number, found by dividing the absolute frequency by the total number of words in the text.  This should be a more useful way to compare texts that will usually differ in their total numbers of words.]

As in part(d), we define the key function more formally, as follows:

**Operation**: Most common words\
**Inputs**: *text*, a bag of words; *m*, integer\
**Preconditions**: *m* > 0\
**Outputs**: *most-common-words*, a list of at most *m* items, where each item is a tuple\
**Postconditions**: Each item of *most-common-words*, is a tuple containing a word from the bag *text*, with its relative frequency in the bag, given as a percentage rounded to 3 decimal places. &emsp;The relative frequency component of each tuple in *most-common-words* is greater than or equal to the relative frequency for any other words in the bag *text*.

Here is the code framework for this second part the  problem.  We have included some test code, to let you check if your code seems to be working properly.

Please make the required changes as indicated by comments. When you have finished run your code to view the output.




```python
# Change this code in the places indicated
# in order to implement and test your solution
%run -i m269_util

# Import the functions read_file and read_and_clean_file
%run -i m269_tma03_filehandling

from collections import Counter

#Method from part 1
def size(bag: Counter) -> int:
    return sum(bag.values())

def get_excluded_words(word_list : list) :
    """Returns the excluded words occurring in word_list
       in a suitable data structure.  Here we use a set.
    """
    words = set()
    for word in word_list:
        if word.strip():
            words.add(word)
            
    return words
    
def bag_of_words(word_list : list, excluded_words)-> Counter:
    """Return the words occurring in word_list as a bag-of-words,
       omitting any excluded words
    """
    words = Counter()

    #  replace the following with your code to add words from the list if not
    #  an excluded word
    
    for word in word_list:
        if word not in excluded_words:
            words[word] +=1
    
    return words

    
def get_bag_from_file(filename : str, excluded_words_file : str) -> Counter:
    """ Return list of "m" most frequent words and their percentage frequencies
        in the text of file "filename", excluding all the words in file "excluded_words"
    """
    excluded_words_list= read_file(excluded_words_file)
    excluded_words = get_excluded_words(excluded_words_list)

    text_list = read_and_clean_file(filename)

    text = bag_of_words(text_list, excluded_words)

    return text

# You should not have to change this function
def relative_frequencies(words_freq : list,  text_size : int) -> list:
    """ Convert the list of (word, absolute frequency) pairs in a text to relative
        frequencies in percentages, rounded to 3 decimal places
    """
    relative_frequency = []
    for w in range(0, len(words_freq)):
        relative_frequency.append( (words_freq[w][0], round((100*words_freq[w][1])/text_size, 3)) )

    return relative_frequency


# Complete the missing parts of this function where indicated by comments
def most_common_words(text : Counter, m : int) -> list:
    """ Return list of "m" most frequent words and their percentage frequencies
        in the text of file "filename", excluding all the words in file "excluded_words"
    """
    # Find total number of words in the text
    # Replace the following line with your code
    text_size = size(text)

    # Find the "m" most common words and their absolute frequencies
    # Replace the following line with your code
    frequency = text.most_common(m)

    # Convert the list of words and absolute frequencies to relative frequencies in percentages
    # Replace the following line with your code
    relative_frequency = relative_frequencies(frequency, text_size)

    return relative_frequency


# You should not have to change this function
def print_table(m : int, frequency_1 : list, frequency_2 : list, frequency_3 : list) -> None:
    """ Print formatted table of 'm' most frequent words and their percentage frequencies
        in each of three lists containing (word, frequency) pairs.
        If there are fewer than "m" items in any of the lists then the table will have the
        same number of rows as the length of the smallest list
    """
    n = min(m, len(frequency_1), len(frequency_2), len(frequency_3))
    print()
    print("The", n, "most frequent words and their percentage frequencies are:")
    print('First text        |    Second text       |    In Both')
    print('===============================================================')

    for i in range(0, n):
        print(f'{frequency_1[i][0]:10} {(frequency_1[i][1]):6.3f} |\
    {frequency_2[i][0]:10} {(frequency_2[i][1]):6.3f} |\
    {frequency_3[i][0]:10} {(frequency_3[i][1]):6.3f}')


TOP = 20
print('Finding the top', TOP, 'most frequent words in first text ...')
# Replace the following two lines with your code
text_1 = get_bag_from_file('hamlet.txt', 'hamlet_excluded_words.txt')
frequency_1 = most_common_words(text_1, TOP)
print("Done")

print('Finding the top', TOP, 'most frequent words in second text ...')
# Replace the following two lines with your code
text_2 = get_bag_from_file('merchant.txt', 'merchant_excluded_words.txt')
frequency_2 = most_common_words(text_2, TOP)
print("Done")


# Find words occurring in both texts and the number of occurrences in common
# Replace the following line with your code
text_3 = text_1 & text_2

print('Finding the top', TOP, 'most frequent words in third (overlap) text ...')
# Replace the following line with your code
frequency_3 = most_common_words(text_3, TOP)
print("Done")

#  Run tests for first 3 words from each text
test(most_common_words, [['Most common text_1', text_1, 3,
                        [('lord', 1.081), ('king', 0.950), ('have', 0.906)] ]])
test(most_common_words, [['Most common text_2', text_2, 3,
                        [('have', 1.207), ('will', 0.982 ), ('do', 0.858)] ]])
test(most_common_words, [['Most common text_3', text_3, 3,
                        [('have', 1.807), ('will', 1.470 ), ('do', 1.285)] ]])

print_table(TOP, frequency_1, frequency_2, frequency_3)


```

    Finding the top 20 most frequent words in first text ...
    Done
    Finding the top 20 most frequent words in second text ...
    Done
    Finding the top 20 most frequent words in third (overlap) text ...
    Done
    Tests finished.
    Tests finished.
    Tests finished.
    
    The 20 most frequent words and their percentage frequencies are:
    First text        |    Second text       |    In Both
    ===============================================================
    lord        1.081 |    have        1.207 |    have        1.807
    king        0.950 |    will        0.982 |    will        1.470
    have        0.906 |    do          0.858 |    do          1.285
    will        0.858 |    shall       0.778 |    shall       1.165
    do          0.809 |    thou        0.749 |    thou        1.122
    all         0.669 |    all         0.647 |    all         0.969
    queen       0.582 |    well        0.589 |    well        0.828
    o           0.582 |    am          0.553 |    at          0.795
    shall       0.562 |    at          0.531 |    would       0.795
    good        0.528 |    would       0.531 |    her         0.740
    come        0.514 |    her         0.495 |    let         0.730
    they        0.514 |    let         0.487 |    come        0.708
    thou        0.509 |    here        0.487 |    more        0.686
    at          0.485 |    than        0.473 |    good        0.686
    more        0.480 |    come        0.473 |    then        0.686
    now         0.480 |    thee        0.473 |    which       0.675
    let         0.465 |    then        0.465 |    how         0.642
    how         0.456 |    more        0.458 |    thy         0.642
    her         0.441 |    good        0.458 |    love        0.642
    project     0.431 |    which       0.451 |    thee        0.632
    

### Question 2 (26 marks)

You should be able to answer this question after you have studied Chapter 18.

This question tests the following learning outcomes:

- Develop and apply algorithms and data structures to solve computational problems.
- Explain how an algorithm or data structure works, in order to communicate with relevant stakeholders.
- Analyse the complexity of algorithms to support software design choices.
- Write readable, tested, documented and efficient Python code.

**Graphs** are explained in Chapters 17 and 18 and we will make use of some of the Python code provided there to implement graphs.
We will revisit the context of the previous question &ndash; analysis of the words in long documents. However, in this case, instead of ordering by frequency we wish to consider connections between words, in particular the occurrence of pairs of words in a particular order.  Such ordered groups of words are known as **bigrams** for two words, trigrams for three words, and in general `n`-grams for an ordered sequence of `n` words.

The table in Chapter 17 Section 17.2.4 shows the operations defined for unweighted graph ADTs, both directed and undirected.  The ADT for weighted graphs is similar but with some differences, as explained in Chapter 18 Section 18.2.2.




#### Q2(a) (11 marks)

We want to be able to carry out an analysis of the relationships between words in long documents.  This can be useful in studies of literary style, identifying likely authors of texts for example.

Later on we will ask you to apply this analysis to Shakespeare's Hamlet. For this question, we will assume that **the file has been cleaned** to remove all line punctuation and other unnecessary leading or trailing characters such as quote marks from the words.

First we want to explore the problem in a more general abstract form.

Given the name (string) of a text file containing words, store the words in such a way as to record which words precede or follow other words. Analyse this stored data to identify the `m` most common ordered pairs of words (bigrams) where `m` is an integer value.  We define this more formally, as follows:

**Operation**: Most common bigrams\
**Inputs**: *filename*, a string; *m*, integer\
**Preconditions**: File of name *filename* is a text file; *m* > 0\
**Outputs**: *most-common*, a list of at most *m* items, where each item is a triple\
**Postconditions**:  Each item of *most-common*, is a triple containing the two words of a bigram from the file, together with its frequency, with the list being in descending order of frequency.
The frequencies of all items in *most-common* are greater than or equal to the frequencies of all other bigrams in *filename*.



#### Q2(a)(i) (4 marks)
The ADT you use should be some kind of graph, though you can use other standard simple built-in data structures of Python such as lists or strings, if necessary.

State what sort of graph ADT you would use for this problem (directed/undirected, weighted/unweighted).  Explain what is represented by the features of the graph, such as its nodes and edges, and why this is a suitable choice.



Write your answer to Q2(a)(i) here<br><br>
I would use a directed and weighted approach to solving the ADT graph, a directed graph will show the relationship between words in an unidirectional way (when each word increments). Additionally, the weighted graph is used to track the frequency of each node using the shortest path. Moreover, I would use a node to represent each [unique] word from the input text file, each edge will represent the connection between the nodes. 



#### Q2(a)(ii) (3 marks)

Give a step-by-step explanation, showing how your solution would work.

You can make use of any of the graph ADT operations from Chapters 17 and 18.




Write your answer to Q2(a)(ii) here<br><br>
(1) Read the text file:<br>
(2) Create Nodes: Create a node for each unique word in the text file.<br>
(3) Create Edges: For each pair of consective words in the text file, create a directed edge from the node representing the first word to the node representing the second node. <br>
(4) Update Edge Weights: increment the weight of the edge reprenting the bigram by 1.<br>
(5) Filter Low-Frequency Bigrams: removing any bigrams with a frequency below a specified threshold. <br>
(6) Sort Edges: sort the edges in decending order of their weights.<br>
(7) Extract Most Common Bigrams: extract the top 'm' edges (where 'm' is a specified integer) to obtain the most common bigrams.<br> 




#### Q2(a)(iii) (4 marks)
Now outline the expected performance of the operations on graphs and other data structures you may have used, in standard Python implementations.  You should explain which graph representation (edge list/adjacency matrix/adjacency list) you would use, and reference the performance discussions for graphs in Chapters 17 and 18.




Write your answer to Q2(a)(iii) here
<br>
<table style="width:100%; background-color: #f2f2f2;">
    <tr>
        <th>
            Operation
        </th>
        <th>
            Implementation
        </th>
        <th>
            Complexity
        </th>
    </tr>
    <tr>
    <td>
        Reading text file
    </td>
    <td>
        Python build in functions (open())
    </td>
    <td>
        0(n)
    </td>
    </tr>
    <tr>
        <td>
        Create Nodes and Edges
    </td>
    <td>
        Iteration
    </td>
    <td>
        0(1) per node or edge
    </td>
    </tr>
       <tr>
        <td>
        Updating Edge Weights
    </td>
    <td>
        Increment the weight of an edge
    </td>
    <td>
        0(1)
    </td>
    </tr>
       <tr>
        <td>
        Filtering Low-Frequency Bigrams
    </td>
    <td>
        Iterate over edges
    </td>
    <td>
        0(n), where n is the number of edges
    </td>
    </tr>
        <tr>
        <td>
        Sorting Edges
    </td>
    <td>
        Python's build-in sorting algorithms
    </td>
    <td>
        0(n log n)
    </td>
    </tr>
        <tr>
        <td>
        Extracting Most Common Bigrams
    </td>
    <td>
        Selecting top 'm' edges
    </td>
    <td>
        0(m)
    </td>
    </tr>
</table>

#### Q2(b) (10 marks)

Implement your approach from part (a) to solve the problem introduced in part (a) and repeated again here, but applied to a specific text:

Analyse Shakespeare's Hamlet (in the given text file `cleaned_hamlet.txt`) to
store all the words in a graph that records which words precede or follow other words. Analyse this graph to identify and display the 20 most common ordered pairs of words (bigrams). You can assume that all punctuation and unnecessary leading and trailing characters (such as quote marks) as well as the very common words have already been removed.

We have provided a framework for your solution below, with comments indicating where you will need to make changes.

Remember that you can only use the Python data types, methods and functions listed in the chapters' summaries unless specifically mentioned in this TMA.

You should make use of relevant parts of the code demonstrated in Chapters 17 and 18 for the of graph ADTs - the code for directed and undirected graphs (both weighted and unweighted) are within the included files.

**The files `m269_ungraph.py`, `m269_digraph.py`, `m269_tma03_filehandling.py` and `m269_util.py` should be in the folder with this TMA notebook.**

To make things easier we provide the framework code in two parts - first the framework for setting up the graph representing the words in the document, then the framework for the rest of the problem - finding and displaying the most common bigrams.



#### Q2(b)(i) (5 marks)
Here is the first part - setting up the graph. When you have made the required changes run your code and check that the printed output seems reasonable.




```python

%run -i m269_digraph
%run -i m269_ungraph
%run -i m269_util

# Import the function read_file
%run -i m269_tma03_filehandling

"""
You will need to amend this function so that it adds the words from the text
file to a graph in the form of nodes and edges.  You should also set the
return type appropriately.
"""

def graph_of_words(word_list : list):
    """Return the words occurring in word_list as a graph
    """
    # replace the right hand side of this statement with an appropriate initialisation
    words = None

    # Add your code for this function here

    return words


print("Collecting words in Shakespeare's Hamlet...")

word_list = read_file('cleaned_hamlet.txt')

word_graph = graph_of_words(word_list)

print("Printing the graph of words")
#  Replace the following line with your code to display the contents
# of the graph without any attempt to reorder it
pass




```


    ---------------------------------------------------------------------------

    OSError                                   Traceback (most recent call last)

    ~\anaconda3\lib\site-packages\IPython\core\magics\execution.py in run(self, parameter_s, runner, file_finder)
        713             fpath = arg_lst[0]
    --> 714             filename = file_finder(fpath)
        715         except IndexError:
    

    ~\anaconda3\lib\site-packages\IPython\utils\path.py in get_py_filename(name, force_win32)
        108     else:
    --> 109         raise IOError('File `%r` not found.' % name)
        110 
    

    OSError: File `'m269_digraph.py'` not found.

    
    During handling of the above exception, another exception occurred:
    

    Exception                                 Traceback (most recent call last)

    ~\m269_tma03_filehandling.py in <module>
    ----> 1 get_ipython().run_line_magic('run', '-i m269_digraph')
          2 get_ipython().run_line_magic('run', '-i m269_ungraph')
          3 get_ipython().run_line_magic('run', '-i m269_util')
          4 
          5 # Import the function read_file
    

    ~\anaconda3\lib\site-packages\IPython\core\interactiveshell.py in run_line_magic(self, magic_name, line, _stack_depth)
       2362                 kwargs['local_ns'] = self.get_local_scope(stack_depth)
       2363             with self.builtin_trap:
    -> 2364                 result = fn(*args, **kwargs)
       2365             return result
       2366 
    

    ~\anaconda3\lib\site-packages\decorator.py in fun(*args, **kw)
        230             if not kwsyntax:
        231                 args, kw = fix(args, kw, sig)
    --> 232             return caller(func, *(extras + args), **kw)
        233     fun.__name__ = func.__name__
        234     fun.__doc__ = func.__doc__
    

    ~\anaconda3\lib\site-packages\IPython\core\magic.py in <lambda>(f, *a, **k)
        185     # but it's overkill for just that one bit of state.
        186     def magic_deco(arg):
    --> 187         call = lambda f, *a, **k: f(*a, **k)
        188 
        189         if callable(arg):
    

    ~\anaconda3\lib\site-packages\IPython\core\magics\execution.py in run(self, parameter_s, runner, file_finder)
        723             if os.name == 'nt' and re.match(r"^'.*'$",fpath):
        724                 warn('For Windows, use double quotes to wrap a filename: %run "mypath\\myfile.py"')
    --> 725             raise Exception(msg)
        726         except TypeError:
        727             if fpath in sys.meta_path:
    

    Exception: File `'m269_digraph.py'` not found.


#### Q2(b)(ii) (5 marks)
Here is the second part - finding and displaying the `m` most common bigrams in the graph from part (b)(i).  We have provided some tests to show you if your first few results are as expected.

When you have made the required changes run your code, check that it passes the tests and that the printed output seems reasonable.

If your code does work properly you might want to try it on other documents but this is optional and not required for this TMA.  We found the texts used in this TMA at [Project Gutenberg](https://www.gutenberg.org/) which has many free and out-of-copyright great works of literature.




```python

"""
You will need to complete this function so that it adds the words from the text
file to a graph in the form of nodes and edges.  You should also set the
return type appropriately.
"""

def most_common_bigrams(filename : str, m : int)-> list:
    """ returns the 'm' most common bigrams and their frequencies in file 'filename'
    """
    # We have provided the function 'read_file' to read the text file into
    # a list of words, with each word as a separate string item in the list.
    # File handling is not covered in M269
    word_list = read_file(filename)

    word_graph = graph_of_words(word_list)

    # Replace the following two lines of code with your code to extract from the
    # graph and return the 'm' most common bigrams and their frequencies,
    # in descending order of frequency
    pass

    return []



print("Collecting words in Shakespeare's Hamlet...")

# The following code tests if your first few results are as expected.
# You should not need to change these unless you decide to add more tests
# They follow the test table approach used in the module text

expected_results = [
                   ('first', 'clown', 33),
                   ('good', 'lord', 23),
                   ('1', 'e', 22),
                   ('room', 'castle', 20),
                   ('project', 'electronic', 18)
                   ]

test_table =    [
                ['Most common bigram', 'cleaned_hamlet.txt', 1, expected_results[:1]],
                ['Top 3 bigrams',      'cleaned_hamlet.txt', 3, expected_results[:3]],
                ['Top 5 bigrams',      'cleaned_hamlet.txt', 5, expected_results[:5]]
                ]

test(most_common_bigrams, test_table)

TOP = 20

#  Replace the following line with your code to find the 20 most common
#  bigrams and their frequencies.
results = []

print("Printing top", len(results), "bigrams by frequency")
#  Replace the following line with your code to display up to 20 of the most common
#  bigrams and their frequencies, in an appropriate format.
pass



```

#### Q(2)(c) (5 marks)

We have asked you to use a graph to model the text, so as to solve the specified problem, but perhaps it may not be an appropriate solution?   Discuss the following questions. For guidance we would expect a maximum of three sentences per question.




#### Q2(c)(i) (3 marks)

Could you have used a tree instead of a graph to model the text or to solve the given problem?   If so, what sort of tree would be appropriate or if not, explain why not.



Write your answer to Q2(c)(i) here.



#### Q2(c)(ii) (2 marks)

Would your approach using a graph extend from finding most common bigrams (two words) to finding most common trigrams (three words) or longer groups of words (n-grams)?  Explain why this extended approach would or would not be appropriate.



Write your answer to Q2(c)(ii) here.




## PART 2


### Question 3 (9 marks)

You should be able to answer this question after you have studied Chapter 26.

This question tests the following learning outcomes:

- Understand the main complexity classes.

A government agency is investigating a potential case of fraud
across several companies. The agency creates an undirected graph where
the nodes represent the current employees from all companies involved.
From analysis of LinkedIn and other social media, the agency creates
an edge between two people if they work for different companies now,
but have worked for the same company in the past or
have some other relationship, e.g. are friends or relatives.
To start the investigation, the agency wants to find a group of
mutually connected people. Because of the way edges are created,
those people all work in different companies but know each other and
so the agency suspects them of coordinating the fraud across the companies.

For this question, consider the following variant of the agency's problem.

**Function:** collusion\
**Inputs:** _people_, an undirected graph; _size_, an integer\
**Preconditions:** _people_ has _n_ ≥ 2 nodes; 2 ≤ _size_ ≤ _n_\
**Output:** _colluded_, a Boolean\
**Postconditions:** _colluded_ is true if and only if
_people_ has _size_ nodes connected to each other

Here is an example graph.

![This figure shows a graph with five nodes, labelled A to E.
There are six undirected and unweighted edges:
A–B, B–C, C–E, E–D, D–A and D–B.](TMA03_Q3_graph.png)

For _size_ = 2 the output is true,
because several pairs of nodes (e.g. E and C) are connected.
For _size_ = 3 the output is also true
because nodes A, B and D are connected to each other.
For _size_ ≥ 4 the output is false.
No four (or more) nodes are mutually connected.
For example, A, B, C and D aren't mutually connected because
edges A–C and C–D are missing.

Prove that this decision problem is in class NP by answering the following parts.



#### Q3(a) (5 marks)
Describe a certificate for a problem instance
(a graph _people_ and an integer _size_) that has a true output.
Give as example the certificate for the graph above and _size_ = 3.


*Write your answer to Q3(a) here.*



#### Q3(b) (4 marks)
EExplain why certificates for this problem can be verified in polynomial time.

In other words, briefly explain what the verifier does,
given _people_, _size_ and the corresponding certificate,
and why it takes polynomial time.



*Write your answer to Q3(b) here.*



### Question 4 (8 marks)

You should be able to answer this question after you have studied Chapter 26.

This question tests the following learning outcomes:

- Understand the common algorithmic techniques and complexity classes.

Consider the problem _IsSet_ of deciding if a list of integers represents a set.
For example, the output is true for `[]`, `[5]` and `[4, 20, -2, 567, 0]`,
because they represent sets, and false for `[5, 0, 5, -1]`
because the items in this list aren't unique.



#### Q4(a) (5 marks)
Outline a reduction algorithm that reduces _IsSet_ to
a problem _Solved_ of your choice.
Make sure your outline states what problem _Solved_ is,
what inputs and output it has, and
what the input and output transformations do.

You may include a diagram, drawn by hand or with a computer,
if it helps your explanation.
To do that, put the PNG or JPEG file with your diagram in this folder and
write `![](...)` in the Markdown cell, where ... is the filename,
e.g. `reduction.jpg`.



_Write your answer to Q4(a) here._



#### Q4(b) (3 marks)
Let's assume that your transformations take polynomial time and that
you have additional information that _IsSet_ is tractable.
Do these two pieces of information and your reduction prove that
problem _Solved_ is also tractable? Explain why or why not.



*Write your answer to Q4(b) here.*



### Question 5 (23 marks)
You should be able to answer this question after you have studied Chapter 27.

This question tests the following learning outcomes:

- Understand the Turing Machine model of computation.
- Explain how an algorithm or data structure works, in order to communicate with relevant stakeholders.

We want a Turing machine that capitalises a string:
the first letter of every word is changed to uppercase.

There can only be six different symbols on the tape:
`a`, `A` , `0`, `"` (double quote), space and `None` (blank symbol).
The input tape consists of a double quote, followed by zero or more spaces,
`a`, `A` and `0`, followed by a double quote. The rest of the tape is blank.

When the Turing machine stops, every `a` at the start of the string or
preceded by a space has been replaced with `A`.
The rest of the string must remain unchanged.
For example, if the tape is initially
```
['"', 'a', 'A', ' ', '0', 'a', ' ', 'a', 'a', '"']
```
then the final tape is
```
['"', 'A', 'A', ' ', '0', 'a', ' ', 'A', 'a', '"']
```
The head begins and must end on the first (left-most) double quote.



#### Q5(a) (15 marks)
Write the transition table for the Turing machine.
Use descriptive state names.

The `list` constructor used in the test below was introduced in
Section 4.6.2: `list('"A"')` evaluates to `['"', 'A', '"']`.
Feel free to add your own tests to check your Turing machine, but
you won't be awarded any marks for your tests.
You don't have to remove your tests before submitting this TMA.

Set the debug parameter to `True` if you want to see the configurations
your Turing machine goes through.
Make sure you **set it back to `False` before submitting** your TMA.




```python
%run -i m269_util
%run -i m269_tm

capitalise = {
    # Write the transitions here in the form
    # (state, symbol): (new_symbol, LEFT or RIGHT or STAY, new_state),
}

capitalise_tests = [
    # case,     TM,         input tape,         debug,  output tape
    ('example', capitalise, list('"aA 0a aa"'), False,  list('"AA 0a Aa"')),
]

test(run_TM, capitalise_tests)

```

#### Q5 (b) (8 marks)
Summarise how your Turing machine works,
explaining the main transitions and the purpose of each state.
Your answer shouldn't be a direct translation of the transition table to English.

You may include diagrams, if you wish, drawn by hand or with a computer.
See Question 4(a) about how to include diagrams in Markdown.



*Write your answer to Q5(b) here.*



Submit this TMA by zipping together the notebook along
with all of the helper and data files you have used, and submitting your .zip
file using the online TMA/EMA service.

