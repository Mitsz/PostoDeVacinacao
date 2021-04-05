



class TelaPaciente():

    def __init__(self):
        pass


    def cadastrar_paciente(self):
        print('Você escolheu cadastrar paciente')
        print('Preencha os campos a seguir')
        nome = input('Nome: ')
        idade = input('Idade: ')

        return {
            'nome': nome,
            'idade': idade
        }

    def excluir_paciente(self):
        print('Você escolheu excluir paciente')
        print('Preencha o nome do paciente que você deseja excluir do sistema')
        nome = input('Nome: ')

        return nome

    def lista_paciente(self):
        print('Você escolheu ver a lista de pacientes')

