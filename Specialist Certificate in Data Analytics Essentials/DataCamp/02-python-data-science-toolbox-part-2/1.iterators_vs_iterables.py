'''
Iterators vs Iterables
The environment has been pre-loaded with the variables flash1 and flash2.
Try printing out their values with print() and next() to figure out which is an iterable and which is an iterator.


Instructions
Possible Answers

    Both flash1 and flash2 are iterators.
    Both flash1 and flash2 are iterables.
    flash1 is an iterable and flash2 is an iterator.

#answer is C
'''
flash1= ['jay garrick', 'barry allen', 'wally west', 'bart allen']
flash2 = iter(flash1)


print(flash1)

print(next(flash2))

#print(flash2)
#next(flash1)




