from telas.telaagendamento import TelaAgendamento
from controle.controladorpaciente import ControladorPaciente
from entidade.paciente import Paciente
from controle.controladorenfermeiro import ControladorEnfermeiro
from entida.enfermeiro import Enfermeiro

class ControladorAgendamento():

    def __init__(self):
        self.__tela_agendamento = TelaAgendamento
        self.__lista_de_agendamentos = []


    def agendar(self):

        novo_agendamento = None
        dados_agendamento = self.__tela_agendamento.cadastra_agendamento()

        if(isinstance(dados_agendamento[paciente], Paciente)
        and isinstance(dados_agendamento[enfermeiro], Enfermeiro)
        and isinstance(dados_agendamento[data], list)
        ):
            
