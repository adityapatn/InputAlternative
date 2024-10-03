'''
My bad code:

def deprecatedfunction(message, datatype):
    tf = {True:True, 1:True, "1":True, "T":True, "True":True, "yes":True, "yeah":True, False:False, 0:False, "0":False, "F":False, "False":False, "no":False, "nah":False}

    value = input(message)

    if datatype == int:
        try:
            value = int(value)
        except:
            print("That can't be converted to an integer.")
            return takeinput(message, datatype)
    
    return value
'''
#The better code:

def takeinput(message, datatype):
    tf = {True:True, 1:True, "1":True, "T":True, "True":True, "yes":True, "yeah":True, False:False, 0:False, "0":False, "F":False, "False":False, "no":False, "nah":False}
    
    while True:
        value = input(message)

        if datatype == int:
            try:
                return int(value)
            except:
                print("That can't be converted to an integer.")
        if datatype == float:
            try:
                return float(value)
            except:
                print("That can't be converted to a float.")
        if datatype == bool:
            try:
                return tf[value]
            except:
                print("That can't be converted to a boolean.")
        