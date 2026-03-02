# arquivo responsável pela geração dos dados qeu serao simulados 

import pandas as pd
import random
from datetime import datetime, timedelta

def gerar_dados(qtd_registros=100):
    dados = []
    tempo_inicial = datetime.now()


