#By: Aditya (July 7th 2021 , 7:00 PM)

def hint(hint_list,i,cat):
    '''
        (hint function)
           By: Aditya
              Gives hint when user asks for it by typing 'hint' .
    '''
    if cat ==1:
        L = [0,1,3,2]
    elif cat ==2:
        L=[0,1]
    else:
        L=[1,0]
    if i>=len(L):
        return hint_list[L[-1]]
    else:
        return hint_list[L[i]]

