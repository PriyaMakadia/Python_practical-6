#Number of Occurance of the Words

x = int(input())

dict = {}
for i in range(x):
    str = input()
    if str in dict:
        dict[str] +=1
    else:
        dict[str] = 1
        
print("\n")
print(len(dict))
for i in dict.values():
    print(i ,end=' ')


