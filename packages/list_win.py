import win32gui

aval = []
in_aval = 0

currect_dict = {'y','yah','yupp','true','1','yes','ye'}
run = True

def switcher():
    global in_aval,run
    while run:
        in_aval = 0
        def winEnumHandler( hwnd, ctx ):
            global in_aval
            if win32gui.IsWindowVisible( hwnd ):
                if win32gui.GetWindowText( hwnd ) != '':
                    print(in_aval,".",win32gui.GetWindowText( hwnd ))
                    aval.append(str(win32gui.GetWindowText( hwnd )))
                    in_aval += 1

        print("\nSelect anyone for writing.\n------------------------------\n")
        win32gui.EnumWindows( winEnumHandler, None )
        try:
            s = int(input("\n----------------------------\nWindow number:_"))
            print("You have selected:_",aval[s])
            if str(input("\nR u sure??_")).lower() in currect_dict:
                hwnd = win32gui.FindWindow(None, aval[s]) 
                win32gui.ShowWindow(hwnd,5)
                win32gui.SetForegroundWindow(hwnd)
                run = False
        
        except:
            pass