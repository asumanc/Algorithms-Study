#Used the stack to store the position of the parentheses which are not valid,
#then the two adjacent not valid positions are
#the length of a valid  parenthetical string;
# time complexity O(n)
def LongestValidParantheses(s):
    maxLen = 0
    stack = []
    for i in range(len(s)):
        if s[i] = ')' and len(stack) > 0 and s[stack[-1]] == '(' :
            stack.pop(len(stack) - 1)
            maxLen = 2
        else:
            stack.append(i)
    # full match
    if len(stack) == 0:
        return len(s)

    # insert elements at the beginning and end to calculate the
    # matching parentheses of the head or tail
     stack.append(len(s))
     stack.insert(0 , -1)

     j = len(stack) - 1
     while j > 0:
         maxLen = max(maxLen, stack[j] - stack[j - 1] - 1)
         j -= 1
     return maxLen
     
print(LongestValidParantheses(s))
