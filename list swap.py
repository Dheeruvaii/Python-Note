#  Find the length of the list and simply swap the first element with (n-1)th element.

def swaplist(list):
    first=list.pop(0)
    last=list.pop(-1)

    list.insert(0,last)
    list.append(first)
    # print(swaplist)
    return list

new_list=[12,13,14,15,16]
print(swaplist(new_list))
