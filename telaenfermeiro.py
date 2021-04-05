



class TelaEnfermeiro():
    def __init__(self):
        pass

    def tela_enf(self):
        print('----- ENFERMEIROS -----')
        print('ESCOLHA O NÚMERO DA OPERAÇÃO QUE DESEJA REALIZAR')
        print('1 - Cadastrar enfermeiro')
        print('2 - Excluir enfermeiro')
        print('3 - Lista de enfermeiros')
        print('0 - Retornar')

        opcao = int(input('Escolha a opção: '))
        return opcao


    def cadastra_enfermeiro(self):
        print('Você escolheu cadastrar enfermeiro')
        print('Preencha as informações a seguir')
        nome = input('Nome: ')
        idt = input('Identidade: ')

        return {
            'nome': nome,
            'idt': idt
        }

    def excluir_enfermeiro(self):
        print('Você escolheu excluir enfermeiro')
        print('Preencha a identidade do enfermeiro que deseja excluir do sistema')
        idt = input('Identidade: ')

        return idt

    def lista_enfermeiros(self):
        print('Você escolheu ver a lista de enfermeiros')