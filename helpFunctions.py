def string_in_list(strng, lst): 
    rtn = -1
    for i,element in enumerate(lst): 
        if strng in element: 
            rtn = i 
    return rtn

