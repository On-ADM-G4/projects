import mysql.connector
from time import sleep
from login import User

try:

    conexao = mysql.connector.connect(
     host='localhost',
     database='db_property',
     user='root',
     password='root')

    if conexao.is_connected():
        
        db_info = conexao.get_server_info()
        print(f'\nCONECTADO AO MySQL VERSÃO: {db_info}')
        cursor = conexao.cursor()
        cursor.execute('select database();')
        linha = cursor.fetchone()
        print(f'\nCONECTOU À BASE: {linha}')
        User()
        

except:

        print('A CONEXÃO NÃO FOI FEITA')

def repetidor():

        escolha = str(input('\n DESEJA VOLTAR AO MENU DE OPÇÕES? S/N: ')).lower()

        if escolha == 's':

                print('\n...')
                sleep(2)
                start()
        if escolha == 'n':

                sleep(1)
                print('\n# PROGRAMA ENCERRADO #')
                cursor.close()
                conexao.close()
                exit()

def visualizador():

        gerenciar_dados = '''SELECT * FROM db_property.tb_login'''
        cursor.execute(gerenciar_dados)
        linhas = cursor.fetchall()
        print(f'\n{cursor.rowcount} REGISTROS ENCONTRADOS\n')

        for linha in linhas:
                print(f'ID: {linha[0]} - USUÁRIO: {linha[1]} - SENHA: {linha[2]}')
        repetidor()


def start():

        print('''
# 1 - ADCIONAR DADOS AO BANCO
# 2 - REMOVER DADOS REGISTRADOS PELO ID(NÚMERICO)
# 3 - VISUALIZAR TODOS OS DADOS REGISTRADOS
# 4 - ATUALIZE SUA SENHA
# 5 - ATUALIZE SEU USUÁRIO
# 6 - DESCRIBE (VER INFORMAÇÕES SOBRE OS VALORES)
        ''')

        escolha = int(input('O QUE DESEJA FAZER? '))

        if escolha == 1:
                adicionar_dados()
        if escolha == 2:
                delete()
        if escolha == 3:
                visualizador()
        if escolha == 4:
                atualizar_senha()
        if escolha == 5:
                atualizar_user()
        if escolha == 6:
                descricao()

def delete():

        deletar = int(input('\nDESEJA DELETAR A LINHA DE QUAL ID? DIGITE UM NÚMERO: '))
        deletando_dados = f'''DELETE FROM db_property.tb_login WHERE ID={deletar}'''
        cursor.execute(deletando_dados)
        conexao.commit()
        print(f'\n{cursor.rowcount} DADOS DELETADOS')
        repetidor()

def adicionar_dados():

        gerenciar_dados = '''SELECT USUARIO FROM db_property.tb_login'''
        cursor.execute(gerenciar_dados)
        linhas = cursor.fetchall()

        usuario = str(input('\nDIGITE UM NOME DE USUARIO: ')).lower()

        for linha in linhas:
                if linha[0] == usuario:
                        print('\n# ESTE USUÁRIO JÁ EXISTE #')
                        adicionar_dados()

        print('\n# SENHA COM MAXIMO DE 8 DIGITOS #')
        senha = int(input('\nCRIE SUA SENHA NUMERICA: '))

        inserir_dados = f'''INSERT INTO db_property.tb_login(USUARIO, SENHA) 
                                VALUES {usuario, senha};'''

        cursor.execute(inserir_dados)
        conexao.commit()
        print(f'\n{cursor.rowcount} DADOS FORAM INSERIDOS')
        repetidor()

def atualizar_user():

        user = str(input('\nQUAL O SEU USUÁRIO? '))
        user_novo = str(input('\nQUAL O NOVO NOME DE USUÁRIO QUE DESEJA REGISTRAR? '))
        att_user = f'''UPDATE db_property.tb_login SET USUARIO = '{user_novo}' WHERE USUARIO = '{user}' '''
        cursor.execute(att_user)
        conexao.commit()
        print(f'\n{cursor.rowcount} DADO FOI ATUALIZADO')
        repetidor()

def atualizar_senha():

        senha = int(input('\nQUAL A SUA SENHA? '))
        senha_nova = int(input('\nQUAL A NOVA SENHA QUE DESEJA REGISTRAR? '))

        att_senha = f'''UPDATE db_property.tb_login SET SENHA = {senha_nova} WHERE SENHA = {senha} '''
        cursor.execute(att_senha)
        conexao.commit()
        print(f'\n{cursor.rowcount} DADO FOI ATUALIZADO')
        repetidor()

def descricao():

        desc = '''DESCRIBE db_property.tb_login;'''
        cursor.execute(desc)
        resul = cursor.fetchall()
        print()
        for linha in resul:
            print(f'{linha[0]} {linha[1]} {linha[2]}')

start()

''' if conexao.is_connected():
        cursor.close()
        conexao.close()
        print('\nA CONEXÃO AO MySQL FOI ENCERRADA') '''