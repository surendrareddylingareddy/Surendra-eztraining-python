L = [2**i for i in range(1,10)]
print(L)

L1 = ["hyd","vizag","chennai","vijayawada"]
city = []
for i in L1:
    if "v" not in i:
        city.append(i)
print(city)

L2 = [i for i in range(100,201,20)]
print(L2)
