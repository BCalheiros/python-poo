# SQLite database
import sqlite3


class BancoDeDados:
    """ Classe que representa o banco de dados (database) da aplicação"""

    """ Construtor da classe:
        @param nome     nome do arquivo database
        @param conexao  conexao com o banco de dados
    """
    def __init__(self, nome = 'banco.db'):
        self.nome = nome
        self.conexao = None

    def conecta(self):
        """ Conecta passando o nome do arquivo
            @param conexao      conexao com o banco de dados
        """
        try:
            self.conexao = sqlite3.connect(self.nome)
            print('Conexão realizada com sucesso.')
        except AttributeError:
            pass


    def desconecta(self):
        """ Desconecta do banco de dados
            @param conexao      conexao com o banco de dados
        """
        self.conexao.close()

    def criarTabelas(self):
        """ Criar as tabelas do banco
            @param cursor       cursor do banco de dados
        """
        try:
            cursor = self.conexao.cursor()

            # Executa comando SQL: cria a tabela
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf VARCHAR(11) UNIQUE NOT NULL,
                email TEXT NOT NULL                    
            );
            """)

            print('Tabela criada com sucesso.')

        except AttributeError:
            print('Faça a conexão com o banco antes de criar as tabelas')

    def inserirCliente(self, nome, cpf, email):
        """ Inserir cliente no banco
            @param nome     Nome do cliente
            @param cpf      CPF do cliente
            @param email    Email do cliente
        """
        try:
            cursor = self.conexao.cursor()

            try:
                cursor.execute("""
                    INSERT INTO clientes (nome, cpf, email) VALUES (?,?,?)
                """, (nome, cpf, email))
            except sqlite3.IntegrityError:
                print('O cpf %s já existe!' % cpf)


            # Realiza efetivamente o comando 'execute'
            self.conexao.commit()

        except AttributeError:
            print('Faça a conexão do banco antes de inserir clientes.')

    def buscarClientes(self, cpf):
        """ Busca um cliente pelo cpf
            @param cpf      CPF do cliente
        """
        try:
            cursor = self.conexao.cursor()

            # obtém todos os dados
            cursor.execute("""SELECT * FROM clientes;""")

            for linha in cursor.fetchall():
                if linha[2] == cpf:
                    print('Cliente %s encontrado CPF: %s' % (linha[1], linha[2]))
                    break
        except AttributeError:
            print('Faça a conexão do banco antes de buscar clientes.')

    def removerCliente(self, cpf):
        """ Remove um cliente pelo cpf
            @param cpf      CPF do cliente
        """
        try:
            cursor = self.conexao.cursor()

            # obtém todos os dados
            cursor.execute("""SELECT * FROM clientes;""")

            for linha in cursor.fetchall():
                if linha[2] == cpf:
                    cursor.execute("""DELETE FROM clientes WHERE cpf = %s""" % (linha[2]))
                    print('Cliente %s removido com sucesso.' % linha[1])
                    break
        except AttributeError:
            print('Faça a conexão no banco antes de remover um cliente.')

    def buscar_email(self, email):
        """ Buscar cliente pelo email
            @param email    email do cliente
        """
        try:
            cursor = self.conexao.cursor()

            # obtém todos os dados
            cursor.execute("""SELECT * FROM clientes;""")

            for linha in cursor.fetchall():
                if linha[3] == email:
                    #print('Cliente %s encontrado: email %s' % (linha[1], linha[3]))
                    return True
                else:
                    return False
        except AttributeError:
            print('Faça a conexão do banco antes de buscar cliente.')