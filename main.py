selecao = int(input("Escolha o exercicio [1..6]:"))

# exercicio01
if selecao == 1:
    Nota = int(input("Digite uma nota entre zero e dez"))
    while Nota < 0 or Nota > 10:
        Nota = int(input("Digite com uma nota válida entre zero e dez"))
    print("Sua Nota:")
    print(Nota)
    print("Fim do exercicio 01")

# exercicio02
if selecao == 2:
    Nome = (input("Digite o nome:"))
    Senha = (input("Insira sua senha"))
    while Nome == Senha:
        Senha = (input("Insira sua senha diferente do nome"))
    print("Nome: " + Nome + "\tSenha: " + Senha)

    print("Fim do exercicio 01")

# exercicio03
if selecao == 3:
    Nome02 = input("Digite seu nome")
    if len(Nome02) < 3:
        Nome02 = input("Seu nome deve ter ao menos 3 caracteres")
    print("Seu nome eh:" + Nome02)
    Idade = int(input("Qual sua idade?"))
    if Idade <= 0 or Idade >= 150:
        Idade = int(input("Entre com uma idade valida:"))
    print(Idade)
    Salario = float(input("Informe seu salario"))
    if Salario >= 0:
        print(Salario)
    else:
        while Salario < 0:
            Salario = float(input("Insira um salario maior que zero"))
        print(Salario)
    Sexo = input("Qual seu genero? [f] ou [m]")
    if Sexo == "f":
        print("Feminino")
    else:
        print("Masculino")
    Estado_civil = input("Informe seu estado civil [s,c,v,d]")
    if Estado_civil == "s":
        print("Solteiro")
    elif Estado_civil == "s":
        print("Casado")
    elif Estado_civil == "v":
        print("Viuvo")
    elif Estado_civil == "d":
        print("Divorciado")
    print("Fim do exercicio 03")
# Exercicio 04
if selecao == 4:
    Texto = input("Digite um texto:")
    print("O tamanho do texto eh:")
    print(len(Texto))
    print("Fim do exercicio 04")
# Exercicio 05
if selecao == 5:
    PaisA = 80000  # crecimento de 3% ao ano
    PaisB = 200000  # crescimento 1,5% ao ano
    TaxaA = 0.03
    TaxaB = 0.015
    Anos = 0

    while (PaisA<PaisB):
        Anos += 1
        PaisA = PaisA+(PaisA * TaxaA)
        PaisB = PaisB+(PaisB * TaxaB)
    print(Anos)
    print("Fim do exercicio 05")

#Exercicio 06
if selecao ==6:

  PaisA = int(input("Informe o numero de habitantes do Pais A ou insira [-1] para sair:"))
  while PaisA != -1:
    PaisB = int(input("Informe o numero de habitantes do Pais B"))
    TaxaA = float(input("Informe a taxa de crescimento anual do Pais A"))
    TaxaB = float(input("Informe a taxa de crescimento anual do Pais B"))
    Anos = 0

    while (PaisA<PaisB):
        Anos += 1
        PaisA = PaisA+(PaisA * TaxaA)
        PaisB = PaisB+(PaisB * TaxaB)
    print(Anos)
    print("Fim do exercicio 06")
print(" ---------------------------------------------------------------------------------")
print("Obrigado")
