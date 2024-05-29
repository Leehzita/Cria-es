letra=int
letra=0
palavra=str(input("Digite uma palavra: "))
letter=input("Digite uma letra que essa palavra possui: ")
for x in palavra:
    if x==letter:
        letra=letra+1
print(letra)