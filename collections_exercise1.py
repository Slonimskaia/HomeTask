a = [1,3,5]
b = [2,4,6]
c = (a + b)
d = sorted(c)
d.reverse()
c.insert(3,42)
d.append(10)
c.extend([7,8,9])
print(c[:3])
print(d[-1])# = print(d[6:])
print(len(d))