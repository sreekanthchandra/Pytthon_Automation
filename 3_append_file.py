'''
1. To do append operation on file we have to open a file with 'a' mode
2. If you open a file with append mode if file is not exist it will create file, if file is exist it will add new data after old data.

'''

fw = open('append_names.txt', 'a')

# To write data into file
fw.write('\nHi Sriram')
fw.write('\nHow are you')

# To close a file
fw.close()