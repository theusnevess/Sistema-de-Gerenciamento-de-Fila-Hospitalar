class ElementoDaListaSimples:
    def __init__(self, numero, cor):
        self.numero = numero # número do cartão 
        self.cor = cor.upper() # cor do cartão convertido em letra maiúscula                              
        self.proximo = None # referência para o próximo elemento          

    def __repr__(self): # torna possível a impressão das instâncias dos nós(pacientes) em formato de string 
        return f"({self.cor} {self.numero})"

class ListaDeEspera:
    def __init__(self):                            
        self.head = None                                                                              
        self.contador_verde = 1   # a contagem do código númerico para pacientes com cartão verde se iniciam em 1
        self.contador_amarelo = 201 # para pacientes com o cartão amarelo, se iniciam em 201
                                                           
    def inserirSemPrioridade(self, nodo): # método para inserção de pacientes com cartão verde na fila, ou seja, pacientes sem prioridade de atendimento                   
        if self.head is None: # caso a lista esteja vazia, então o primeiro nó adicionado será o head                               
            self.head = nodo                                  
        else: 
            atual = self.head  
            while atual.proximo is not None: # percorrerá todos os nós da fila, até que o último nó aponte para None             
                atual = atual.proximo                   
            atual.proximo = nodo  # quando nó seguinte for None, então o nó adicionado como parâmetro será o nó subsequente do último nó da fila 

    def inserirComPrioridade(self, nodo):          
        if self.head is None:  # se a lista estiver vazia, o nó adicionado se torna o head                    
            self.head = nodo                       
        elif self.head.cor == 'V':                 
            nodo.proximo = self.head # se o parâmetro cor do head for verde, então o nó será inserido antes dela 
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None and atual.proximo.cor == 'A': # o loop irá percorrer toda a fila até que se chegue no último elemento com o atributo cor amarelo
                atual = atual.proximo  
            nodo.proximo = atual.proximo # fará a inserção do nó na posição correta
            atual.proximo = nodo

    def inserir(self):
        cor = input("Informe a cor do cartão (A/V): ").upper()  

        if cor not in ['A', 'V']: # verifica se o valor de entrada para a cor do cartão do paciente é verde ou amarelo, caso não seja então é impresso a mensagem de erro
            print("Cor do cartão inválida! Digite novamente")  
            return
        elif cor == "V": # caso o paciente adicionado tenha o cartão verde, então será acrescido 1 no contador verde
            numero = self.contador_verde
            self.contador_verde += 1 
        else: # caso o paciente adicionado tenha o cartão amarelo, então será acrescido 1 no contador amarelo      
            numero = self.contador_amarelo 
            self.contador_amarelo += 1

        nodo = ElementoDaListaSimples(numero, cor) # cria um novo nó, uma instância de um paciente 

        # decide a prioridade de inserção do paciente na fila com base na cor do cartão
        if self.head == None:
            self.head = nodo
        elif cor == "V": # caso a cor do cartão do paciente seja verde, então ele será inserido na fila sem prioridade no atendimento
            self.inserirSemPrioridade(nodo)
        elif cor == "A": # caso a cor do cartão seja amarelo, então o paciente seja adicionado na fila com prioridade
            self.inserirComPrioridade(nodo)

        print(f"Paciente com cartão {cor}{numero} adicionado a fila")
        

    def imprimirListaDeEspera(self):
        atual = self.head 
        filaEspera = [] # armazena os nós em uma lista para posterior impressão    
        while atual is not None: # percorre toda a lista 
            filaEspera.append(atual)
            atual = atual.proximo
        print("Lista ->", end=" ") # cada paciente da fila irá apontar para o paciente seguinte   
        for paciente in filaEspera:
            print(paciente, end=" -> ") # imprime cada paciente, em sequência, com base na prioridade de atendimento
        print("None", end=" ") # marca o final da lista, onde o último paciente irá apontar para None 
        print()   

    def atenderPaciente(self): 
        if self.head is None: # verifica se há pacientes na fila 
            print("Não há pacientes na fila para atender!")
            return
        else:                                 
            atual = self.head
            self.head = atual.proximo # remove o primeiro paciente da fila         

            print(f"Atendendo paciente cor {atual.cor} e número {atual.numero}.") # faz a chamada desse paciente para atendimento 

# ------------------------------------------------ MENU PRINCIPAL --------------------------------------------------------
fila = ListaDeEspera() # cria a instância da lista encadeada
while True:
    print('---------------------- SISTEMA HOSPITAL ----------------------') 
    print('1 - Adicionar paciente a fila')
    print('2 - Mostrar pacientes na fila')
    print('3 - Chamar paciente')
    print('4 - Fechar programa')

    escolha = int(input("Escolher: ")) # armazena na variável a escolha realizada pelo usuário 

    try:
        if escolha == 1:
            fila.inserir()
        elif escolha == 2:
            fila.imprimirListaDeEspera()
        elif escolha == 3: 
            fila.atenderPaciente()
        elif escolha == 4:
            print("Fechando programa...")
            break
        else: 
            print("Opção inválida! Tente Novamente")  
            continue  
    except ValueError: 
        print("Opção inválida! Digite um número entre 1 e 4")  
        continue       








    
              