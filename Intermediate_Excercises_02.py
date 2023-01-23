#Jacob Wieland
#I had to look up some things about dictionaries in Python, which I found here: https://www.w3schools.com/python/python_dictionaries.asp
def get_combined_dict(dict1: dict, dict2: dict):
    
    combined_dict = {}
    
    for key1 in dict1:
        for key2 in dict2: 
            if(key1 == key2):
                combined_dict[key1] = dict1[key1] + dict2[key2]

    return combined_dict


my_dict_1 = {'a': 3, 'c': 5, 'f': 9, 'g': 10}
my_dict_2 = {'b': 7, 'c': 9, 'f': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)
    
    
