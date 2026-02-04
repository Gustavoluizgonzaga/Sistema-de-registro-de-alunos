import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        """
        Inicializa o sistema de registro de alunos, criando uma conexão com o banco de dados e um cursor 
        para executar comandos SQL.
        """
        self.conexao = sqlite3.connect('alunos.db')
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        """
        Cria a tabela de alunos no banco de dados se ela não existir.
        A tabela tem as seguintes colunas: id (chave primária), nome, idade e email...
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                email TEXT NOT NULL,
                sexo TEXT NOT NULL,
                data_nascimento TEXT NOT NULL,
                telefone TEXT NOT NULL,
                endereco TEXT NOT NULL,
                curso TEXT NOT NULL,
                foto TEXT NOT NULL
            )
        ''')
    
    def registro_aluno(self, alunos):
        """
        Registra um aluno ao banco de dados.
        """
        self.cursor.execute('''
            INSERT INTO alunos (nome, idade, email, sexo, data_nascimento, telefone, endereco, curso, foto)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', alunos)
        self.conexao.commit()

        # Exibir mensagem de sucesso
        messagebox.showinfo("Sucesso", "Aluno registrado com sucesso!")
        
    def ver_alunos(self):
        """
        Retorna uma lista com todos os alunos registrados no banco de dados.
        """
        self.cursor.execute('SELECT * FROM alunos')
        dados = self.cursor.fetchall()
        
        for i in dados:
            print(f"Id: {dados[0]}\nNome: {dados[1]}\nIdade: {dados[2]}\nEmail: {dados[3]}\nSexo: {dados[4]}"
                  "\nData de Nascimento: {dados[5]}\nTelefone: {dados[6]}\nEndereco: {dados[7]}\nCurso: {dados[8]}\nFoto: {dados[9]}\n")
            
    def procurar_aluno(self, id):
        """
        Procura um aluno pelo ID no banco de dados.
        """
        self.cursor.execute('SELECT * FROM alunos WHERE id = ?', (id,))
        dados = self.cursor.fetchone()
        
        print(f"Id: {dados[0]}\nNome: {dados[1]}\nIdade: {dados[2]}\nEmail: {dados[3]}\nSexo: {dados[4]}"
                "\nData de Nascimento: {dados[5]}\nTelefone: {dados[6]}\nEndereco: {dados[7]}\nCurso: {dados[8]}\nFoto: {dados[9]}\n")
        
    def atualizar_aluno(self, novos_dados):
        """
        Atualiza um aluno no banco de dados.
        Requer um array com os novos dados do aluno, com as seguintes colunas: id, nome, idade, email, 
        sexo, data_nascimento, telefone, endereco, curso e foto.
        """
        consulta = 'UPDATE alunos SET nome = ?, idade = ?, email = ?, sexo = ?, data_nascimento = ?,' 
        'telefone = ?, endereco = ?, curso = ?, foto = ? WHERE id = ?'
        self.cursor.execute(consulta, novos_dados)
        self.conexao.commit()
        
        # Exibir mensagem de sucesso
        messagebox.showinfo("Sucesso", "Aluno atualizado com sucesso!")

    def deletar_aluno(self, id):
        """
        Deleta um aluno do banco de dados.
        Requer o ID do aluno que deseja deletar.
        Exibe uma mensagem de sucesso ao deletar o aluno.
        """
        self.cursor.execute('DELETE FROM alunos WHERE id = ?', (id,))
        self.conexao.commit()
        
        # Exibir mensagem de sucesso
        messagebox.showinfo("Sucesso", "Aluno deletado com sucesso!")