# Python program to swap two elements in a list
def swap_Position(list, pos1, pos2):
    list[pos1],list[pos2] = list[pos2],list[pos1]
    return list
list = [23,65,19,90]
pos1,pos2 = 1,3

print(swap_Position(list,pos1-1,pos2-1))

def swapPositions(lis, pos1, pos2):
    temp=lis[pos1]
    lis[pos1]=lis[pos2]
    lis[pos2]=temp
    return lis
# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
 
print(swapPositions(List, pos1-1, pos2-1))