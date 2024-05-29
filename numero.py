print("1 a 100")
for a in range(101):
    print(a)
print("Números pares (Forma #1)")
for a in range(2, 101, 2):
    print(a)
print("Números pares (Forma #2)")
for b in range(101):
    if (b%2==0):
        print(b)
print("Números ímpares (Forma #1)")
for a in range(3, 101, 3):
    print(a)
print("Números ímpares (Forma #2)")
for b in range(101):
    if (b%2!=0):
        print(b)