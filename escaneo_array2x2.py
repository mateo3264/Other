import numpy as np

#a = np.array([[-2,-2,-2],[-2,-1,0],[-2,0,0]])


def change_state(suma,living):
    if living:
        if 1 < suma < 4:
            return -1
        else:
            return 0
    elif not living:
        if suma == 3:
            return -1
        else:
            return 0

    #a = np.random.randint(-1,1,size=(2,2))
    #a = np.pad(a,(1,1),constant_values=(-2,-2))
    #print(a)

def get_new_state_of_cell(window,living):
    suma = 0
    a = window
    for r in range(3):
        for c in range(3):
            #print('a[r,c]',a[r,c])
            if a[r,c] != -2:
                if r == 1 and c == 1:
                    pass
                else:
     #               print('ENTRO')
                    #if r == 0 and c == 0:
                    #print('r',r,'c',c)
                    if a[r,c] == -1:
                        suma +=1
                    #elif a[r,c] == 0:
                     #   suma +=1
    return change_state(suma,living)
    #print(suma)
