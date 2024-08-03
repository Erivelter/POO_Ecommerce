from index import EcommerceApp
class Produto():
    def __init__(self, nome_produto:str, preco:float, codigo:str, quantidade:int) -> None:
        self.nome_produto = nome_produto
        self.preco = preco
        self.codigo = codigo
        self.quantidade = quantidade
        self.historico_compras = {}  # Dicionário para armazenar histórico de compras

  
class Vendedor():
    def __init__(self, nome:str, sobrenome:str, cnpj:str ) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.cnpj = cnpj
        self.produtos_venda = []

    def adicionar_produto_venda(self, produto):
        self.produtos_venda.append(produto)

    def remover_produto_venda(self, produto):
        if produto in self.produtos_venda:
            self.produtos_venda.remove(produto)
    
    def visualizar_a_vendas(self):
        if self.produtos_venda:
            print(f"Produtos à venda pelo vendedor {self.nome} {self.sobrenome}:")
            for produto in self.produtos_venda:
                print(f"- {produto.nome_produto}, Preço: R${produto.preco}, Quantidade: {produto.quantidade}")
        else:
            print("Este vendedor não possui produtos à venda.")
    
    def visualizar_vendas_realizadas(self):
        if self.produtos_venda:
            print(f"Vendas realizadas pelo vendedor {self.nome} {self.sobrenome}:")
            for produto in self.produtos_venda:
                if produto.historico_compras:
                    for comprador, compras in produto.historico_compras.items():
                        for compra in compras:
                            print(f"Comprador: {comprador.nome_Comprador} {comprador.sobrenome_Comprador}, Produto: {produto.nome_produto}, Quantidade: {compra['quantidade']}, Preço: R${compra['preco']}")
                else:
                    print(f"Nenhum histórico de vendas para o produto {produto.nome_produto}")
        else:
            print("Este vendedor não possui produtos vendidos.")


class Comprador():
    def __init__(self, nome_Comprador:str, sobrenome_Comprador:str, cpf:str, dinheiro_disponivel:int) -> None:
        self.nome_Comprador = nome_Comprador
        self.sobrenome_Comprador = sobrenome_Comprador
        self.cpf = cpf
        self.dinheiro_disponivel = dinheiro_disponivel
        self.historico_compras = []
        self.carrinho = CarrinhoDeCompras()

    def adicionar_carrinho(self, produto):
        self.carrinho.adicionar_produto(produto)

    def remover_carrinho(self, produto):
        self.carrinho.remover_produto(produto)

    def realizar_compra(self):
        self.carrinho.realizar_compra(self)


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos_no_carrinho = []

    def adicionar_produto(self, produto):
        self.produtos_no_carrinho.append(produto)

    def remover_produto(self, produto):
        if produto in self.produtos_no_carrinho:
            self.produtos_no_carrinho.remove(produto)

    def visualizar_carrinho(self):
        if self.produtos_no_carrinho:
            print("Produtos no carrinho:")
            for produto in self.produtos_no_carrinho:
                print(f"- {produto.nome_produto}")
        else:
            print("Carrinho vazio.")

    def realizar_compra(self, comprador):
        if self.produtos_no_carrinho:
            produto = self.produtos_no_carrinho[0]  # Por simplicidade, pega o primeiro produto do carrinho
            if produto.preco <= comprador.dinheiro_disponivel:
                comprador.dinheiro_disponivel -= produto.preco
                # Atualiza o histórico de compras do produto
                if comprador not in produto.historico_compras:
                    produto.historico_compras[comprador] = []
                produto.historico_compras[comprador].append({'quantidade': 1, 'preco': produto.preco})
                self.produtos_no_carrinho.remove(produto)
                produto.quantidade -= 1
                print(f"Compra realizada com sucesso: {produto.nome_produto}")
            else:
                print("Dinheiro insuficiente para realizar a compra.")
        else:
            print("Carrinho de compras vazio.")


# Exemplo de uso:
vendedor1 = Vendedor("João", "Silva", "123456789")
produto1 = Produto("Celular", 1500.0, "001", 10)
produto2 = Produto("Tablet", 1200.0, "002", 5)
vendedor1.adicionar_produto_venda(produto1)
vendedor1.adicionar_produto_venda(produto2)

comprador1 = Comprador("Maria", "Santos", "987654321", 2000.0)
comprador1.adicionar_carrinho(produto1)

comprador1.realizar_compra()
print(f"Quantidade de {produto1.nome_produto} no estoque do vendedor: {produto1.quantidade}")

vendedor1.visualizar_vendas_realizadas()
