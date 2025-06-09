import re 

g= " quick brown fox jumps over the lazy dog that was rammed by a car" 

# match =re.search( "ram ",g)

# print("start match", match.start())
# print("end match", match.end())

# view="was" 

# find = re.findall(view,g)
# print("find all", find)


p = re.compile('[a-k]')

print(p.findall(g))