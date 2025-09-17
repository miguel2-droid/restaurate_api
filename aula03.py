class ContaBancaria:
    def __init__(self, numero, titular, saldo):
        self.numero = numero 
        self._saldo = saldo
        self._titular = titular

    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def saldo(self):
        return self._saldo

    def saque(self, valor):
        self._saldo -= valor

    def deposito(self, valor):
        if valor <= self._saldo:
            self._saldo += valor
        else:
            print("valor invalido")    

    def __str__(self):
        return f"Conta de {self._titular}: {self._saldo}"

conta = ContaBancaria("65425", "titular", 500)

print(conta)
conta.deposito(10)
print(conta)
conta.saque(10)
print(conta)
conta.deposito(10)
print(conta)
conta.saque(10)
print(conta) 