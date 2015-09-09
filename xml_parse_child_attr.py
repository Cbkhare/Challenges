import xml.etree.ElementTree as et


n_line = int(input())
x_line = ''
for i in range(n_line):
    x_line += input() +'\n'
#print (x_line)
etroot   = et.ElementTree(et.fromstring(x_line))
root = etroot.getroot()
#print (root.tag, root.attrib,root[0].tag,root[0].attrib)
score = 0
for element in root.iter(None):   #root.iter('*') can also be used refer to docu
    score += len(element.attrib)  #Note here use of a dict or list is not feasible
    #print (element,element.attrib,)   # read below for further info
print (score)


'''
Use of dict or List:-
Not feasible
1)dict:- 2 keys having same value will be treated as one, hene one of them will
be discarded
2)List:- though list will be give all the dict inside the attribute but it will
give 2 problems
    a) null dict will also get included,
    b) even if null dict are discarded via na if statement, whole attribute of
       a single element if it contains more than key-value pair will be taken
       as a single dict. hence will not give correct count. 
Problem Statement

You are given a valid XML document and you have to print its score. The first line of input is the number of XML lines followed by the XML lines. Score is given by the sum of score of each element. For any element, score is equal to the number of attributes it has.

Input Format

The first line shows the number of lines in XML document followed by the XML document.

Output Format

An integer score

Sample Input
#######################################
11
<feed xml:lang='en'>
  <title>HackerRank</title>
  <subtitle lang='en'>Programming challenges</subtitle>
  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
  <updated>2013-12-25T12:00:00</updated>
  <entry>
  	<author gender='male'>Harsh</author>
    <question type='hard'>XML 1</question>
    <description type='text'>This is related to XML parsing</description>
  </entry>
</feed>

Output = 5
########################################
6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>

Output = 8
'''
