from tkinter import Tk, Frame, Label, Entry, Button, ttk, messagebox, filedialog as fd
from tkinter import RAISED, RIDGE, SOLID, LEFT, CENTER, W, END

from tkcalendar import DateEntry
from PIL import ImageTk, Image
from datetime import date, datetime
from sistema import SistemaDeRegistro

# Initialize global variables for image handling
imagem = None
imagem_string = ""
l_imagem = None

# Create main window
app = Tk()
app.geometry("1060x720")
app.resizable(False, False)
app.configure(bg="ghostwhite")
app.title("Registro de Alunos")

# Initialize Database System
sistema = SistemaDeRegistro()

# Style configuration
style = ttk.Style(app)
style.theme_use("clam")

# --- Frames ---
frame_logo = Frame(app, width=1010, height=90, bg="steelblue")
frame_logo.grid(row=0, column=0, padx=0, pady=35, sticky="nsew", columnspan=5)

frame_botoes = Frame(app, width=300, height=250, bg="ghostwhite", relief=RAISED)
frame_botoes.grid(row=1, column=0, padx=0, pady=0, sticky="w")
frame_botoes.config(bg="ghostwhite") # Fixed red background

frame_detalhes = Frame(app, width=800, height=250, bg="ghostwhite", relief=SOLID)
frame_detalhes.grid(row=1, column=1, padx=0, pady=0, sticky="nsew")

frame_tabela = Frame(app, width=800, height=100, bg="ghostwhite", relief=SOLID)
frame_tabela.grid(row=3, column=0, padx=0, pady=1, sticky="nsew", columnspan=5)

# --- Header/Logo ---
try:
    # App Icon
    icon = Image.open("registro de alunos/imagens/open-book.png")
    photo = ImageTk.PhotoImage(icon)
    app.wm_iconphoto(False, photo)
    
    # Header Logo
    img = Image.open("registro de alunos/imagens/study.png")
    img = img.resize((80, 80))
    logo = ImageTk.PhotoImage(img)
    
    label_logo = Label(frame_logo, image=logo, text="Sistema de Registro de Alunos - (SRA)", 
                      width=900, height=90, compound=LEFT, anchor=W, 
                      font="verdana 15 bold", fg="white", bg="steelblue")
    label_logo.image = logo # Keep reference
    label_logo.place(x=250, y=0)
except Exception as e:
    print(f"Erro ao carregar imagens: {e}")
    # Fallback text if images fail
    label_logo = Label(frame_logo, text="Sistema de Registro de Alunos - (SRA)", 
                      width=900, height=90, anchor=CENTER, 
                      font="verdana 15 bold", fg="white", bg="steelblue")
    label_logo.place(x=50, y=0)

# --- Form Fields ---
# Name
Label(frame_detalhes, text="Nome: ", font="verdana 10", fg="black", bg="ghostwhite").place(x=50, y=10)
entry_nome = Entry(frame_detalhes, width=25, font="verdana 10", justify=LEFT, relief=SOLID, fg="black", bg="white")
entry_nome.place(x=50, y=40)

# Email
Label(frame_detalhes, text="Email: ", font="verdana 10", fg="black", bg="ghostwhite").place(x=50, y=70)
entry_email = Entry(frame_detalhes, width=25, font="verdana 10", justify=LEFT, relief=SOLID, fg="black", bg="white")
entry_email.place(x=50, y=100)

# Phone
Label(frame_detalhes, text="Telefone: ", font="verdana 10", fg="black", bg="ghostwhite").place(x=50, y=130)
entry_tel = Entry(frame_detalhes, width=12, font="verdana 10", justify=LEFT, relief=SOLID, fg="black", bg="white")
entry_tel.place(x=50, y=160)

# Gender
Label(frame_detalhes, text="Sexo: ", font="verdana 10", fg="black", bg="ghostwhite").place(x=170, y=130)
combo_sexo = ttk.Combobox(frame_detalhes, width=8, font="verdana 10", justify=CENTER)
combo_sexo['values'] = ("Masculino", "Feminino")
combo_sexo.place(x=170, y=160)

# Date of Birth
Label(frame_detalhes, text="Data de Nascimento: ", font="verdana 10", fg="black", bg="ghostwhite").place(x=400, y=10)
nasc = DateEntry(frame_detalhes, width=15, justify=CENTER, font="verdana 10", fg="black", bg="white", year=date.today().year, date_pattern='dd/mm/yyyy', locale='pt_BR')
nasc.place(x=400, y=39)

# Address
Label(frame_detalhes, text="Endereço: ", font="verdana 10", fg="black", bg="ghostwhite").place(x=400, y=70)
entry_endereco = Entry(frame_detalhes, width=17, font="verdana 10", justify=LEFT, relief=SOLID, fg="black", bg="white")
entry_endereco.place(x=400, y=100)

# Course
cursos = ["Informática", "Medicina", "Engenharia", "Design", "Tecnologia", "Outro"]
Label(frame_detalhes, text="Curso: ", font="verdana 10", fg="black", bg="ghostwhite").place(x=400, y=130)
combo_curso = ttk.Combobox(frame_detalhes, width=15, font="verdana 10", justify=LEFT)
combo_curso['values'] = cursos
combo_curso.place(x=400, y=160)

# Image Preview Label
l_imagem = Label(frame_detalhes, bg="ghostwhite")
l_imagem.place(x=650, y=10)

# --- Treeview Setup ---
lista_headers = ["ID", "Nome", "Idade", "Email", "Telefone", "Sexo", "Data de Nascimento", "Endereço", "Curso"]

tree_aluno = ttk.Treeview(frame_tabela, columns=lista_headers, show="headings")
tree_aluno.grid(row=1, column=0, sticky="nsew")

vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
vsb.grid(row=1, column=1, sticky="ns")

hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)
hsb.grid(row=2, column=0, sticky="ew")

tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

frame_tabela.grid_rowconfigure(1, weight=1)
frame_tabela.grid_columnconfigure(0, weight=1)

anchors = ["w", "w", "center", "w", "center", "center", "center", "w", "w"]
widths  = [40, 150, 60, 180, 120, 80, 140, 150, 120]

for i, col in enumerate(lista_headers):
    tree_aluno.heading(col, text=col, anchor=W)
    tree_aluno.column(col, width=widths[i], anchor=anchors[i])

# --- Functions ---

def escolher_imagem(): 
    """Abre diálogo para selecionar imagem e atualiza preview."""
    global imagem, imagem_string, l_imagem

    caminho = fd.askopenfilename()
    if not caminho:
        return
        
    imagem_string = caminho

    try:
        imagem = Image.open(caminho)
        imagem = imagem.resize((130, 130))
        imagem = ImageTk.PhotoImage(imagem)
        l_imagem.config(image=imagem)
        l_imagem.image = imagem # Keep reference
        
        botao_carregar['text'] = "Alterar Imagem"
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível carregar a imagem: {e}")

def calcular_idade(nascimento):
    today = date.today()
    return today.year - nascimento.year - ((today.month, today.day) < (nascimento.month, nascimento.day))

def mostrar_alunos():
    """Busca alunos no BD e preenche a tabela."""
    df_lista = sistema.ver_alunos()
    
    # Limpar tabela atual
    for i in tree_aluno.get_children():
        tree_aluno.delete(i)
             
    for item in df_lista:
        # DB: id, nome, idade, email, sexo, data_nascimento, telefone, endereco, curso, foto
        display_item = [item[0], item[1], item[2], item[3], item[6], item[4], item[5], item[7], item[8]]
        tree_aluno.insert("", END, values=display_item)

def limpar_campos():
    global imagem_string, l_imagem
    entry_nome.delete(0, END)
    entry_email.delete(0, END)
    entry_tel.delete(0, END)
    entry_endereco.delete(0, END)
    nasc.set_date(date.today())
    combo_sexo.set('')
    combo_curso.set('')
    
    imagem_string = ""
    l_imagem.config(image="") 
    l_imagem.image = None
    botao_carregar['text'] = "Carregar Imagem"

def adicionar_aluno():
    nome = entry_nome.get()
    data_nasc = nasc.get_date()
    idade = calcular_idade(data_nasc)
    email = entry_email.get()
    telefone = entry_tel.get()
    sexo = combo_sexo.get()
    endereco = entry_endereco.get()
    curso = combo_curso.get()
    foto = imagem_string

    if nome == "":
        messagebox.showerror('Erro', 'O nome é obrigatório')
        return

    dados = [nome, idade, email, sexo, data_nasc, telefone, endereco, curso, foto]
    sistema.registro_aluno(dados)
    mostrar_alunos()
    limpar_campos()

def atualizar_aluno():
    try:
        tree_selection = tree_aluno.selection()[0]
        tree_values = tree_aluno.item(tree_selection, 'values')
        id_aluno = tree_values[0]
        
        nome = entry_nome.get()
        data_nasc = nasc.get_date()
        idade = calcular_idade(data_nasc)
        email = entry_email.get()
        telefone = entry_tel.get()
        sexo = combo_sexo.get()
        endereco = entry_endereco.get()
        curso = combo_curso.get()
        foto = imagem_string
        
        dados = [nome, idade, email, sexo, data_nasc, telefone, endereco, curso, foto, id_aluno]
        sistema.atualizar_aluno(dados)
        mostrar_alunos()
        limpar_campos()
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um aluno na tabela')

def deletar_aluno():
    try:
        tree_selection = tree_aluno.selection()[0]
        tree_values = tree_aluno.item(tree_selection, 'values')
        id_aluno = tree_values[0]
        
        sistema.deletar_aluno(id_aluno)
        mostrar_alunos()
        limpar_campos()
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um aluno na tabela')

def selecionar_aluno(event):
    global imagem_string, l_imagem, imagem
    
    try:
        selection = tree_aluno.selection()
        if not selection:
            return
            
        selected_item = selection[0]
        tree_values = tree_aluno.item(selected_item, 'values')
        id_aluno = tree_values[0]
        
        # Busca dados completos no BD
        dados = sistema.procurar_aluno(id_aluno)
        # id, nome, idade, email, sexo, data_nascimento, telefone, endereco, curso, foto
        
        entry_nome.delete(0, END)
        entry_nome.insert(0, dados[1])
        
        entry_email.delete(0, END)
        entry_email.insert(0, dados[3])
        
        entry_tel.delete(0, END)
        entry_tel.insert(0, dados[6])
        
        combo_sexo.set(dados[4])
        
        try:
            # Tenta converter de YYYY-MM-DD (padrão do banco) para objeto date
            data_nascimento_obj = datetime.strptime(dados[5], '%Y-%m-%d').date()
            nasc.set_date(data_nascimento_obj)
        except ValueError:
            # Caso a data esteja em outro formato ou inválida, tenta setar direto ou ignora
            try:
                # Se estiver em DD/MM/YYYY
                data_nascimento_obj = datetime.strptime(dados[5], '%d/%m/%Y').date()
                nasc.set_date(data_nascimento_obj)
            except ValueError:
                pass # Data inválida ou vazia
        
        entry_endereco.delete(0, END)
        entry_endereco.insert(0, dados[7])
        
        combo_curso.set(dados[8])
        
        imagem_string = dados[9]
        if imagem_string:
            try:
                imagem = Image.open(imagem_string)
                imagem = imagem.resize((130, 130))
                imagem = ImageTk.PhotoImage(imagem)
                l_imagem.config(image=imagem)
                l_imagem.image = imagem
                botao_carregar['text'] = "Alterar Imagem"
            except Exception:
                l_imagem.config(image="") 
                l_imagem.image = None
        else:
            l_imagem.config(image="")
            l_imagem.image = None
                
    except IndexError:
        pass

# --- Buttons ---
# Now that functions are defined, we create buttons
botao_carregar = Button(frame_detalhes, text="Carregar Imagem", command=escolher_imagem, 
                        font="verdana 10 bold", fg="white", bg="steelblue", 
                        activebackground="green", bd=2, anchor="center", overrelief=RIDGE)
botao_carregar.place(x=650, y=160)

botao_novo = Button(frame_botoes, command=limpar_campos, text="Novo", width=10, 
                   font="verdana 10 bold", fg="white", bg="steelblue", 
                   activebackground="green", anchor="center", overrelief=RIDGE)
botao_novo.grid(row=0, column=0, padx=10, pady=10, sticky="w")

botao_adicionar = Button(frame_botoes, command=adicionar_aluno, text="Adicionar", width=10, 
                        font="verdana 10 bold", fg="white", bg="steelblue", 
                        activebackground="green", anchor="center", overrelief=RIDGE)
botao_adicionar.grid(row=1, column=0, padx=10, pady=10, sticky="w")

botao_atualizar = Button(frame_botoes, command=atualizar_aluno, text="Atualizar", width=10, 
                        font="verdana 10 bold", fg="white", bg="steelblue", 
                        activebackground="green", anchor="center", overrelief=RIDGE)
botao_atualizar.grid(row=2, column=0, padx=10, pady=10, sticky="w")

botao_deletar = Button(frame_botoes, command=deletar_aluno, text="Deletar", width=10, 
                      font="verdana 10 bold", fg="white", bg="steelblue", 
                      activebackground="green", anchor="center", overrelief=RIDGE)
botao_deletar.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# --- Bindings & Initial Load ---
tree_aluno.bind("<<TreeviewSelect>>", selecionar_aluno)
mostrar_alunos() # Initial load

app.mainloop()