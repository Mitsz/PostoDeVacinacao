from abc import ABC, abstractmethod
from pessoa import Pessoa

class Paciente():

 #   @abstractmethod
 #   def __init__ (self, nome: str, idade: int):
 #      super().__init__(nome, idade)

    def __init__ (self, nome: str, idade: int):

        if isinstance(nome, str):
            self.__nome = nome
        
        if isinstance(idade, int):
            self.__idade = idade
    
    @property
    def nome(self):
        return self.__nome