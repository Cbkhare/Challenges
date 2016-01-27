t = int(input())

for i in range(t):
    n = int(input())
    g = {}  # food:pokemon    pokemon:food
    pok  = 0
    for i in range(n):
        f,p = input().split(' ')
        if f==p:  continue
        if f in g:
            g[f] +=1
        else: 
            g[f] = 1
        if p not in g:
            pok += 1
        elif g[p] == 0:
            pok += 1
        else:
            g[p] -= 1
    print (pok)

'''
 Monk in the land of Pokemons!
Attempted by: 1339
/
Accuracy: 94%
/
Tag(s):
Easy, Hashing
Problem
Editorial
My Submissions
Analytics
Code Monk (Hashing)

Monk has to visit a land where strange creatures, known as Pokemons, roam around in the wild. Each Pokemon in the land will attack any visitor. They can only be pacified by feeding them their favorite food.

    The Pokemon of type X eats one food item of type X.

Monk knows that he will encounter N ponds on the way. At each pond, he will find a food item and then encounter a Pokemon. The i'th pond has the food item of type Ai and the Pokemon of type Bi.

The monk can feed the item at the i'th pond to the Pokemon at the pond if the type matches. Monk may have to carry some food items with him before leaving so as to feed all the Pokemons. Help him find the number of items he must carry, to be to able to pass through the land safely.

Input:
The first line contains T, denoting the number of test cases. Then, T test cases follow.
The first line of each test case contains an integer N. Then, N lines follow.
Each line consists of 2 space-separated integers Ai and Bi.

Output: For each test case, print the answer in a new line.

Constraints:
1 ≤ T ≤ 10
1 ≤ N ≤ 105
1 ≤ Ai, Bi ≤ 106
Sample Input
(Plaintext Link)

1
5
1 1
2 2
3 4
4 3
2 4

Sample Output
(Plaintext Link)

1

Explanation

At First Pond he gets item of type1 and feeds it to the Pokemon of type1.
At Second Pond he gets item of type 2 and feeds it to the Pokemon of type2.
At Third Pond he gets item of type 3 ,but the Pokemon is of type4 . Hence, he has to bring a food item of type 4 with him.
At Fourth Pond he gets item of type 4. He already has a item of type 3 and feeds it to the Pokemon.
At Fifth Pond he gets items of type 2. He already has a item of type 4 and feeds it to the Pokemon at this pond.

'''
