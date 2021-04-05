from controle.controladorsistema import ControladorSistema
from telas.telaenfermeiro import TelaEnfermeiro
from entidade.enfermeiro import Enfermeiro

class ControladorEnfermeiro():

    def __init__(self):
        self.__lista_enfermeiros = []

        self.__tela_enfermeiro = TelaEnfermeiro
        self.__controlador_sistema = ControladorSistema

    def incluir_enfermeiro(self, nome: str):

        novo_enfermeiro = None
        dados_enfermeiro = self.__tela_enfermeiro.cadastra_enfermeiro()
        if isinstance(dados_enfermeiro['nome'], str) and isinstance(dados_enfermeiro['idt'], int):
            
            novo_enfermeiro =  Enfermeiro(dados_enfermeiro['nome'], dados_enfermeiro['idt'])

            for enfermeiro in self.__lista_enfermeiros:
                if enfermeiro.nome == nome:
                    novo_enfermeiro = None
                    print('Esse enfermeiro já foi cadastrado')
            if novo_enfermeiro is not None:
                self.__lista_enfermeiros.append(novo_enfermeiro)
            return novo_enfermeiro

    def excluir_enfermeiro(self):

        enfermeiro_a_excluir = self.__tela_enfermeiro.excluir_enfermeiro()
        if isinstance(enfermeiro_a_excluir, Enfermeiro) and enfermeiro_a_excluir is not None:
            if enfermeiro_a_excluir in self.__lista_enfermeiros:
                self.__lista_enfermeiros.remove(enfermeiro_a_excluir)
            else:
                print ("Este enfermeiro não está cadastrado")
    
    def lista_enfermeiros(self):
        return self.lista_enfermeiros

    def abre_tela(self):

        lista_opcoes = {
            1: self.incluir_enfermeiro, 
            2: self.excluir_enfermeiro, 
            3: self.lista_enfermeiros
        }

        while True:
            opcao_escolhida = self.__tela_enfermeiro.tela_opcoes()

            funcao_escolhida = lista_opcoes[opcao_escolhida]

            funcao_escolhida()