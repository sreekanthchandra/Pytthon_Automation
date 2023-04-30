fh = open('write_names.txt', 'r')

## Using read we can read entire file data and return in string format
fdata = fh.read()
print(type(fdata))

## To read the first five characters
#fdata = fh.read(5)
#print(fdata)

## Using readline we can read only one line and return in string format
#line  = fh.readline()
#print(' 1 ',line)

#line  = fh.readline()
#print(' 2 ',line)

## Using readlines we can read entire file data and return in list format
lines = fh.readlines()
print(' 3 ' , lines)

## Using for loop also we can read FH data, it will iterate line by line
# for line in fh:
    # print(' For loop :', line)

# To close a file
# fh.close()
