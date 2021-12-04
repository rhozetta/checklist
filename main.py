import PySimpleGUI as sg
import os
import json

def getlists():
    lists = os.listdir("lists")

    y = []
    for x in lists:
        y.append(x.replace(".json", ""))
    return y

lists = getlists()

main = [[sg.Listbox(values=lists, size=(30, 6), bind_return_key=True, key='-LIST-')],
        [sg.Button('Open')],
        [sg.Text("")],
        [sg.Text("Name your new checklist")],
        [sg.Input(do_not_clear=False)],
        [sg.Button('Add')] ]

window = sg.Window('Checklists', main, finalize=True)

template = {'not done':False,'done':True}

while True:
    lists = getlists()

    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Add':
        print(values)
        list = open(f"lists/{values[0]}.json", "w")
        list.write(json.dumps(template))
        list.close()

        lists.append(values[0])

        window["-LIST-"].update(values=lists)
        window.finalize()
    elif event != 'Add':
        list = open(f"lists/{values['-LIST-'][0]}.json", "r")
        print(list.read())

window.close()