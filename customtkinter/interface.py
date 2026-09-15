import customtkinter as ctk
ctk.set_appearance_mode('dark')

janela = ctk.CTk()
janela.geometry('500x500')
janela.title('carteira de trabalho')
janela.iconbitmap('customtkinter/security-protection-protect-key-password-login_108554.ico')

titulo = ctk.CTkLabel(janela,
                      text='\n\nSISTEMA DE LOGIN',
                      text_color='#ffffff',
                      font=('Times new roman',40))
titulo.pack()

login = ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     border_color='#ffffff',
                     placeholder_text='Digite o seu Login: ')
login.pack(pady=40)

senha = ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     border_color='#ffffff',
                     placeholder_text='Digite a sua Senha: ',
                     show='*')
senha.pack(pady=10)

botao = ctk.CTkButton(janela,
                      width=200,
                      height=40,
                      text='Acessar',
                      fg_color="#000000",
                      text_color='#ffffff',
                      cursor='hand2')
botao.pack(pady=30)

janela.mainloop()