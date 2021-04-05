from tela.telasistema import TelaSistema
from controlador.controladorvacina import ControladorVacina
from controlador.controladorpacientes import ControladorPaciente
from controlador.controladorenfermeires import ControladorEnfermeire



class ControladorSistema():
    
    def __init__(self):
        self.__controlador_enfermeire = ControladorEnfermeire()
        self.__controlador_paciente = ControladorPaciente()
        self.__tela_sistema = TelaSistema()
        self.__controlador_vacina = ControladorVacina()


    def iniciar_sistema(self):
        self.abre_tela()

    def encerrar_sistema(self):
        exit(0)

    def cadastra_vacina(self):
        self.__controlador_vacina.abre_tela()

    def cadastra_paciente(self):
        self.__controlador_paciente.abre_tela()

    def cadastra_enfermeire(self):
        self.__controlador_enfermeire.abre_tela()

    def agendamento(self):
        self.__controlador_agendamento.abre_tela()


    def abre_tela(self):

        lista_opcoes = {
            1: self.cadastra_vacina,
            2: self.cadastra_paciente,
            3: self.cadastra_enfermeire,
            0: self.encerrar_sistema,
        }

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()

            funcao_escolhida = lista_opcoes[opcao_escolhida]

            funcao_escolhida()




