import re

#just lists of funcatins to help aroundm mostly checking elements in lists and vise versa 

def string_in_list(strng, lst): 
    rtn = -1
    for i,element in enumerate(lst): 
        if strng in element: 
            rtn = i 
    return rtn

def list_in_string(strng, lst): 
    rtn = False 
    for element in lst: 
        if element in strng: 
            rtn = True
    return rtn 

def list_in_string_dict(strng, lst,dicted): 
    rtn = -1 
    for i,element in enumerate(lst): 
        if element[dicted] in strng: 
            rtn = i
    return rtn 

def string_first_num(strng):  
    try: 
        return int(re.findall(r'\d+',strng)[0])
    except: 
        return 0 