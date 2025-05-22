filmeslista=[]
sessaolista=[]  
clientelista=[]

class Filme:
    def __init__(self,titulo,duracao,classificacao,indicativa):
        self.titulo=titulo
        self.duracao=duracao
        self.classificacao=classificacao
        self.indicativa=indicativa

    def ExibirInf(self):
        print(f"\nTítulo: {self.titulo}\nDuração: {self.duracao} Min.\nClassificação: {self.classificacao}\nIndicativa: {self.indicativa}")


class Sessao:
    def __init__(self,filme='',horario='',assentosdisponiveis=0):
        self.filme=filme
        self.horario=horario
        self.assentosdisponiveis=assentosdisponiveis

    def ExibirSessao(self):
        print(f"\nFilme: {self.filme}\nHorário: {self.horario}\nAssentos Disponiveis: {self.assentosdisponiveis} Restantes")

    
    #metodo para venda de ingressos
    def vender_ingresso(self, quantidade):
        if quantidade <= self.assentosdisponiveis:
            self.assentosdisponiveis -= quantidade
            print(f"Ingressos vendidos: {quantidade}")
            print(f"Ingressos restantes: {self.assentosdisponiveis}")
        else:
            print("Quantidade de ingressos insuficiente!")

    def ingressos_restantes(self):
        return self.assentosdisponiveis


class Cliente:
    def __init__(self, nome, nif, ingressosComprados):
        self.nome = nome
        self.nif = nif
        self.ingressosComprados = ingressosComprados

    def ExibirCliente(self):
        print(f"\nNome: {self.nome}\nNIF: {self.nif}\nIngressos Comprados: {self.ingressosComprados}")


class Cinema:
    def __init__(self,listadeSessoes):
        self.listadeSessoes=listadeSessoes
#Criar sessões e adiciona na lista de sessões
def Sessoesfilme():
   
    filme=str(input("\nFilme: "))
    horario=input("Horário: ")
    assentosdisponiveis=int(input("Total de assentos: "))

 
    todasSessoes=Sessao(filme,horario,assentosdisponiveis)
    
    sessaolista.append(todasSessoes)
#Adiciona filme a lista de filmes
def AddFilmes():
    while True:
        titulo=str(input("\nTitulo: "))
        duracao=input(f"Duração: ")
        classificacao=input("Classificação: ")
        indicativa=input("Indicativa: ")

        todosfilme=Filme(titulo,duracao,classificacao,indicativa)
        filmeslista.append(todosfilme)

        Sessoesfilme()
        break
#Compra de ingresso
def ComprarIngressos():
    if not sessaolista:
        print("Nenhuma sessão cadastrada.")
        return

    print("\nSessões disponíveis:")
    for i, sessao in enumerate(sessaolista):
        print(f"{i + 1} - {sessao.filme} às {sessao.horario} ({sessao.assentosdisponiveis} assentos disponíveis)")

    escolha = int(input("Escolha o número da sessão desejada: ")) - 1

    if 0 <= escolha < len(sessaolista):
        sessao_escolhida = sessaolista[escolha]
        nome = input("\nNome: ")
        nif = int(input("NIF: "))
        ingressoscomprados = int(input("Quantidade de ingressos a comprar: "))

        if sessao_escolhida.assentosdisponiveis >= ingressoscomprados:
            sessao_escolhida.vender_ingresso(ingressoscomprados)
            cliente = Cliente(nome, nif, ingressoscomprados)
            clientelista.append(cliente)
        else:
            print("Não há ingressos suficientes.")
    else:
        print("Sessão inválida.")





def Menu():
    op=int(input("\n\n\n1-Adicionar filmes e sessões novas\n2-Listar sessões disponíveis\n3-Comprar ingresso para uma sessão\n4-Mostrar ingressos de um cliente\nAguardando: "))
    if op==1:
        AddFilmes()
        op=int(input("1 - Voltar ao Menu | 0 - Encerrar o programa\nAguardando: "))
        if op==1:
            Menu()
        else:
            print("Encerrando...")

    if op==2:
        print("\nTodas as Sessões Disponiveis:")
        for sessao in sessaolista:
            sessao.ExibirSessao()
        op=int(input("1 - Voltar ao Menu | 0 - Encerrar o programa\nAguardando: "))
        if op==1:
            Menu()
        else:
            print("Encerrando...")

    if op==3:
        ComprarIngressos()
        Menu()

    if op==4:
        print("\nIngressos dos cliente:")
        for cliente in clientelista:
            cliente.ExibirCliente()
        op=int(input("1 - Voltar ao Menu | 0 - Encerrar o programa\nAguardando: "))
        if op==1:
            Menu()
        else:
            print("Encerrando...")
print("\n\n\n\nBEM VINDO AO CINEMA ACT\n(Escolha uma das opções do menu a seguir)\n-----------------------------------------------")           
Menu()

