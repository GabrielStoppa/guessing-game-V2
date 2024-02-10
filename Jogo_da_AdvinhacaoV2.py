import random
import PySimpleGUI as sg

def iniciar_jogo_adivinhacao():
    n_random = random.randint(0, 10)
    regra = """ 
    AS REGRAS SÃO SIMPLES SÃO ELAS:
    1- VOCÊ TERÁ 3 TENTATIVAS PARA ACERTAR
    2- TENTE ACERTAR O NÚMERO ENTRE 0 E 10
    """

    sg.theme('DarkAmber')
    layout = [
        [sg.Text('SEJA BEM-VINDO AO JOGO DA ADIVINHAÇÃO!', size=(50, 1), font=('Helvetica', 10), justification='center')],
        [sg.Text(regra, size=(50, 5), font=('Helvetica', 9), justification='center')],
        [sg.Button('Iniciar Jogo'), sg.Button('Sair')]
    ]

    window = sg.Window('JOGO DA ADIVINHAÇÃO!', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Sair':
            break
        elif event == 'Iniciar Jogo':
            total_tentativa = 3

            for x in range(1, total_tentativa + 1):
                guess_layout = [
                    [sg.Text(f'Tentativa {x} de {total_tentativa}', key='tentativa', size=(30, 1), font=('Helvetica', 12), justification='center')],
                    [sg.Text("O número foi sorteado! Qual foi ele?"), sg.InputText(key='guess')],
                    [sg.Button('Enviar'), sg.Button('Sair')]
                ]

                guess_window = sg.Window(f'Tentativa {x}', guess_layout)

                while True:
                    guess_event, guess_values = guess_window.read()

                    if guess_event == sg.WIN_CLOSED or guess_event == 'Sair':
                        break
                    elif guess_event == 'Enviar':
                        try:
                            numero = int(guess_values['guess'])
                            assert 0 <= numero <= 10, "O número deve estar entre 0 e 10"

                            if numero == n_random:
                                sg.popup(f'Você Acertou! O número sorteado foi {n_random}', title='Fim de Jogo')
                                break
                            else:
                                feedback = "Eita! Calma lá amigão, talvez o buraco seja mais lá embaixo..." if numero > n_random else "Eita! Que tal subir uns degraus?"
                                sg.popup_error(feedback, title='Erro')
                        except ValueError:
                            sg.popup_error("Por favor, insira um número válido.", title='Erro')
                        except AssertionError as e:
                            sg.popup_error(str(e), title='Erro')

                guess_window.close()

    window.close()

iniciar_jogo_adivinhacao()
