



class TelaVacina():
    def __init__(self):
        pass


    def tela_vac(self):
        print('----- VACINA -----')
        print('ESCOLHA O NÚMERO DA OPÇÃO QUE DESEJA REALIZAR')
        print('1 - Cadastrar vacina')
        print('2 - Excluir vacina')
        print('3 - Lista de vacinas')
        print('0 - Retornar')

        opcao = int(input('Escolha a opção: '))
        return opcao

    def cadastra_vacina(self):
        print('Você escolheu cadastrar vacina')
        print('Preencha os campos a seguir')
        nome = input('Nome: ')
        fabricante = input('Fabricante: ')
        qtd_doses = input('Quantidade de doses: ')

        return {
            'nome': nome,
            'fabricante': fabricante,
            'qtd_doses': qtd_doses
        }

    def excluir_vacina(self):
        print('Você escolheu excluir vacina')
        print('Preencha o nome da vacina que deseja excluir do sistema')
        nome = input('Nome: ')

        return nome

    def lista_vacinas(self):
        print('Você escolheu ver doses disponíveis')