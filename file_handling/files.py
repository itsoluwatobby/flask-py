# r = Read
# a = Append
# w = Write
# x = Create
import sys
import os

# Read (r) - error if not found
# try:
#     path = sys.path[0]
#     f = open(path+'\\names.txt', 'r')
# except FileNotFoundError:
#     print('File Not Found')
# else:
#     # print(f"\n{f.read()}\n")
#     # print(f"\n{f.read(4)}\n") reads the first 4 characters in the file

#     # print(f"{f.readline()}") reads a line of a file
#     # print(f"{f.readline()}")
#     for line in f:
#         print(line)
# finally:
#     f.close()

# Append (a) - appends to an existing file or creates a file if it doesn't exists
# try:
#     path = sys.path[0]
#     fAppend = open(path+'\\names.txt', 'a')
# except FileNotFoundError:
#     print('File Not Found')
# else:
#     fAppend.write('\nMark')
#     print('\nWrite successful\n')
#     fAppend.close()
    
#     fRead = open(path+'\\names.txt', 'r')
#     print(fRead.read())
# finally:
#     fRead.close()

# Write (w) - opens a file for writing and also creates a file if it doesn't exit
# try:
#     path = sys.path[0]
#     fWrite = open(path+'\\context.txt', 'w')
# except FileNotFoundError:
#     print('File Not Found')
# else:
#     fWrite.write('Mark\nSam\nDaniel\n')
#     print('\nWrite successful\n')
#     fWrite.close()

#     fRead = open(path+'\\context.txt', 'r')
#     print(fRead.read())
# finally:
#     fRead.close()


# Create (x) - also creates a file if it doesn't exit but returns an error if it exist
# try:
#     path = sys.path[0]
#     if not os.path.exists(path+'\\list.txt'):
#         fWrite = open(path+'\\list.txt', 'x')
#     else:
#         fWrite = open(path+'\\list.txt', 'w')    
# except (FileNotFoundError, Exception) as error:
#     print('File Not Found')
# else:
#     fWrite.write('Mark\nSam\nDaniel\n')
#     print('\nWrite successful\n')
#     fWrite.close()

#     fRead = open(path+'\\list.txt', 'r')
#     print(fRead.read())
#     fRead.close()
# finally:
#     print('\nDone')

# Delete a file
# try:
#     path = sys.path[0]
#     if os.path.exists(path+'\\lists.txt'):
#         pass
#     else:
#         raise FileNotFoundError('File Does Not Exist')
# except FileNotFoundError as error:
#     print(error)
# else:
#     os.remove(path+'\\list.txt')
# finally:
#     print('\nDone')

path = sys.path[0]
with open(path+'\\names.txt') as f:
    content = f.read()

with open(path+'\\more_names.txt', 'w') as f:
    f.write(content)