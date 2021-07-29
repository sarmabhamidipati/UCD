'''
Pop quiz about errors
Take a look at the following function calls to len():

len('There is a beast in every man and it stirs when you put a sword in his hand.')

len(['robb', 'sansa', 'arya', 'eddard', 'jon'])

len(525600)

len(('jaime', 'cersei', 'tywin', 'tyrion', 'joffrey'))

Which of the function calls raises an error and what type of error is raised?

Possible Answers

    The call len('There is a beast in every man and it stirs when you put a sword in his hand.') raises a TypeError.
    The call len(['robb', 'sansa', 'arya', 'eddard', 'jon']) raises an IndexError.
    The call len(525600) raises a TypeError.
    The call len(('jaime', 'cersei', 'tywin', 'tyrion', 'joffrey')) raises a NameError.

len(525600)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'int' has no len()
'''
#Answer = C
