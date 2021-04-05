from entidade.vacinas import Vacina
from controle.controladorsistema import ControladorSistema
from telas.telavacina import TelaVacina


class ControladorVacina():

    def __init__(self):
        self.__lista_vacinas: []

        self.__tela_vacinas = TelaVacina()
        self.__controlador_sistema = ControladorSistema()
    
    def incluir_vacinas(self, nome: str, fabricante: str, qtd_doses: int) -> Vacina:

        dados_vacina = self.__tela_vacinas.cadastra_vacina()
        nova_vacina = None
        if(
            isinstance(dados_vacina['nome'], str) 
            and isinstance(dados_vacina['fabricante'], str) 
            and isinstance(dados_vacina['qtd_doses'], int)
        ):
            nova_vacina =  Vacina(dados_vacina['nome'], dados_vacina['fabricante'], dados_vacina['qtd_doses'])

            for vacina in self.__lista_vacinas:
                if vacina.nome == nome:
                    nova_vacina = None
            if nova_vacina is not None:
                self.__lista_vacinas.append(nova_vacina)
            return nova_vacina
    
    def excluir_vacina(self, vacina: Vacina):

        vacina_a_excluir = self.__tela_vacinas.excluir_vacina()
        if isinstance(vacina_a_excluir, Vacina) and vacina_a_excluir is not None:
            if vacina_a_excluir in self.__lista_vacinas:
                self.__lista_vacinas.remove(vacina_a_excluir)
            else:
                print("Esta vacina não está cadastrada")
    
    def doses_disponiveis(self, vacina: Vacina):
    
        if isinstance(vacina, Vacina) and vacina is not None:
            for vacina in self.__lista_vacinas:
                return vacina.qtd_doses

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_vacinas,
            2: self.excluir_vacina,
            3: self.doses_disponiveis
        }

        while True:
            opcao_escolhida = self.__tela_vacinas.tela_vac()

            funcao_escolhida = lista_opcoes[opcao_escolhida]

            funcao_escolhida()
