
myUniqueList = []
myLeftovers = []


def add_to_leftovers(var):
    myLeftovers.append(var)


def add_to_list(var):
    if var not in myUniqueList:
        myUniqueList.append(var)
        return True
    else:
        add_to_leftovers(var)
        return False


print(add_to_list(5))
print(add_to_list(3))
print(add_to_list(100))
print(add_to_list(100))
print(add_to_list(77))
print(add_to_list(87))
print(add_to_list(41))
print(add_to_list(-2.58))
print(add_to_list(77))
print(add_to_list(-2.58))
print(add_to_list(41))


print(myUniqueList)
print(myLeftovers)
