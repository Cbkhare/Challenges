#Applying the technique of Decorators with passing them the Arguments
def bazinga(fun):
    def wrap_fun(num_list):
        new_num_list = fun(num_list)
        for i in new_num_list:
            #num = new_num_list
            print('+91'+' '+str(i[-10:-5])+' '+str(i[-5:]))
    return wrap_fun
        
@bazinga
def sort_list(num_list):
    num_list.sort()
    return num_list


if __name__== "__main__":
    num = int(input())
    num_list= [] 
    for i in range(num):
        num_list.append(input()[-10:])
    sort_list(num_list)


"""
Problem Statement

Lets dive into decorators! You are given N mobile numbers. Sort them in ascending order after which print them in standard format.

+91 xxxxx xxxxx



The given mobile numbers may have +91 or 91 or 0 written before the actual 10 digit number. Alternatively, there maynot be any prefix at all.

Input Format

An integer N followed by N mobile numbers.

Output Format

N mobile numbers printed in different lines in the required format.

Sample Input

3
07895462130
919875641230
9195969878

Sample Output

+91 78954 62130
+91 91959 69878
+91 98756 41230

Concept

Like most other programming languages, python has the concept of closures. Just extending it gives us decorators, which is an invaluable asset. You can learn about decorators in 12 easy steps from here.
To solve the above question, make a list of the mobile numbers and pass it to a function which sorts the array in ascending order. Make a decorator which standardizes mobile numbers and apply it to the function. Simpe, Isn't it!
"""
