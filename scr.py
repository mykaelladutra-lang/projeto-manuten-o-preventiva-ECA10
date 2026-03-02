# arquivo responsável pela geração dos dados qeu serao simulados 

import pandas as pd
import random
from datetime import datetime, timedelta

def gerar_dados(qtd_registros=100):
    dados = []
    tempo_inicial = datetime.now()

    for i in range(qtd_registros):
        registro = {
            "timestamp": tempo_inicial + timedelta(minutes=i),
            "temperatura": round(random.uniform(60, 95), 2),
            "vibracao": round(random.uniform(1.5, 5.0), 2),
            "corrente": round(random.uniform(3.5, 7.0), 2)
        }
        dados.append(registro)

    df = pd.DataFrame(dados)
    df.to_csv("dados/dados_simulados.csv", index=False)
    print("Dados gerados com sucesso!")

if __name__ == "__main__":
    gerar_dados()

