# reading names.txt and writing into names_write.txt
with open('names.txt') as fr, open('names_write.txt', 'w') as fw:
    fw.write('Yesterday I went to phonex mall\n')
    fw.write('with my family members and relatives')
    print(fr.read())





