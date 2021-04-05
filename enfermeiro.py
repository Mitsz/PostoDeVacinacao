class Enfermeiro():

    def __init(self, nome: str, idt: int):
        if isinstance(nome, str):
            self.__nome = nome

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
    def idt(self):
        return self.__idt

    @idt.setter
    def idt(self, idt: int):
        if isinstance(idt, int):
            self.__idt = idt