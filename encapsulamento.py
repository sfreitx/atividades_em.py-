class Funcionário: 
    def __init__(self, nome, salario):
      self.__nome = nome 
      self.__salario = salario 

    def obter_nome(self):
      return self.__nome 

    def obter_salario(self): 
      return self.__salario 

    def alterar_salario(self, novo_salario): 
      if novo_salario > 0: 
        self.__salario = novo_salario 

      else: 
          print("Erro: O salário deve ser maior que zero.")