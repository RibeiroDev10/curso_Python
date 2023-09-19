# outer_function
def create_function(func):

    # inner_function
    def intern(*args, **kwargs):
        
        print('I go to decored!')
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print(f'Your result is: {result}') 
        print('Ok, now you are decored')
        return result
    
    return intern

def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')
    
inverte_string_checando_parametro = create_function(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)