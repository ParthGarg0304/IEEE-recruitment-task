# Enter your code here. Read input from STDIN. Print output to STDOUT

l=[]        #list with words
n=int(input())    #number of words

result={}

for i in range(n):       #word input
    word=input()
    l.append(word)
    
    
for j in l:                 #counter number of occurence
    if j in result:
        result[j] += 1
    else:
        result[j] = 1
        
print(len(result))
print(' '.join([str(result[word]) for word in result]))
