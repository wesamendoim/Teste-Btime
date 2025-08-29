import requests 
import pandas as pd

try:
    endpoint = "https://www.espn.com.br/futebol/classificacao/_/liga/bra.1"

    response = requests.get(endpoint)

    if response.status_code == 200:
        print("Conexão bem sucedida!")  
    else:
        print(f"Falha na conexão. Código de status: {response.status_code}")

except Exception as e:
    print("Erro ao conectar: ", e)
finally:
    print("Finalizando a conexão")