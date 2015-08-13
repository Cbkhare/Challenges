import sys
'''
file_name = sys.argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n') for line in fp]
content = [item.split(' ') for item in contents]
'''

if sys.byteorder=='little':
        print ('LittleEndian')
else:
        print ('BigEndian')
'''
 Write a program which prints the endianness of the system.
Input sample:

There is no input for this program.
Output sample:

Print to stdout the endianness, wheather it is LittleEndian or BigEndian.

For example:
BigEndian
'''
