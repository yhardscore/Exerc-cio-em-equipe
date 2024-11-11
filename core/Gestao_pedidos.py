from functools import reduce
from typing import List, Dict
from datetime import datetime
from core.pedido import Pedido
import core.manipulacaoAquivo


def log_atividade(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] {datetime.now()} - Executou: {func} | Args: {args[1:]} | Retorno: {result}")
        return result
    return wrapper

class GestorDePedidos:
    def __init__(self):
        self.pedidos = [] 

    @log_atividade
    def adicionar_pedido(self, pedido: Pedido):
        self.pedidos.append(pedido)

    @log_atividade
    def listar_pedidos_por_status(self, status: str):
        return list(filter(lambda p: p.status == status, self.pedidos))

    def pedidos_por_categoria(self, categoria: str):
        produtos_categoria = filter(lambda p: any(produto.categoria == categoria for produto in p.produtos), self.pedidos)
        return list(map(lambda p: (p.cliente, [prod.nome for prod in p.produtos if prod.categoria == categoria]), produtos_categoria))

    def total_vendas(self):
        return reduce(lambda acc, pedido: acc + pedido.total_pedido(), self.pedidos, 0)

    def salvar_dados_json(self, arquivo="pedidos.json"):
        core.manipulacaoAquivo.salvar_dados_json(self.pedidos, arquivo)

    def carregar_dados_json(self, arquivo="pedidos.json"):
        self.pedidos = core.manipulacaoAquivo.carregar_dados_json(arquivo)

    def salvar_dados_binario(self, arquivo="pedidos.pkl"):
        core.manipulacaoAquivo.salvar_dados_binario(self.pedidos, arquivo)

    def carregar_dados_binario(self, arquivo="pedidos.pkl"):
        self.pedidos = core.manipulacaoAquivo.carregar_dados_binario(arquivo)
