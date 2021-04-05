from entidade.enfermeiro import Enfermeiro
from entidade.paciente import Paciente

class Agendamento():

    def __init__(self, data: str, paciente: Paciente, enfermeiro: Enfermeiro):

        self.__data = data
        self.__enfermeiro = enfermeiro