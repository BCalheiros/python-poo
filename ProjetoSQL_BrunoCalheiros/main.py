# Principal
from database import BancoDeDados

if __name__ == "__main__":

    banco = BancoDeDados()
    banco.conecta()
    banco.criarTabelas()

    banco.inserirCliente('Bruno', '11111111111', 'brunoolc@gmail.com')
    banco.inserirCliente('Andrelize', '22222222222', 'andrelize@gmail.com')

    banco.buscarClientes('22222222222')

    banco.removerCliente('11111111111')
    banco.buscarClientes('11111111111')
    print(banco.buscar_email('andrelize@gmail.com'))
    banco.desconecta()