class Registro:
    def __init__ (self):
        self.nome="Lucas"
        self.cpf=50885168871
        self.rg=50885168871
        self.endereço="av Rudge, 315"

    def validacao(self):
        if self.cpf!=self.rg:
            return True
        else:
            return False

cadastro=Registro()
print("Validação para Cpf e Rg válidos ou inválidos...",cadastro.validacao())
print(cadastro.nome)
print(cadastro.cpf)
print(cadastro.rg)
print(cadastro.endereço)