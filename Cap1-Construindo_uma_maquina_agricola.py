# Importação dos módulos
import os
import oracledb
import pandas as pd
from datetime import datetime
from tabulate import tabulate

today_date = datetime.today().date()
# Try para tentativa de Conexão com o Banco de Dados
try:
    # Efetua a conexão com o Usuário no servidor
    conn = oracledb.connect(user='rm559439', password="010170", dsn='oracle.fiap.com.br:1521/ORCL')
    # Cria as instruções para cada módulo
    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
    inst_alteracao = conn.cursor()
    inst_exclusao = conn.cursor()
except Exception as e:
    # Informa o erro
    print("Erro: ", e)
    # Flag para não executar a Aplicação
    conexao = False
else:
    # Flag para executar a Aplicação
    conexao = True 
margem = ' ' * 4 # Define uma margem para a exibição da aplicação

# Enquanto o flag conexao estiver apontado com True
while conexao:
    # Limpa a tela via SO
    os.system('cls')

    # Apresenta o menu
    print("------- CRUD - TRABALHADORES RURAIS -------")
    print("""
    Para a manutenção dos sensores tempos as seguintes opções:      
    1 - Cadastrar Sensor
    2 - Listar Sensor
    3 - Alterar Sensor
    4 - Excluir Sensor
    
    Para consultas gerais temos:
    5 - Consultar Solo
    6 - Consultar Humidade
    7 - Consultar Irrigacao
    
    Para sair do sistema:
    8 - Sair
    """)

    # Captura a escolha do usuário
    escolha = input(margem + "Escolha -> ")

    # Verifica se o número digitado é um valor numérico
    if escolha.isdigit():
        escolha = int(escolha)
    else:
        escolha = 6
        print("Digite um número.\nReinicie a Aplicação!")

    os.system('cls')  # Limpa a tela via SO

    # VERIFICA QUAL A ESCOLHA DO USUÁRIO
    match escolha:
        case 1:
            try:
                print("----- CADASTRAR SENSOR-----\n")
                # Recebe os valores para cadastro
                var_sensor_type = input("Digite o tipo....: ")
                var_status = input("Digite o status....: ")
                var_sensor_location = input("Digite a localização...: ")
                today_date = datetime.today().date()

                # Monta a instrução SQL de cadastro com parâmetros
                cadastro = """ 
                INSERT INTO tb_md3_sensors (sensor_type, installation_date, status, sensor_location)
                VALUES (:sensor_type, :installation_date, :status, :sensor_location)
                """

                # Define the data dictionary for the parameterized query
                data = {
                    "sensor_type": var_sensor_type,
                    "installation_date": today_date,
                    "status": var_status,
                    "sensor_location": var_sensor_location
                }

                # Execute and commit the record
                inst_cadastro.execute(cadastro, data)
                conn.commit()

            except ValueError:
                # Handle non-numeric input where numeric is expected
                print("Digite um número na idade!")
            except Exception as e:
                # Handle any database connection or SQL errors
                print("Erro na transação do BD:", e)
            else:
                # Success message if the record was saved
                print("\n##### Dados GRAVADOS #####")

                # LISTAR TODOS OS PETS
        case 2:
            try:
                # Assuming you have an active connection and cursor (conn and inst_cadastro)
                print("----- LISTAR TODOS OS SENSORES -----\n")

                # SQL query to fetch all records
                query = "SELECT * FROM TB_MD3_Sensors"

                # Execute the query
                inst_cadastro.execute(query)

                # Fetch all rows from the query result
                sensors = inst_cadastro.fetchall()

                # Define table headers
                headers = ["Sensor ID", "Sensor Type", "Installation Date", "Status", "Sensor Location"]

                # Check if there are any sensors to display
                if sensors:
                    # Display the data in a table format using tabulate
                    print(tabulate(sensors, headers=headers, tablefmt="grid"))
                else:
                    print("No sensors found.")

            except Exception as e:
                # Handle any database connection or SQL errors
                print("Erro ao listar os sensores:", e)
            finally:
                # Close the connection if needed (optional)
                # conn.close()
                pass
                
                    # ALTERAR OS DADOS DE UM REGISTRO
        case 3:
            try:
                print("----- ATUALIZAR SENSOR -----\n")
                
                # Recebe o Sensor_ID para localizar o sensor
                var_sensor_id = int(input("Digite o Sensor ID para atualizar: "))

                # Check if the sensor exists
                check_query = "SELECT COUNT(*) FROM TB_MD3_Sensors WHERE sensor_id = :sensor_id"
                inst_cadastro.execute(check_query, {"sensor_id": var_sensor_id})
                result = inst_cadastro.fetchone()

                # If the count is 0, the sensor does not exist
                if result[0] == 0:
                    print(f"Sensor ID {var_sensor_id} não encontrado!")
                else:
                    # Recebe os novos valores para o sensor
                    var_sensor_type = input("Digite o tipo....: ")
                    var_status = input("Digite o status....: ")
                    var_sensor_location = input("Digite a localização...: ")

                    # Get today's date for the installation date update (if needed)
                    today_date = datetime.today().date()

                    # Monta a instrução SQL para atualizar os dados
                    update_query = """
                    UPDATE TB_MD3_Sensors
                    SET sensor_type = :sensor_type, 
                        installation_date = :installation_date,
                        status = :status,
                        sensor_location = :sensor_location
                    WHERE sensor_id = :sensor_id
                    """

                    # Dados para passar para a query
                    data = {
                        "sensor_type": var_sensor_type,
                        "installation_date": today_date,
                        "status": var_status,
                        "sensor_location": var_sensor_location,
                        "sensor_id": var_sensor_id
                    }

                    # Executa a atualização
                    inst_cadastro.execute(update_query, data)
                    conn.commit()

                    print("\n##### Dados ATUALIZADOS #####")

            except ValueError:
                # Erro de tipo de dado, por exemplo, se o ID não for um número
                print("Digite um número válido para o Sensor ID!")
            except Exception as e:
                # Erro de conexão ou SQL
                print("Erro ao atualizar o sensor:", e)
        case 4:
            try:
                print("----- EXCLUIR SENSOR -----\n")
                
                # Recebe o Sensor_ID para localizar o sensor
                var_sensor_id = int(input("Digite o Sensor ID para excluir: "))

                # Check if the sensor exists
                check_query = "SELECT COUNT(*) FROM TB_MD3_Sensors WHERE sensor_id = :sensor_id"
                inst_cadastro.execute(check_query, {"sensor_id": var_sensor_id})
                result = inst_cadastro.fetchone()

                # If the count is 0, the sensor does not exist
                if result[0] == 0:
                    print(f"Sensor ID {var_sensor_id} não encontrado!")
                else:
                    # Prompt to confirm deletion
                    confirm = input(f"Tem certeza de que deseja excluir o Sensor ID {var_sensor_id}? (s/n): ")
                    if confirm.lower() == 's':
                        # Monta a instrução SQL para excluir o sensor
                        delete_query = "DELETE FROM TB_MD3_Sensors WHERE sensor_id = :sensor_id"

                        # Executa a exclusão
                        inst_cadastro.execute(delete_query, {"sensor_id": var_sensor_id})
                        conn.commit()

                        print(f"\n##### Sensor ID {var_sensor_id} EXCLUÍDO #####")
                    else:
                        print("Exclusão cancelada.")

            except ValueError:
                # Erro de tipo de dado, por exemplo, se o ID não for um número
                print("Digite um número válido para o Sensor ID!")
            except Exception as e:
                # Erro de conexão ou SQL
                print("Erro ao excluir o sensor:", e)
        
        case 5:
            print("\n!!!!! EXCLUI TODOS OS DADOS TABELA !!!!!\n")
            confirma = input(margem + "CONFIRMA A EXCLUSÃO DE TODOS OS PETS? [S]im ou [N]ÃO?")
            if confirma.upper() == "S":
                # Apaga todos os registros
                exclusao = "DELETE FROM petshop"
                inst_exclusao.execute(exclusao)
                conn.commit()

                # Depois de excluir todos os registros ele zera o ID
                data_reset_ids = """ ALTER TABLE petshop MODIFY(ID GENERATED AS IDENTITY (START WITH 1)) """
                inst_exclusao.execute(data_reset_ids)
                conn.commit()

                print("##### Todos os registros foram excluídos! #####")
            else:
                print(margem + "Operação cancelada pelo usuário!")

        # SAI DA APLICAÇÃO
        case 6:
            # Modificando o flag da conexão
            conexao = False

        # CASO O NUMERO DIGITADO NÃO SEJA UM DO MENU
        
        case 7:
            # Modificando o flag da conexão
            conexao = False

        # CASO O NUMERO DIGITADO NÃO SEJA UM DO MENU
        
        case 8:
            # Modificando o flag da conexão
            conexao = False

        # CASO O NUMERO DIGITADO NÃO SEJA UM DO MENU
        
        
        case 9:
            # Modificando o flag da conexão
            conexao = False

        # CASO O NUMERO DIGITADO NÃO SEJA UM DO MENU
        case _:
            input(margem + "Digite um número entre 1 e 9.")

    # Pausa o fluxo da aplicação para a leitura das informações
    input(margem + "Pressione ENTER")
else:
    print("Obrigado por utilizar a nossa aplicação! :)")