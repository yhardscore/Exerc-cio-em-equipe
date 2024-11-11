from core.Gestao_pedidos import GestorDePedidos
from core.pedido import Pedido
from core.produto import Produto


def main():
    try:
        produto1 = Produto("Camisa", 50.0, "Vestuário")
        produto2 = Produto("Calça", 80.0, "Vestuário")
        produto3 = Produto("Tênis", 110.0, "Vestuário")
        produto4 = Produto("Celular", 4500.0, "Eletrônico")
        
        produtos = [produto1, produto2]
        quantidade1 = {produto1: 2, produto2: 1}
        pedido1 = Pedido(produtos, quantidade1, "Jonas", status="Novo")

        produtos2 = [produto3, produto4]
        quantidade2 = {produto3: 2, produto4: 1}
        pedido2 = Pedido(produtos2, quantidade2, "Diego", status="Antigo")

        gestor = GestorDePedidos()
        gestor.adicionar_pedido(pedido1)
        gestor.adicionar_pedido(pedido2)
        pedidos_novos = gestor.listar_pedidos_por_status("Novo")
        pedidos_antigos = gestor.listar_pedidos_por_status("Antigo")

        print("Pedidos com status 'Novo':", [p.detalhes_pedido() for p in pedidos_novos])
        print("Pedidos com status 'Antigo':", [p.detalhes_pedido() for p in pedidos_antigos])

        gestor.salvar_dados_json()
        gestor.carregar_dados_json()
        gestor.salvar_dados_binario()
        gestor.carregar_dados_binario()

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
