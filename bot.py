from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager
from core.Gestao_pedidos import GestorDePedidos
from core.pedido import Pedido
from core.produto import Produto
import csv
import pandas as pd

def preencher_formulario(bot, pedido):
    bot.browse("http://127.0.0.1:5000/")
    
    bot.find_element('//*[@id="cliente"]', By.XPATH).send_keys(pedido.cliente)
    bot.sleep(2)
    
    bot.find_element('//*[@id="formularioPedido"]/input[2]', By.XPATH).send_keys(pedido.status)
    bot.sleep(2)

    for i, (produto, quantidade) in enumerate(pedido.quantidade.items(), 1):
        bot.find_element(f'//*[@id="produto{i}"]/div[1]/input', By.XPATH).send_keys(produto.nome)
        bot.sleep(2)
        
        bot.find_element(f'//*[@id="produto{i}"]/div[2]/input', By.XPATH).send_keys(str(produto.preco))
        bot.sleep(2)
        
        bot.find_element(f'//*[@id="produto{i}"]/div[3]/input', By.XPATH).send_keys(str(quantidade))
        bot.sleep(2)

        if i < len(pedido.quantidade):  
            bot.find_element('//*[@id="adicionarProduto"]', By.XPATH).click()
            bot.sleep(2)

    bot.find_element('//*[@id="formularioPedido"]', By.XPATH).submit()
    bot.sleep(1000)

    print("\n" + pedido.detalhes_pedido())

def mostrar_listagem_json(bot):
    bot.browse("http://127.0.0.1:5000/listagem")
    bot.sleep(3000)
    
def carregar_pedidos_csv(gestor, caminho_csv):
    with open(caminho_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        pedidos_dict = {}
        
        for row in reader:
            cliente = row['cliente']
            produto_nome = row['produto_nome']
            produto_preco = float(row['produto_preco'])
            quantidade = int(row['quantidade'])
            status = row['status']
            
            produto = Produto(produto_nome, produto_preco, "Diversos")
            
            if cliente not in pedidos_dict:
                pedidos_dict[cliente] = {"produtos": [], "quantidades": {}, "status": status}
            
            pedidos_dict[cliente]["produtos"].append(produto)
            pedidos_dict[cliente]["quantidades"][produto] = quantidade
        
        # Cria uma instância de Pedido para cada cliente e adiciona ao gestor
        for cliente, dados in pedidos_dict.items():
            pedido = Pedido(dados["produtos"], dados["quantidades"], cliente, dados["status"])
            gestor.adicionar_pedido(pedido)

    print("Pedidos carregados do CSV com sucesso.")

def carregar_pedidos_xlsx(gestor, caminho_xlsx):
    # Lê o arquivo Excel
    df = pd.read_excel(caminho_xlsx)
    
    pedidos_dict = {}
    
    for _, row in df.iterrows():
        cliente = row['cliente']
        produto_nome = row['produto_nome']
        produto_preco = float(row['produto_preco'])
        quantidade = int(row['quantidade'])
        status = row['status']
        
        produto = Produto(produto_nome, produto_preco, "Diversos")
        
        if cliente not in pedidos_dict:
            pedidos_dict[cliente] = {"produtos": [], "quantidades": {}, "status": status}
        
        pedidos_dict[cliente]["produtos"].append(produto)
        pedidos_dict[cliente]["quantidades"][produto] = quantidade
    
    for cliente, dados in pedidos_dict.items():
        pedido = Pedido(dados["produtos"], dados["quantidades"], cliente, dados["status"])
        gestor.adicionar_pedido(pedido)

    print("Pedidos carregados do arquivo XLSX com sucesso.")

def main():
    produto1 = Produto("Camisa", 50.0, "Vestuário")
    produto2 = Produto("Calça", 80.0, "Vestuário")
    produto3 = Produto("Sapato", 100.0, "Calçado")

    quantidade1 = {produto1: 2, produto2: 1, produto3: 3}
    pedido1 = Pedido([produto1, produto2, produto3], quantidade1, "Yasmin", "Novo")

    quantidade2 = {produto1: 1, produto3: 4}
    pedido2 = Pedido([produto1, produto3], quantidade2, "Ricardo", "Processando")

    gestor = GestorDePedidos()
    gestor.adicionar_pedido(pedido1)
    gestor.adicionar_pedido(pedido2)

    caminho_csv = 'data/pedidos.csv'
    carregar_pedidos_csv(gestor, caminho_csv)
    caminho_xlsx = 'data/pedidos.xlsx'
    carregar_pedidos_xlsx(gestor, caminho_xlsx)

    gestor.salvar_dados_json()
    gestor.carregar_dados_json()
    gestor.salvar_dados_binario()
    gestor.carregar_dados_binario()

    bot = WebBot()
    bot.headless = False 
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    for pedido in gestor.pedidos:
        preencher_formulario(bot, pedido)

    mostrar_listagem_json(bot)

    bot.stop_browser()

if __name__ == "__main__":
    main()
