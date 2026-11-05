
def func_1(lst_value): 
    ''' 
    Produces an average of all of the numbers in the list
    ''' 

    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
        sum = sum + value 
    return sum/num_of_value 