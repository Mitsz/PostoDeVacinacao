from controle.controladorsistema import ControladorSistema
from telas.telapaciente import TelaPaciente
from entidade.paciente import Paciente

class ControladorPaciente():

    def __init__(self, controlador_sistema):
        self.__lista_pacientes = []

        self.__tela_paciente = TelaPaciente()
        self.__controlador_sistema = controlador_sistema

    def incluir_pacientes(self, nome: str, idade: int):

        novo_paciente = None
        dados_paciente = self.__tela_paciente.excluir_paciente()
        if isinstance(dados_paciente['nome'], str) and isinstance(dados_paciente['idade'], int):
            
            novo_paciente =  Paciente(dados_paciente['nome'], dados_paciente['idade'])

            for paciente in self.__lista_pacientes:
                if paciente.nome == nome:
                    novo_paciente = None
            if novo_paciente is not None:
                self.__lista_pacientes.append(novo_paciente)
            return novo_paciente

    def excluir_pacientes(self, paciente: Paciente):

        paciente_a_excluir = self.__tela_paciente.excluir_paciente()
        if isinstance(paciente_a_excluir, Paciente) and paciente_a_excluir is not None:
            if paciente_a_excluir in self.__lista_pacientes:
                self.__lista_pacientes.remove(paciente_a_excluir)
            else:
                print ("Este paciente não está cadastrado")
    
    def lista_pacientes(self):
        return self.__lista_pacientes

    def abre_tela(self):

        lista_opcoes = {
            1: self.incluir_pacientes, 
            2: self.excluir_pacientes, 
            3: self.lista_pacientes
        }

        while True:
            opcao_escolhida = self.__tela_paciente.tela_opcoes()

            funcao_escolhida = lista_opcoes[opcao_escolhida]

            funcao_escolhida()
