# Classe pai
class Veículo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._velocidade = 0 # privado por convenção

        def acelerar(self):
            self._velocidade += 10
            return f"Velocidade: {self._velocidade} km/h"
        
# Classe filha Carro 
class Carro(Veículo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo) 
        self.portas = portas

        # Polimorfismo (sobrescrita do método)
        def acelerar(self):
            self._velocidade += 20
            return f"Carro acelerando: {self._velocidade} km/h"

# Classe filha Moto
class Moto(Veículo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo) 
        self.cilindradas = cilindradas

        # Polimorfismo (sobrescrita do método)
        def acelerar(self):
            self._velocidade += 30
            return f"Moto acelerando: {self._velocidade} km/h"

# Criando objetos
veículo = Veículo ("Genérica", "X")
carro = Carro ("Toyota", "Corolla", 4)
moto = Moto ("Yamaha", "R15", 150)

# Testando polimorfismo
print(veículo.acelerar())  # +10
print(carro.acelerar())    # +20
print(moto.acelerar())     # +30

#---------------------------------------------------------------------------------------------------------------------

# Uma versão usando o @property para controlar melhor o acesso a velocidade

# Classe pai 
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._velocidade = 0 # atributo "protegido"

    @property
    def velocidade (self):
        return self._velocidade
    
    @velocidade.setter
    def velocidade(self, valor):
        if valor < 0:
            raise ValueError("A velocidade não pode ser negativa")
        self._velocidade = valor

    def acelerar(self) 
        self._velocidade +=10
        return f"Velocidade: {self.velocidade} km/h"

# Classe filha Carro 
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo) 
        self.portas = portas

    def acelerar(self):
        self.velociade += 20
        return f"Carro acelerando {self.velocidade} km/h"

# Classe filha Moto 
class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo) 
        self.cilindradas = cilindradas

    def acelerar(self):
        self.velociade += 30
        return f"Moto acelerando {self.velocidade} km/h"

# Criando objetos
veículo = Veículo ("Genérica", "X")
carro = Carro ("Toyota", "Corolla", 4)
moto = Moto ("Yamaha", "R15", 150)

# Testando 
print(veículo.acelerar())  
print(carro.acelerar())    
print(moto.acelerar())     

# Teste de validação
# carro.velocidade = -50 
# Vai gerar erro
        


     