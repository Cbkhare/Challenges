from sys import argv
import os

file_name = argv[1]

size = os.path.getsize(file_name)   #1st way, ans in Bytes

#info = os.stat(file_name)     #2nd way, also to get all other details 
#size = info.st_size           # ans in Bytes

print (size)

'''
####################Straight Lines##############################
def distance(values):
    #print (values[0][0],values[0][1],values[1][0],values[1][1]) #x0y0,x1y1
    distance = math.sqrt((values[0][0]-values[1][0])**2\
                         +(values[0][1]-values[1][1])**2)
    return distance
    




if __name__== '__main__':
    z = list(itertools.combinations(content,2)) #reuslt is a list of tuples contaning 
    dis_dict = {}                               # list of 2 cordinates
    for data in z:
        dis_dict[str(data)]= round(distance(data),2) #
    for key, value in dis_dict.items():
        print (key,value, math.cos(math.sqrt(value)-1))
        


for key, values in dis_dict.items():
    for i in range(len(key)):
        print (key[i])
'''    
