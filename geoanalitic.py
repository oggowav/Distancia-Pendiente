import math

def distancia(x1,y1,x2,y2):
    d = (math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2)))
    return d
def pendiente (x1,y1,x2,y2):
    if (x2-x1)==0:
        return ("Syntax Error ")
    else:
        return (y2-y1)/(x2-x1)