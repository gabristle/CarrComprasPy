class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
    
    def addProd(self, produto):
        self.produtos.append(produto)

    def exibirProd(self):
        for produto in self.produtos:
            print(f"{produto.nome} : R${produto.preco:.2f}")
    
    def total(self):
        resultado = 0
        for produto in self.produtos:
            resultado += produto.preco
        return resultado

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = CarrinhoDeCompras()

produto1 = Produto("Perfume", 129.99)
produto2 = Produto("Pulseira", 89.90)
produto3 = Produto("Par de Brincos", 120.00)
produto4 = Produto("Anel de Esmeralda", 2600.00)

carrinho.addProd(produto1)
carrinho.addProd(produto2)
carrinho.addProd(produto3)
carrinho.addProd(produto4)

carrinho.exibirProd()

totalCompra = carrinho.total()
print(f"Valor total da compra: R${totalCompra:.2f}")