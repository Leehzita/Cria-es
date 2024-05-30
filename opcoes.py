print('1) Suporte 2) Comercial 3) Falar com o atendente')
menu=int(input('Digite um número de 1 a 3: '))
match menu:
    case 1:
        print('1) Banda larga 2) Celular') 
        menu=int(input('Digite um número entre 1 e 2: '))
        match menu:
            case 1:
                print('1) Sem internet 2) Internet lenta')
                menu=int(input('Digite um número entre 1 e 2: '))
                match menu :
                    case 1:
                        print('Reinicie seu modem')
            case 2:
                print('1) Sem sinal 2) Bloqueado')
                menu=int(input('Digite um número entre 1 e 2: '))