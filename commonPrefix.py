def commonPrefix(self, string):
    string = [input(i) for i in input().split()]
    # for each character of the first word in the array
    for i in range(len(string[0])):
        char = string[0][i] 
        
        # for each individual words
        for j in range(1,len(string)):
            
            if i == len(string[j]):
                return string[0][:i]
            
            if string[j][i] != char:
            	return string[0][:i]
    
    if not string: 
    	return ""
    
    return string[0]