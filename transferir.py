class Conta:
    def __init__(self,titular,saldo):
        self.cliente = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True 
        return False
    
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return True
        return False
    
    def transferir(self, valor, conta_destino):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            return True
        return False

conta_a = Conta("Ariel", 100)
conta_b = Conta("Ryan", 500)

print(conta_a.cliente)
conta_a.depositar(200)
print(conta_a.saldo)

conta_a.transferir(100, conta_b)
print(conta_a.saldo)
print(conta_b.saldo)