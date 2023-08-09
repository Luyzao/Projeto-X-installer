import os
import PySimpleGUI as sg

try:

    os.system("powershell choco")

except:

    os.system("powershell Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))")

else:

    sg.theme('Dark Red 1')

    BAR_MAX = 1000

    # layout the Window
    layout = [[sg.Text('Carregando sistema')],
            [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,20), key='-PROG-')],
            [sg.Cancel('Cancelar')]]

    # create the Window
    window = sg.Window('X-Installer - v1.0', layout)
    # loop that would normally do something useful
    for i in range(1000):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = window.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            exit()
            # update bar with loop value +1 so that bar eventually reaches the maximum
        window['-PROG-'].update(i+1)
    # done with loop... need to destroy the window as it's still open
    window.close()

    tab1_layout = [[sg.Text('Seleciones os programas que deseja baixar',justification='center', font=('Helvetica', 16))],      
        
                [sg.Text('_'  * 100, size=(65, 1))],      
                [sg.Text('Programas', font=('Helvetica', 15), justification='left')],      
                [sg.Checkbox('Opera', size=(12, 1), default=True), sg.Checkbox('chrome', size=(20, 1))],      
                [sg.Checkbox('winrar', size=(12, 1)), sg.Checkbox('epic games', size=(20, 1), default=True)],      
                [sg.Checkbox('steam', size=(12, 1)), sg.Checkbox('operagx', size=(20, 1))],      
    ]    

    tab2_layout = [[sg.Text('Seleciones os programas que deseja baixar',justification='center', font=('Helvetica', 16))],      
        
                   
    ]   

    layout = [[sg.TabGroup([[sg.Tab('Inicio', tab1_layout, tooltip='tip'), sg.Tab('Sobre', tab2_layout)]], tooltip='TIP2')],    
            [sg.Button('Instalar'),sg.Cancel('Sair')]]    

    window = sg.Window('X-Installer - v1.0', layout, default_element_size=(12,1))    

    while True:    
        event, values = window.read()    
        print(event,values)   

        if event == 'Sair' or event == sg.WIN_CLOSED:
            exit()
            
        else:
            
            if values[0] == True:
                a = 'opera'
            else:
                a = ''

            if values[1] == True:
                b = 'googlechrome'
            else:
                b = ''

            if values[2] == True:
                c = 'winrar'
            else:
                c = ''

            if values[3] == True:
                d = 'epicgameslauncher'
            else:
                d = ''

            if values[4] == True:
                e = 'steam'
            else:
                e = ''

            if values[5] == True:
                f = 'opera-gx'
            else:
                f = ''


            if a != '' or b != '' or c != '' or d != '' or e != '' or f != '':
                os.system(f"powershell choco install {a} {b} {c} {d} {e} {f} -y")
                
