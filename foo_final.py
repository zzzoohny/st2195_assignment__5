def is_divisible_by_k(x, k):
    '''
    Checks whether x is divisible by k.
    '''
    #1 assert is used to debug the codes. not appropriate within a function to get back True/False
    #assert x%k == 0 
    return x % k == 0 

'''
Store all the integers that are multiples of 2 or 5 or 7 
that are lower or equal to 1000 (excluding doubles)
'''
#x = ()   #2 round bracket is tuple, an immutable object. need to change to [] to be a list.
              #3 it will be confusing to use the same name, x ,  as above

# for i in range(1000): 
    #4 range(1000) is a list of numbers that are lower than 1000.
    #but numbers lower or equal than 1000 required. hence, change to range(1001)

   # if (is_divisible_by_k(x, 2) & is_divisible_by_k(x, 3)) | 
       # is_divisible_by_k(x, 7): 
            #5 misprint of 5 -> 3
            #6 input is not the list. should be i instead of list x
            #7 boolean operator: the condition is 'or' not 'and'/ '&'
            #8 invalid syntax to continue in the next line, '\' should be used, instead of '|'
       
    # x.append(i) 
    #9 indentation of x.append(i) is wrong. in another block.

nums=[]
for x in range(1,1001):
    if is_divisible_by_k(x,2) or is_divisible_by_k(x,5) or \
       is_divisible_by_k(x,7):
       nums.append(x)

'''
Sum all the integers that are multiples of 2 or 5 or 7 
that are lower or equal to 1000 (excluding doubles)
'''
#sum(x)

total=sum(nums)     #assign variable to save the results
print(total)               #print the results 

