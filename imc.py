print('Programa de cálculo do imc peso/altura.altura')
peso=input('Qual é o seu peso? ')
altura=input('Qual é a sua altura? ')
imc=float(peso)/float(altura)*float(altura)
print('Seu IMC é de: ',imc)
if imc <=16:
    print('Magreza grave!')
elif imc >16.1 and imc <16.9:
    print('Magreza moderada!')
elif imc >=17 and imc <18.5:
    print('Magreza leve!')
elif imc >=18.6 and imc <24.9:
    print('Peso ideal!')
elif imc >=25 and imc <29.9:
    print('Sobrepeso!')
elif imc >=30 and imc <34.9:
    print('Obesidade grau 1!')
elif imc >=35 and imc <39.9:
    print('Obesidade grau 2!')
else :
    print('Obesidade morbida!')