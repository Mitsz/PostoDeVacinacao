from abc import ABC, abstractmethod

class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome: str, idade: int, idt: int):
        if isinstance(nome, str):
            self.__nome = nome

        if isinstance(idade, int):
            self.__idade = idade

        if isinstance(idt, int):
            self.__idt = idt
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        if isinstance(idade, int):
            self.__idade = idade

    @property
    def idt(self):
        return self.__idt

    @idt.setter
    def idt(self, idt: int):
        if isinstance(idt, int):
            self.__idt = idt