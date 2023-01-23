#Jacob Wieland
#For this excercise, I had to look up how to make letters lowercase with the .lower() command, which I found out about here: https://www.datacamp.com/tutorial/case-conversion-python
final_dict = {}  

entry = str(input("Enter a string: "))

lower_entry = entry.lower()

i = 0
    
while (i < len(lower_entry)):
    if(lower_entry[i] != " " and lower_entry[i] not in final_dict):
        final_dict[lower_entry[i]] = lower_entry.count(lower_entry[i])
    i = i + 1

print(final_dict)
