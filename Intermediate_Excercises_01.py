#Jacob Wieland
#For this excercise, I had to learn how to initialize and call a function, which I found out about here: https://www.w3schools.com/python/python_functions.asp

def get_unique_list(og_list: list):

    unique_list = []
    
    i = 0
    j = 0
    k = 0
    while(i < len(og_list)):
        if(unique_list.count(og_list[i]) < 1):
            unique_list.append(og_list[i])
        i = i + 1
    
    return unique_list


my_list = [2, 3, 8, 9, 8, 0, 3, 1]
unique = get_unique_list(my_list)
print(unique)

    

