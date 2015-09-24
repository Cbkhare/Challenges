from sys import argv
import re, math, ast

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n') for line in fp]
#content = [item.split(' ') for item in contents]

#content = fp.read().split(';')
'''
center, radius, point = input_line.split(";")
center = ast.literal_eval(center.split(":")[1].strip())
radius = ast.literal_eval(radius.split(":")[1].strip())
point = ast.literal_eval(point.split(":")[1].strip())

print (center, radius, point)
'''
#print (contents, '\n' , content)
#content = input().split()
#boolean= []
#jhakas = lambda lst,siz: [lst[i:i+siz] for i in range(0,len(lst),siz)]


data = "Center: (2.12, -3.48); Radius: 17.22; Point: (16.21, -5)"
for item in contents:
    result = re.search('Center: \(([-0-9\.]+), ([-0-9\.]+)\); Radius: ([-0-9\.]+); Point: \(([-0-9\.]+), ([-0-9\.]+)\)', item)
    center_x, center_y, radius, point_x, point_y = map(float, result.groups())
    #print (center_x, center_y, radius, point_x, point_y)
    dist = math.sqrt(math.pow(center_x-point_x,2)+math.pow(center_y-point_y,2))
    #print (dist)
    if round(dist,2) <= radius:
        print ('true')
    else:
        print ('false')

'''
Point in Circle

Challenge Description:

Having coordinates of the center of a circle, it's radius and coordinates of a point you need to define whether this point is located inside of this circle.
Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

Center: (2.12, -3.48); Radius: 17.22; Point: (16.21, -5)
Center: (5.05, -11); Radius: 21.2; Point: (-31, -45)
Center: (-9.86, 1.95); Radius: 47.28; Point: (6.03, -6.42)

All numbers in input are between -100 and 100
Output sample:

Print results in the following way.

true
false
true'''
