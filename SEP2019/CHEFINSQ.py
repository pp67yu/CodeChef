"""
https://www.codechef.com/problems/CHEFINSQ

100 % accepted solution
"""
from math import factorial

def find_count(L, group_by):
    # base case
    result = 1

    res = [0] * 101
    # create a count array:
    for num in L:
        res[num] += 1
    
    
    for i in res:
        # j can be 0 or a number that is the count or the index of it in L
        # this is because if j <= group_by - we do not have to choose when traversing the res array:
        # those index number whatever comes, if its count is less than group_by, they will be in the array - no choosing needed
        # Ex: choosing 3 out 3 nums is 3C3 which is 1 - hence result stays the same group_by = group_by-j
        if i <= group_by: 
            group_by -= i
        else:
            # if you reach here that means that we have to choose group_by values from j whre J is > group_by
            result = result * (factorial(i)/(factorial(group_by)*factorial(i-group_by)))
            group_by -=  i

        # check if group_by < 0: meaning we have chosen all the required numbers:
        if group_by < 0:
            break
    
    print(int(result))



if __name__ == "__main__":
    for i in range(int(input())):
        chi = list(map(int, input().split()))
        l = chi[0]
        group_by = chi[1]

        L = list(map(int, input().split()))
        find_count(L, group_by)
