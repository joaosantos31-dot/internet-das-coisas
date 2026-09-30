import customtkinter as ctk

ctk.set_appearance_mode("dark")

def calcular():
    try:
        a = float(primeiranota.get())
        b = float(segundanota.get())
        c = float(terceiranota.get())
    except ValueError:
        resultado.configure(text='Por gentileza digite uma nota válida!!!', text_color='yellow')
        return

    formula = (a + b + c) / 3

    if a > 10 or a < 0 or b > 10 or b < 0 or c > 10 or c < 0:
        resultado.configure(text='Por gentileza digite uma nota válida!!!', text_color='yellow')

    elif formula >= 5:
        resultado.configure(text=f"O aluno está aprovado!!!\nO resultado das notas é: {formula:.2f}")

    else:
        resultado.configure(text=f"O aluno está reprovado!!!\nO resultado das notas é: {formula:.2f}")

janela = ctk.CTk()
janela.geometry('600x600')
janela.title('Sistema Escolar 2026')
janela.iconbitmap('aula30/09/book_science_on_school_knowledge_university_learning_education_lockers_icon_266648.ico')

titulo = ctk.CTkLabel(janela,
                      text='\n\nSISTEMA ESCOLA',
                      text_color='yellow',
                      font=('Times new roman', 30))
titulo.pack()

primeiranota = ctk.CTkEntry(janela,
                            width=400,
                            height=40,
                            border_color='yellow',
                            placeholder_text='Digite a 1º nota: ')
primeiranota.pack(pady=20)

segundanota = ctk.CTkEntry(janela,
                           width=400,
                           height=40,
                           border_color='yellow',
                           placeholder_text='Digite a 2º nota: ')
segundanota.pack(pady=20)

terceiranota = ctk.CTkEntry(janela,
                            width=400,
                            height=40,
                            border_color='yellow',
                            placeholder_text='Digite a 3º nota: ')
terceiranota.pack(pady=20)

botao = ctk.CTkButton(janela,
                      width=200,
                      height=40,
                      text='Calcular',
                      fg_color="#000000",
                      text_color='yellow',
                      command=calcular,
                      cursor='hand2')
botao.pack(pady=20)

resultado = ctk.CTkLabel(janela,
                         font=('Times new roman', 20),
                         text='',
                         text_color='yellow')
resultado.pack(pady=20)

janela.mainloop()