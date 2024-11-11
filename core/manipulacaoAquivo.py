import json
import os
import pickle
from core.pedido import Pedido

def salvar_dados_json(pedidos, arquivo="pedidos.json", pasta="data"):
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    
    caminho_arquivo = os.path.join(pasta, arquivo)
    
    with open(caminho_arquivo, 'w') as file:
        json.dump([pedido.to_dict() for pedido in pedidos], file, indent=4)
    
    print(f"Dados salvos em {caminho_arquivo}.")

def carregar_dados_json(arquivo="pedidos.json", pasta="data"):
    caminho_arquivo = os.path.join(pasta, arquivo)
    try:
        with open(caminho_arquivo, 'r') as file:
            pedidos_data = json.load(file)
            return [Pedido.from_dict(data) for data in pedidos_data]
    except FileNotFoundError:
        print(f"O arquivo {caminho_arquivo} não foi encontrado.")
        return []

def salvar_dados_binario(pedidos, arquivo="pedidos.pkl", pasta="data"):
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    
    caminho_arquivo = os.path.join(pasta, arquivo)
    
    with open(caminho_arquivo, 'wb') as file:
        pickle.dump(pedidos, file)
    
    print(f"Dados salvos em {caminho_arquivo}.")

def carregar_dados_binario(arquivo="pedidos.pkl", pasta="data"):
    caminho_arquivo = os.path.join(pasta, arquivo)
    try:
        with open(caminho_arquivo, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        print(f"O arquivo {caminho_arquivo} não foi encontrado.")
        return []