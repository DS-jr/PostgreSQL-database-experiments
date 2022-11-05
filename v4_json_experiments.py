c_1 = open('v3_other_data.json') 

# read_1 = c_1.read().split(',')
# print(read_1)
# print(type(read_1))
# string_1 = str(read_1)
# print(type(string_1))

# c_2 = open('file_created_by_python_script.txt', 'w')
# write_1 = c_2.write(string_1) 

read_2 = c_1.read().split('changes_log')
# print(read_2)
# print(type(read_2))
# print(len(read_2))

c_3 = (read_2[0])
# print(c_3)
# print(type(c_3))

c_4 = open('file_created_by_python_script.txt', 'w')
c_4.write(c_3)


c_1.close()
# c_2.close() 
c_4.close()
