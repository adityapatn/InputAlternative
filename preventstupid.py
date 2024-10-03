'''
My bad code:

def takeinput(message, datatype):
    tf = {True:True, 1:True, "1":True, "T":True, "True":True, "yes":True, "yeah":True, False:False, 0:False, "0":False, "F":False, "False":False, "no":False, "nah":False}

    value = input(message)

    if datatype == int:
        try:
            value = int(value)
        except:
            print("That can't be converted to an integer.")
            return takeinput(message, datatype)
    
    return value

The better code (recommended to me by father)
'''

def takeinput2(message, datatype):
    while True:
        value = input(message)
        try:
            return int(value)
        except:
            print("That can't be converted to an integer.")

need = takeinput2("I need an integer: ", int)
print(need)