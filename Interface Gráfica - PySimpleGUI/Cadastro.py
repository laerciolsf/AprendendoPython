from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')

layout = [
        [sg.Text('Usuario'),sg.Input(key='usuario')],
        [sg.Text('Senha'),sg.Input(key='senha',password_char='*')],
        [sg.Checkbox('Salvar o login?')],
        [sg.Button('Entrar')]
    ]

#janela
janela = sg.Window('Tela de Login',layout)

#Ler os Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Laio' and valores['senha'] == '1234':
            print('Sucesso!')




         
