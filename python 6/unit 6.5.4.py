# Distance midlle dots in coords [x, y]
def distance_between_dots(a: list, b: list)-> float:
    
    try:
        if type(a[0]) is not int or type(a[1]) is not int \
            or type(b[0]) is not int or type(b[1]) is not int:
                
                raise ValueError
            
    except ValueError:
        print('Wrong coords!')
        return

    return round(((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2), 2)

def str_to_int(_lst: list)-> list:
    result_lst = []
    
    for each in _lst:
        result_lst.append(int(each))
        
    return result_lst

#print(distance_between_dots([1, 2],[4, -4]))
#print(distance_between_dots([5, 2],[-11, -4]))
a = str_to_int(input('Please enter coord dot A[x,y]: ').split(','))
b = str_to_int(input('Please enter coord dot B[x,y]: ').split(','))
print(distance_between_dots(a, b))