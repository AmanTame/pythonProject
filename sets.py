#collection of unordered,unindexed data
#no duplicate data is allowed

Group_A={"1","2","3"}
Group_B={"a","b","c"}
print(Group_B)
Group_B.add("1")
print(Group_B)

print(Group_B.union(Group_A))
print(Group_B.difference(Group_A))
print(Group_B.intersection(Group_A))