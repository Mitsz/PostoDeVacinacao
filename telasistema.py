



class TelaSistema():
    def __init__(self):
        pass


    def tela_opcoes(self):
        print('----- POSTO DE VACINAÇÃO -----')
        print('ESCOLHA O NÚMERO DA OPERAÇÃO QUE DESEJA REALIZAR')
        print('1 - Cadastrar vacina')
        print('2 - Cadastrar paciente')
        print('3 - Cadastrar enfermeiro')
        print('0 - Sair do programa')

        opcao = int(input('Escolha a opção: '))
        return opcao 