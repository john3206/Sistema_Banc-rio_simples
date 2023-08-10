



        #Menu visual

menu = """
         __________________
         BEM VINDO AO BANCO
         __________________

         |################|
         | [1]- Sacar     |            
         | [2]- Depositar |        
         | [3]- Extrato   |          
         | [0]- Sair      |
         |################|

=> """

        #Variáveis 

extrato = "";
saldo = 0;
limite = 500;
LIMITE_DE_SAQUE = 3;
NUMERO_DE_SAQUE = 0;

        #Comando de repetição

while True:

      
        # Inicio do atendimento


        opcao = input(menu);
     
        #Realizando depósito

        if (opcao == "2"):
                valor = float(input("Digite o valor para depósito:"));
                
                if valor > 0:
                        saldo += valor;
                        extrato += f"deposito: R$ {valor:.2f}\n"; 
                else:
                        print("Operação falhou! O valor informado é inválido");       


        #Realizando saque

        elif (opcao == "1"):
                valor = float(input("Digite o valor desejado:"));
       
                excedeu_saldo = valor > saldo;

                excedeu_limite = valor > limite;

                excedeu_saques = NUMERO_DE_SAQUE >= LIMITE_DE_SAQUE;

                if excedeu_saldo:
                        print("Falha na operação, Saldo insuficiente");

                elif excedeu_limite:
                        print("Operação falhou, o valor do saque excedeu o limite");

                elif excedeu_saques:
                        print("Operação falhou, número máximo de saques excedido");

                elif valor > 0:
                     saldo -= valor;
                     extrato += f"saque: R$ {valor:.2f}\n";
                     NUMERO_DE_SAQUE += 1;

                else:
                        print("Operação falhou! O valor informado é inválido");

        #Visualizando o extrato

        elif opcao == "3":
                print("\n########## Extrato #########");
                print("\nNão foram realizadas movimentações." if not extrato else extrato);
                print(f"\nsaldo: R$ {saldo:.2f}");
                print("\n############################");

        #opção de sair

        elif opcao == "0":
                break;

        else:
                print("Operação inválida, por favor selecione novamente a opção desejada:");





       
        

                

