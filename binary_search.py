
from tools.simulation import *
validations= []

validations.append({
    'data':{
        'numbers': [1,3,7,13,21,45,67,89],
        'search': 1
    },
    'result' : 0,
    'description':'Number at the beginning'
    })

validations.append({
    'data':{
        'numbers': [1,3,7,13,21,45,67,89],
        'search': 89
    },
    'result' : 7,
    'description':'Number at the end'
    
    })

validations.append({
    'data':{
        'numbers': [1,3,7,13,21,45,67,89],
        'search': 100
    },
    'result' : -1,
    'description':'Missing number'
    })
validations.append({
    'data':{
        'numbers': [89],
        'search': 89
    },
    'result' : 0,
    'description':'One number only'
    })
validations.append({
    'data':{
        'numbers': [1,3,3,4,7,13,21,45,67,89],
        'search': 7
    },
    'result' : 4,
    'description':'Number Repetions'
    })

def find_number_binary(numbers, search):
    rigth= 0
    left= len(numbers)-1
    
    while rigth <= left:
        center = (rigth + left) // 2
        center_number = numbers[center]
                
        if center_number == search:
            return center
        elif center_number < search:
            rigth = center + 1  
        elif center_number > search:
            left = center - 1
    
    return -1

large_validation = {
    'data': {
        'numbers': [i for i in range(10000000)],
        'search': 99999999
    },
    'result': 99999999,
    'description':'Very large list'    
    }
     
test_validations(find_number_binary,validations)


import matplotlib.pyplot as plt
sim_number=10000000
increment=500000
ypoints_binary=simulation(find_number_binary,large_validation,sim_number,increment)
plt.plot(ypoints_binary, color = 'b')
plt.show()