
import time
def get_time(function,validation):
    start = time.time()
    function(**validation['data'])
    end = time.time()
    return(end - start)

def simulation(function,validation,sim_number, increment):
    step=sim_number//increment
    results=[]
    for i in range(0,step):
        validation['data']['search']=i*increment
        validation['result']=i*increment
        results.append(get_time(function,validation))
        
    return results

def test_validations(function,validations):
    for test in validations:
        result=function(**test['data']) 
        if result== test['result']:
            print('Test Passed ->: {}'.format(test['description']))           
        else:
            print('Test Failed ->: {}'.format(test['description']))
            
        print('\t Input   ->: Input {}'.format(test['data']))
        print('\t Results ->: Output {}, expected {}'.format(result,test['result']))    