import requests 
import pandas as pd

try:
    # Conectando na API da ESPN
    endpoint = "https://site.api.espn.com/apis/v2/sports/soccer/bra.1/standings"

    #Pedindo a conexão
    response = requests.get(endpoint)

    #Verificando se a conexão foi bem sucedida
    if response.status_code == 200:
        print("Conexão bem sucedida!")  
    else:
       Exception(f"Falha na conexão. Código de status: {response.status_code}")

    data = response.json()
    df = pd.json_normalize(data["children"][0]["standings"]["entries"], sep=".")
    print(df)
    
    entries = pd.json_normalize(
    data["children"][0]["standings"]["entries"],
    sep=".")
    
    #Variavel para guardar a tabela
    tabela = []

    #Iterando sobre as linhas do Json
    for _, row in entries.iterrows():
        team = row["team.displayName"] #Capturando o nome do time
        stats_list = row["stats"] #Capturando a lista de stats
        stats = {s["name"]: s.get("value", s.get("displayValue")) for s in stats_list}

        #Montando a tabela para enviar para o DataFrame
        tabela.append({
            "time": team,
            "jogos": stats.get("gamesPlayed"),
            "vitorias": stats.get("wins"),
            "empates": stats.get("ties"),
            "derrotas": stats.get("losses"),
            "gols_pro": stats.get("pointsFor"),
            "gols_contra": stats.get("pointsAgainst"),
            "saldo": stats.get("pointDifferential"),
            "pontos": stats.get("points"),
        })

    #Montando o DF
    df = pd.DataFrame(tabela)
    print(df)
    
    #Montando o CSV
    df.to_csv("Excel(arquivocsv)\\tabela_brasileirao_V2.csv", index=False, sep=";", encoding="utf-8-sig")

except Exception as e:
    print("Erro ao conectar: ", e)
finally:
    print("Finalizando a conexão")
