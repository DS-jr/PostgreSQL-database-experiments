import json 

b_1 = open('v3_other_data.json').read()
# print(type(b_1))
# print(b_1)

b_3 = open('v3_other_data.json').read().split()
# print(b_3) 
# print(type(b_3)) 

b_2 = open('v3_other_data.json')
# print(b_2)
line_1 = b_2.readlines()
# print(line_1)
# print(type(line_1)) 

b_4 = open('file_created_by_python_script.txt', 'w') 
# b_5 = b_4.write('gO to tHe coRe of aNy taSk ! ')

b_6 = b_4.write(b_1)  # Write a string w/ data from JSON file to .txt file 




b_2.close()
b_4.close()

