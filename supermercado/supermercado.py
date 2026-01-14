class cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        
class produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        
 
class venda:
    def __init__(self, cliente, data_venda):
        self.nome_cliente = cliente
        self.data_venda = data_venda
        self.itens = [] 
        
    def adicionar_item(self , nome_produto):
        self.itens.append(produto)
        print(F"Produto'{produto.nome}'adicionar à venda.")
        
    def calcular_total(self):
        total = 0
        for produto in self.itens:
            total += produto.valor
            return total
            
    def resumo(self):
        print("/n--- RESUMO DA VENDA ---")    
        print(f"clinte:{self.cliente.nome}")
        print(f"CPF:{self.cliente.cpf}")
        print(f"Data da venda:{ self.data_venda}")
        print("Itens:")
        for p in self.itens:
            print(f"-{p.nome} | R$ {p.valor:2f}")
        print(f"Total de itens: {len(self.itens)}")
        print(f"Valor total: R${self.calcular.total():.2f} ")
        
venda = venda("Ryan Yure vaz vieira","073.066.323.02")

venda = venda(cliente,"03/12/2025")

produto1 = produto("Arroz", 7,50)
produto2 = produto("Detergente", 2,30)
produto3 = produto("Fita adesiva", 4,20)

 
venda.adicionar_item(produto1)
venda.adicionar_item(produto2)
venda.adicionar_item(produto3)

venda.resumo()
               