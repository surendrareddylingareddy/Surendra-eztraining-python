s1 = {1,2,5,9}
s2 = {2,4,6,4,0,8}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))
s1.add(10)
s1.update({20,30,40})
print(s1)
s1.discard(9)
print(s1)
s1.remove(10)
print(s1-s2)

s3 = {9,8,6,4,5}
s4 = {1,2,3}
print(s3.issuperset(s4))
print(s4.issubset(s3))
print(s1.symmetric_difference(s4))
print(s4.isdisjoint(s3))