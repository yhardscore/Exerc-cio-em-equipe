from flask import Flask, json, render_template, request
from core.produto import Produto
from core.pedido import Pedido

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        cliente = request.form["cliente"]
        status = request.form["status"]
        
        produtos = []
        quantidades = {}

        contador_produtos = len(request.form) // 3
        for i in range(1, contador_produtos + 1):
            produto_nome = request.form.get(f'produto{i}')
            produto_preco = float(request.form.get(f'preco{i}'))
            produto_quantidade = int(request.form.get(f'quantidade{i}'))
            
            produto = Produto(produto_nome, produto_preco, "Categoria")
            produtos.append(produto)
            quantidades[produto] = produto_quantidade

        pedido_novo = Pedido(produtos, quantidades, cliente, status)
        
        return render_template("resultado.html", pedido=pedido_novo)

    return render_template("formulario.html")


@app.route('/listagem')
def listagem():
    with open('data/pedidos.json', 'r', encoding='utf-8') as f:
        dados = json.load(f)
    
    return render_template('listagem.html', pedidos=dados)

if __name__ == "__main__":
    app.run(debug=True)
