import numpy as np



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



def get_new_state_of_cell(window,living):
    suma = 0
    a = window
    for r in range(3):
        for c in range(3):
            
            if a[r,c] != -2:
                if r == 1 and c == 1:
                    pass
                else:

                    if a[r,c] == -1:
                        suma +=1

    return change_state(suma,living)
