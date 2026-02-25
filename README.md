# Sistema de Registro de Alunos 🎓

Um sistema de gerenciamento de alunos moderno e intuitivo, desenvolvido em Python utilizando Tkinter para a interface gráfica e SQLite para o armazenamento persistente de dados.

## 🚀 Funcionalidades

- **CRUD Completo**: Adicione, visualize, atualize e exclua registros de alunos.
- **Campos Detalhados**: Registro de Nome, Email, Telefone, Sexo, Data de Nascimento, Endereço e Curso.
- **Suporte a Imagens**: Possibilidade de carregar e visualizar fotos de perfil para cada aluno.
- **Interface Intuitiva**: Tabela interativa (Treeview) para visualização rápida dos dados.
- **Banco de Dados Local**: Utiliza SQLite3, não requer configuração complexa de servidor.

## 🛠️ Tecnologias Utilizadas

- **Python 3**: Linguagem base do projeto.
- **Tkinter**: Interface gráfica (GUI).
- **SQLite3**: Banco de Dados relacional leve.
- **Pillow (PIL)**: Processamento e exibição de imagens.
- **Tkcalendar**: Widget amigável para seleção de datas.

## 📋 Pré-requisitos

Antes de começar, você precisará ter o Python instalado em sua máquina.

### Instalação de dependências

Abra o terminal na pasta do projeto e execute:

```bash
pip install Pillow tkcalendar
```

## ⚙️ Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/Gustavoluizgonzaga/Sistema-de-registro-de-alunos.git
   ```
2. Navegue até a pasta do projeto:
   ```bash
   cd Sistema-de-registro-de-alunos
   ```
3. Execute a aplicação:
   ```bash
   python "Registro de alunos/interface.py"
   ```

## 📁 Estrutura do Projeto

- `Registro de alunos/interface.py`: Código principal da interface gráfica.
- `Registro de alunos/sistema.py`: Lógica de backend e comunicação com o banco de dados.
- `alunos.db`: Arquivo do banco de dados SQLite (gerado automaticamente).
- `imagens/`: Pasta contendo ícones e fotos de perfil.

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---
Desenvolvido por [Gustavo Luiz Gonzaga](https://github.com/Gustavoluizgonzaga)
