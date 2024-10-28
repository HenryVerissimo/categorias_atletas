from time import localtime, strftime

pergunta = str(input("Deseja saber a categoria de um atleta? (sim/não) ").strip().lower())

dataAtual = localtime()
anoAtual = strftime("%Y", dataAtual)

while pergunta not in "nao não":
    if pergunta == "sim":
        while True:
            try:
                ano = int(input("Digite o ano de nascimento do atleta: ").strip())
                if ano >= 0:
                    while True:
                        confirmacao = str(input(f"O ano {ano} está certo? (sim/não) ").strip().lower())
                        if confirmacao == "sim":
                            break
                        elif confirmacao == "nao" or confirmacao == "não":
                            print("\nDigite novamente...\n")
                            ano = int(input("Digite o ano de nascimento do atleta: ").strip())
                        else:
                            print("\n\033[1;31mVocê precisa digitar sim ou não!\033[m\n")
                    break 
                else:       
                    print("\n\033[1;31mNingém nasce em anos negativos!\033[m\n")
            except ValueError:
                print("\n\033[1;31mAlgo deu errado! Você precisa digitar um ano!\033[m\n")

        while True:
            aniversario = str(input("O atleta já fez aniversário esse ano? (sim/não) ").lower().strip())
            if aniversario == "sim":
                break
            elif aniversario == "nao" or aniversario == "não":
                break
            else:
                print("\n\033[1;31mVocê precisa digitar sim ou não!\033[m\n")
        if aniversario == "sim":
            idade = int(anoAtual) - ano
        else:
            idade = (int(anoAtual) - ano) - 1

        if idade <= 9:
            print(f"O atleta tem {idade} anos, por tanto é da categoria \033[1;33mMIRIM!\033[m")
        elif idade > 9 and idade <= 14:
            print(f"O atleta tem {idade} anos, por tanto é da categoria \033[1;33mINFANTIL!\033[m")
        elif idade > 14 and idade <= 19:
            print(f"O atleta tem {idade} anos, por tanto é da categoria \033[1;33mJUNIOR!\033[m")
        elif idade > 19 and idade <= 20:
            print(f"O atleta tem {idade} anos, por tanto é da categoria \033[1;33mSÊNIOR!\033[m")
        else:
            print(f"O atleta tem {idade} anos, por tanto é da categoria \033[1;33mMASTER!\033[m")
            
    else:
        print("\n\033[1;31mVocê precisa digitar sim ou não!\033[m\n")

    print(100 * "-")
    pergunta = str(input("Deseja saber a categoria de um atleta? (sim/não) ").strip().lower())

print("\033[1;32mPrograma finalizado!\033[m")