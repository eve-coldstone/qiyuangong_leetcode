##1
list = ['PIN', 'ALSIG', 'YAHR', 'PI']
print(f"list of char arrays are :", list)
print(type(list))
print(''.join(list))  ## PINALSIGYAHRPI
##2
string1 = 'abcac'
string2 = 'bcac'
print(f"max of 2 strings based off alphabetic is :", max(string1, string2))
print(f"max of 2 strings based off length is :", max(string1, string2, key = len))