print("1) Dizer suporte 2) Dizer comercial 3) Dizer falar com o atendente")
menu = int(input("Dizer uma opção:"))
match menu: 
    case 1:
        print("1) Banda larga 2) celular")
        menu2 = int(input("digite uma opção:"))
        match menu2:
            case 1:
                print("1) Sem internet 2) Internet lenta")
                menu3  = int(input("digite uma opção"))
                match menu3 :
                    case 1:
                        print("reinicie seu modem")
                    case 2:
                        print("reinicie seu modem")
            case 2: 
                print("1) sem sinal 2) ") 
                        