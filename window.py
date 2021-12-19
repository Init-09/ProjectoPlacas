import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter.constants import OFF
import pymysql
from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
from datetime import datetime
import string
import random
from datetime import datetime
from tkinter.constants import S

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create value lists
        self.option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
        self.combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
        self.readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

        # Create control variables
        self.var_0 = tk.BooleanVar()
        self.var_1 = tk.BooleanVar(value=True)
        self.var_2 = tk.BooleanVar()
        self.var_3 = tk.IntVar(value=2)
        self.var_4 = tk.StringVar(value=self.option_menu_list[1])
        self.var_5 = tk.DoubleVar(value=75.0)

        # Create widgets :)
        self.setup_widgets()

    def setup_widgets(self):
        global Placa
        global Nombre
        global Email

        class DataBase:            
            
            def __init__(self):
                self.connection=pymysql.connect(
                    host='MYSQL5034.site4now.net',
                    user='a7df43_atzel09',
                    password='1q2w3e4r',
                    db='db_a7df43_atzel09'
                )
                self.cursor = self.connection.cursor()
                print("--------------")
                print("Conexion Exitosa!!!")
                print("#################")

            def show_one_record(self):                
                sql="select * from usuarios_ocacionales where Placa LIKE 'HAB2649'"
                try:
                    self.cursor.execute(sql)
                    Autos = self.cursor.fetchone()   
                    Ticket = Autos[0]                                     
                    Placa = Autos[1]
                    Ingreso = Autos[2]                    
                    Salida = Autos[3]
                    Valor = Autos[4]
                    ShowPlaca.delete(0, 'end')
                    ShowPlaca.insert(1, Autos[1])
                    ValorTime.delete(0, 'end')
                    now = datetime.now()
                    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
                    ValorTime.insert(1, date_time)
                    # ShowNombre.delete(0, 'end')
                    # ShowNombre.insert(1, Autos[1])
                    # ShowEmail.delete(0, 'end')
                    # ShowEmail.insert(1, Autos[2])
                    print("_______________")
                    print("Ticket:",Ticket)
                    print("Placa:",Placa)
                    print("Ingreso:",Ingreso)
                    print("Salida:",Salida)
                    print("Valor:",Valor)
                    print("_______________")
                    return
                except Exception as e:
                    raise
        obj_db1 = DataBase()

        # Panedwindow
        self.paned = ttk.PanedWindow(self)
        self.paned.grid(row=0, column=0, pady=(0, 0), sticky="nsew", rowspan=3)


        # Notebook, pane #2
        self.pane_1 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_1, weight=3)

        # Notebook, pane #2
        self.notebook = ttk.Notebook(self.pane_1)
        self.notebook.pack(fill="both", expand=True)

        # Tab #1
        self.tab_1 = ttk.Frame(self.notebook)
        for index in [0, 1]:
            self.tab_1.columnconfigure(index=index, weight=1)
            self.tab_1.rowconfigure(index=index, weight=5)
        self.notebook.add(self.tab_1, text="Camara")

        #Imagenvideos
        def iniciar():
            global cap
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            visualizar()
        def visualizar():
            
            global cap
            if cap is not None:
                ret, frame = cap.read()
                if ret == True:
                    frame = imutils.resize(frame, width=640)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                    im = Image.fromarray(frame)
                    img = ImageTk.PhotoImage(image=im)

                    labelimg.configure(image=img)
                    labelimg.image = img
                    labelimg.after(10, visualizar)
                else:
                    labelimg.image = ""
                    cap.release()
        def finalizar():
            global cap
            cap.release()
        cap = None
        # Label
        labelimg = self.label = ttk.Label(                     
            self.tab_1,           
        )
        labelimg.pack()
        self.label.grid(row=0, column=0, pady=10, columnspan=2)


        # Label
        self.label = ttk.Label(
            self.tab_1,
            text="Entrada / Salida",
            justify="center",
            font=("-size", 15, "-weight", "bold"),
        )
        self.label.grid(row=2, column=0, pady=10, columnspan=2, sticky="nsew")

        # Button
        self.button = ttk.Button(self.tab_1, text="On / Off", command=iniciar)
        self.button.grid(row=2, column=1, padx=5, pady=10, sticky="nsew")

        # Tab #2
        self.tab_2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_2, text="Reporte de concurrentes")

        

        # Tab #3
        self.tab_3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_3, text="Reporte de ticekt ocacional")

        # Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))









############################################################################################################

        # Create a Frame for the Checkbuttons
        self.check_frame = ttk.LabelFrame(self, text="Ticket", padding=(20, 10))
        self.check_frame.grid(
            row=0, column=4, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )
         # Entry
        ShowTicket = self.entry = ttk.Entry(self.check_frame)
        self.entry.insert(0, "Ticket")        
        self.entry.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="nsew") 
        
        def ticket():
            length_of_string = 8
            ticket=""
            ticket=ticket.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
            ShowTicket.delete(0, 'end')
            ShowTicket.insert(1, ticket)


        # Accentbutton
        self.accentbutton = ttk.Button(
            self.check_frame, text="Generar", style="Accent.TButton", command=ticket
        )
        self.accentbutton.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")



        def calcularelcosto():
            s = SalidaShow.get()
            s = str(s)
            Salida = datetime.fromisoformat(s)
            s1 = EntradaShow.get()
            s1 = str(s1)
            Entrada = datetime.fromisoformat(s1)
            diferencia = (Salida - Entrada)
            diferencia = (round(diferencia.total_seconds() * 0.000277778))*12
            diferencia = str(diferencia) + " Lps"
            Total.delete(0,'end')
            Total.insert(1,diferencia)


        # Accentbutton
        self.accentbutton = ttk.Button(
            self.check_frame, text="Calcular Costo", style="Accent.TButton", command=calcularelcosto
        )
        self.accentbutton.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")               
       

        # Separator
        self.separator = ttk.Separator(self)
        self.separator.grid(row=1, column=4, padx=(20, 10), pady=10, sticky="ew")

        # Create a Frame for the Radiobuttons
        self.radio_frame = ttk.LabelFrame(self, text="Valor de ticket", padding=(20, 10))
        self.radio_frame.grid(row=2, column=4, padx=(20, 10), pady=10, sticky="nsew")

          # Entry
        EntradaShow=self.entry = ttk.Entry(self.radio_frame)
        self.entry.insert(0, "Entrada")        
        self.entry.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="nsew") 
        
          # Entry
        SalidaShow=self.entry = ttk.Entry(self.radio_frame)
        self.entry.insert(0, "Salida")        
        self.entry.grid(row=2, column=0, padx=5, pady=(0, 10), sticky="nsew") 

          # Entry
        Total = self.entry = ttk.Entry(self.radio_frame)
        self.entry.insert(0, "Costo total")        
        self.entry.grid(row=3, column=0, padx=5, pady=(0, 10), sticky="nsew") 
        
        # Accentbutton
        self.accentbutton = ttk.Button(
            self.radio_frame, text="Registrar Salida", style="Accent.TButton"
        )
        self.accentbutton.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")        
       

        

        # Create a Frame for input widgets
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(
            row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)


        # Entry
        ShowPlaca = self.entry = ttk.Entry(self.widgets_frame)
        self.entry.insert(0, "Placa")
        self.entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")


        # Entry
        ValorTime = self.entry = ttk.Entry(self.widgets_frame)
        self.entry.insert(0, "Fecha/Hora")
        self.entry.grid(row=5, column=0, padx=5, pady=(0, 10), sticky="ew")

        # Button
        self.button = ttk.Button(self.widgets_frame, text="Obtener lectura")
        self.button.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

        # Accentbutton
        self.accentbutton = ttk.Button(
            self.widgets_frame, text="Registrar Entrada", style="Accent.TButton", command=obj_db1.show_one_record
        )
        self.accentbutton.grid(row=7, column=0, padx=5, pady=10, sticky="nsew")



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema de control de placas de vehiculos en estacionamiento")

    # Simply set the theme
    root.tk.call("source", "sun-valley.tcl")
    root.tk.call("set_theme", "dark")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

    root.mainloop()