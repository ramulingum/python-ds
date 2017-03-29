"""program to illustrate honay towers our target is to move numbers from tower_1 one to tower_3"""


def move_from_tower(n,source,destinataion,intermediate):
    if not n:
        pass
    elif n == 1:
        destinataion.append(source.pop())
        
    else:
        move_from_tower(n-1,source,intermediate,destinataion)
        move_from_tower(1,source,destinataion,intermediate)
        move_from_tower(n-1,intermediate,destinataion,source)
    return source,destinataion,intermediate    
            
tower_1 = [14,11,10,6,5,4,3,2,1]
tower_2 = []
tower_3 = []
move_from_tower(9,tower_1,tower_3,tower_2)
print tower_1,tower_2,tower_3

