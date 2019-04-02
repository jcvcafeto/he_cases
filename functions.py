
def remove_repetitive_elements(array):
    """
    Removes nan values from each item of an array
    """
    lista = []
    for item in array:
        lista.append(str(item))
    count = 0
    while 'nan' in lista:
        lista.remove('nan')
    return lista

