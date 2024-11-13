import oracledb
import json
 
menu_opcoes = [
    '[1] - Fontes',
    '[2] - Emissões',
    '[3] - Regiões',
    '[4] - Projetos',
    '[5] - Exportar Dados para JSON',
    '[6] - Sair'
]
 
sub_opcoes = [
    '[1] - Inserir',
    '[2] - Consultar',
    '[3] - Atualizar',
    '[4] - Deletar'
]
 
 
def get_connection():
    try:
        connection = oracledb.connect('rm557137/020106@oracle.fiap.com.br:1521/orcl')
        print('Conectado com o Oracle DB')
    except Exception as e:
        print(f'error obtaining a conncetion: {e}')
    return connection
 
def exportar_dados_para_json():
    try:
        connection = get_connection()
        cursor = connection.cursor()
       
 
        tabelas = ["tipo_fontes", "emissoes_carbono", "regioes_sustentaveis", "projetos_sustentaveis"]
        dados = {}
 
        for tabela in tabelas:
            cursor.execute(f"SELECT * FROM {tabela}")
            colunas = [col[0] for col in cursor.description]
            registros = cursor.fetchall()
            dados[tabela] = [dict(zip(colunas, registro)) for registro in registros]
 
 
        with open('dados_exportados.json', 'w') as json_file:
            json.dump(dados, json_file, indent=4)
        print("Dados exportados com sucesso para 'dados_exportados.json'")
   
    except Exception as e:
        print(f"Ocorreu um erro ao exportar os dados: {e}")
    finally:
        cursor.close()
        connection.close()
 
 
def inserir_fonte_banco(fonte):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = """
            INSERT INTO tipo_fontes (id_tipo_fonte, nome)
            VALUES(:id_tipo_fonte, :nome)
        """
        cursor.execute(sql, {
            'id_tipo_fonte': fonte['id_tipo_fonte'],
            'nome': fonte['nome']
        })
        connection.commit()
        print('Dados da fonte inseridos com sucesso.')
    except Exception as e:
        print(f'Ocorreu um erro ao inserir os dados da fonte: {e}')
 
 
def inserir_fonte():
    id_tipo_fonte = int(input('Digite o ID do Tipo de Fonte: '))
    nome = input('Digite o nome do tipo de fonte de energia: ')
    dados = {
        'id_tipo_fonte': id_tipo_fonte,
        'nome': nome
    }
    inserir_fonte_banco(dados)
 
 
 
def consultar_fonte_banco():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = "SELECT * FROM tipo_fontes"
        cursor.execute(sql)
        fontes = cursor.fetchall()
        for fonte in fontes:
            print("Fonte:", fonte)
    except Exception as e:
        print(f"Erro ao consultar {e}")
 
def atualizar_fonte_banco(id_tipo_fonte,dados_novos):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = """
            UPDATE tipo_fontes
            SET nome = :nome
            WHERE id_tipo_fonte = :id_tipo_fonte
        """
        dados_novos['id_tipo_fonte'] = id_tipo_fonte
        cursor.execute(sql, dados_novos)
        connection.commit()
        print("Os dados foram atualizados")
    except Exception as e:
        print(f"Ocorreu um erro ao atualizar os dados: {e}")
    finally:
        cursor.close()
        connection.close()
 
def atualizar_fonte():
    id_tipo_fonte = int(input('Digite o ID'))
    nome = input('Digite a emissao: ')
    dados = {
        "nome": nome
    }
    atualizar_fonte_banco(id_tipo_fonte,dados)
 
def deletar_fonte_banco(id_tipo_fonte):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = "DELETE FROM tipo_fontes WHERE id_tipo_fonte = :id_tipo_fonte"
       
        cursor.execute(sql, {'id_tipo_fonte': id_tipo_fonte})
        connection.commit()
        print("Os dados foram deletados")
    except Exception as e:
        print(f"Ocorreu um erro ao deletar os dados: {e}")
    finally:
        cursor.close()
        connection.close()
 
def deletar_fonte():
    id_tipo_fonte = int(input('Digite o ID que gostaria de Deletar: '))
    deletar_fonte_banco(id_tipo_fonte)
 
def inserir_regiao_banco(regiao):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = """
            INSERT INTO regioes_sustentaveis (id_regiao, nome)
            VALUES (:id_regiao, :nome)
        """
 
        cursor.execute(sql, {
            'id_regiao': regiao['id_regiao'],
            'nome': regiao['nome'],
        })
        connection.commit()
        print('Dados inseridos')
    except Exception as e:
        print(f'Erro na inserção: {e}')
    finally:
        cursor.close()
        connection.close()
 
def inserir_regiao():
    id_regiao = int(input('Digite o ID da região: '))
    nome = input('Digite o nome: ')
    dados = {
        "id_regiao": id_regiao,
        "nome": nome
    }
    inserir_regiao_banco(dados)
 
def consultar_regiao_banco():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = "SELECT * FROM regioes_sustentaveis"
        cursor.execute(sql)
        regioes = cursor.fetchall()
        for regiao in regioes:
            print("Região:", regiao)
    except Exception as e:
        print(f"Erro ao consultar {e}")
 
 
 
def atualizar_regiao_banco(id_regiao,dados_novos):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = """
            UPDATE regioes_sustentaveis
            SET nome = :nome
            WHERE id_regiao = :id_regiao
        """
        dados_novos['id_regiao'] = id_regiao
        cursor.execute(sql, dados_novos)
        connection.commit()
        print("Os dados foram atualizados")
    except Exception as e:
        print(f"Ocorreu um erro ao atualizar os dados: {e}")
    finally:
        cursor.close()
        connection.close()
 
def atualizar_regiao():
    id_regiao = int(input('Digite o ID'))
    nome = input('Digite a regiao que deseja atualizar: ')
    dados = {
        "nome": nome
    }
    atualizar_regiao_banco(id_regiao,dados)
 
def deletar_regiao_banco(id_regiao):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = "DELETE FROM regioes_sustentaveis WHERE id_regiao = :id_regiao"
       
        cursor.execute(sql, {'id_regiao': id_regiao})
        connection.commit()
        print("Os dados foram deletados")
    except Exception as e:
        print(f"Ocorreu um erro ao deletar os dados: {e}")
    finally:
        cursor.close()
        connection.close()
 
 
def deletar_regiao():
    id_regiao = int(input('Digite o ID que quer apagar: '))
    deletar_regiao_banco(id_regiao)
 
 
def inserir_emissao_banco(emissao):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = """
            INSERT INTO emissoes_carbono (id_emissao, id_tipo_fonte, emissao)
            VALUES (:id_emissao, :id_tipo_fonte, :emissao)
        """
 
        cursor.execute(sql, {
            'id_emissao': emissao['id_emissao'],
            'id_tipo_fonte': emissao['id_tipo_fonte'],
            'emissao': emissao['emissao']
        })
        connection.commit()
        print('Dados inseridos')
    except Exception as e:
        print(f'Erro na inserção: {e}')
    finally:
        cursor.close()
        connection.close()
 
def inserir_emissao():
    id_emissao = int(input('Digite o ID de emissão: '))
    id_tipo_fonte = int(input('Digite o ID tipo fonte: '))
    emissao = int(input('Digite a emissao: '))
    dados = {
        "id_emissao": id_emissao,
        "id_tipo_fonte": id_tipo_fonte,
        "emissao": emissao
    }
    inserir_emissao_banco(dados)
 
 
def consultar_emissao_banco():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = "SELECT * FROM emissoes_carbono"
        cursor.execute(sql)
        emissoes = cursor.fetchall()
        for emissao in emissoes:
            print("Emissao:", emissao)
    except Exception as e:
        print(f"Erro ao consultar {e}")
 
 
 
def atualizar_emissao_banco(id_emissao,dados_novos):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = """
            UPDATE emissoes_carbono
            SET emissao = :emissao
            WHERE id_emissao = :id_emissao
        """
        dados_novos['id_emissao'] = id_emissao
        cursor.execute(sql, dados_novos)
        connection.commit()
        print("Os dados foram atualizados")
    except Exception as e:
        print(f"Ocorreu um erro ao atualizar os dados: {e}")
    finally:
        cursor.close()
        connection.close()
 
def atualizar_emissao():
    id_emissao = int(input('Digite o ID'))
    emissao = int(input('Digite a emissao: '))
    dados = {
        "emissao": emissao
    }
    atualizar_emissao_banco(id_emissao,dados)
 
 
def deletar_emissao_banco(id_emissao):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = "DELETE FROM emissoes_carbono WHERE id_emissao = :id_emissao"
       
        cursor.execute(sql, {'id_emissao': id_emissao})
        connection.commit()
        print("Os dados foram deletados")
    except Exception as e:
        print(f"Ocorreu um erro ao deletar os dados: {e}")
    finally:
        cursor.close()
        connection.close()
 
 
def deletar_emissao():
    id_emissao = int(input('Digite o ID que quer apagar'))
    deletar_emissao_banco(id_emissao)
 
 
def inserir_projeto_banco(projeto):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = """
            INSERT INTO projetos_sustentaveis (id_projeto, descricao, custo, status, id_tipo_fonte, id_regiao)
            VALUES (:id_projeto, :descricao, :custo, :status, :id_tipo_fonte, :id_regiao)
        """
 
        cursor.execute(sql, {
            'id_projeto': projeto['id_projeto'],
            'descricao': projeto['descricao'],
            'custo': projeto['custo'],
            'status':projeto['status'],
            'id_tipo_fonte':projeto['id_tipo_fonte'],
            'id_regiao':projeto['id_regiao']
        })
        connection.commit()
        print('Dados inseridos')
    except Exception as e:
        print(f'Erro na inserção: {e}')
    finally:
        cursor.close()
        connection.close()
 
def inserir_projeto():
    id_projeto = int(input('Digite o ID do projeto: '))
    descricao = input('Digite a descrição do projeto: ')
    custo = int(input('Digite o custo: '))
    status = input('Digite um status para o projeto: ')
    id_tipo_fonte = int(input('Digite o ID do tipo da fonte de energia: '))
    id_regiao = int(input('Digite o ID da região: '))
    dados = {
        "id_projeto": id_projeto,
        "descricao": descricao,
        "custo": custo,
        "status": status,
        "id_tipo_fonte": id_tipo_fonte,
        "id_regiao": id_regiao
    }
    inserir_projeto_banco(dados)
 
def consultar_projeto_banco():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = "SELECT * FROM projetos_sustentaveis"
        cursor.execute(sql)
        projetos = cursor.fetchall()
        for projeto in projetos:
            print("Projeto:", projeto)
    except Exception as e:
        print(f"Erro ao consultar {e}")
 
 
def atualizar_projeto_banco(id_projeto,dados_novos):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = """
            UPDATE projetos_sustentaveis
            SET descricao = :descricao,
                custo = :custo,
                status = :status
            WHERE id_projeto = :id_projeto
        """
        dados_novos['id_projeto'] = id_projeto
        cursor.execute(sql, dados_novos)
        connection.commit()
        print("Os dados foram atualizados")
    except Exception as e:
        print(f"Ocorreu um erro ao atualizar os dados: {e}")
    finally:
        cursor.close()
        connection.close()
 
def atualizar_projeto():
    id_projeto = int(input('Digite o ID'))
    descricao = input('Digite a nova descricao: ')
    custo = int(input('Digite o novo valor de custo: '))
    status = input('Digite o novo status: ')
    dados = {
        "descricao": descricao,
        "custo": custo,
        "status": status
    }
    atualizar_projeto_banco(id_projeto,dados)
 
def deletar_projeto_banco(id_projeto):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = "DELETE FROM projetos_sustentaveis WHERE id_projeto = :id_projeto"
       
        cursor.execute(sql, {'id_projeto': id_projeto})
        connection.commit()
        print("Os dados foram deletados")
    except Exception as e:
        print(f"Ocorreu um erro ao deletar os dados: {e}")
    finally:
        cursor.close()
        connection.close()
 
 
def deletar_projeto():
    id_projeto = int(input('Digite o ID que quer apagar'))
    deletar_projeto_banco(id_projeto)
 
 
def exibir_menu():
    for i in menu_opcoes:
        print(i)
 
def exibir_submenu():
    for i in sub_opcoes:
        print(i)
 
def main():
    while True:
        exibir_menu()
        opcao = input('Digite sua opção: ')
        if opcao == '1':
            exibir_submenu()
            subopcao = input('O que deseja fazer?')
            if subopcao == '1':
                inserir_fonte()
            elif subopcao == '2':
                consultar_fonte_banco()
            elif subopcao == '3':
                atualizar_fonte()
            elif subopcao == '4':
                deletar_fonte()
        elif opcao == '2':
            exibir_submenu()
            subopcao = input('O que deseja fazer?')
            if subopcao == '1':
                inserir_emissao()
            elif subopcao == '2':
                consultar_emissao_banco()
            elif subopcao == '3':
                atualizar_emissao()
            elif subopcao == '4':
                deletar_emissao()      
        elif opcao == '3':
            exibir_submenu()
            subopcao = input('O que deseja fazer?')
            if subopcao == '1':
                inserir_regiao()
            elif subopcao == '2':
                consultar_regiao_banco()
            elif subopcao == '3':
                atualizar_regiao()
            elif subopcao == '4':
                deletar_regiao()
        elif opcao == '4':
            exibir_submenu()
            subopcao = input('O que deseja fazer?')
            if subopcao == '1':
                inserir_projeto()
            elif subopcao == '2':
                consultar_projeto_banco()
            elif subopcao == '3':
                atualizar_projeto()
            elif subopcao == '4':
                deletar_projeto()
        elif opcao == '5':
            exportar_dados_para_json()
        elif opcao == '6':
            break            
 
 
main()