def average_from_list(_lst: list)->float:
    
    sum_all = 0
    for each in _lst:
        
        try:
            
            if type(each) is not int and type(each) is not float:
                
                raise ValueError
        
        except ValueError:
            
            print(f'{each} is wrong item!')
            return
        
        sum_all += each
    
    return round(sum_all/len(_lst), 3)

print(average_from_list([1, 5, 4.8, 20.5, 7]))
print(average_from_list([1, 2, 3, 4, 5, 6]))