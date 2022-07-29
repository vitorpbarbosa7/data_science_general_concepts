import numpy as np

arr1 = np.array(np.random.normal(loc = 0, scale = 1, size = 100))
arr2 = np.array(np.random.normal(loc = 0, scale = 1, size = 100))

a = [1,2,3,4,5,6,7,8,9]
b = [4,5,6,5,6,6,7,8,9]

c = [1,2,3,4,5,6,7]
d = [9,7,6,5,4,3,2]


norm_a = np.linalg.norm(a)
norm_b = np.linalg.norm(b)
norm_c = np.linalg.norm(c)
norm_d = np.linalg.norm(d)

unit_a = a/norm_a
unit_b = b/norm_b
unit_c = c/norm_c
unit_d = d/norm_d

print(f"Norm a: {norm_a}")
print(f"Norm b: {norm_b}")
print(f"Norm c: {norm_c}")
print(f"Norm d: {norm_d}")

print("\n")

print(f"a b dot product {np.dot(a,b)}")
print(f"c d dot product {np.dot(c,d)}")

print("\n")

print(f"a b dot product normalized {np.dot(unit_a, unit_b)}")
print(f"c d dot product normalized {np.dot(unit_c, unit_d)}")



