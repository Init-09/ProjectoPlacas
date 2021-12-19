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
from tkinter import messagebox
from tkinter.constants import S
import pytesseract

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

            def reportocacional(self,tickets): 
                sql="select * from usuarios_ocacionales where Tiket LIKE '%{}%'".format(tickets)
                try:
                    self.cursor.execute(sql)
                    Autos = self.cursor.fetchone()                       
                    placaticket.delete(0, 'end')
                    placaticket.insert(1, Autos[1])    
                    entradaticket.delete(0, 'end')
                    entradaticket.insert(1, Autos[2])  
                    salidaticket.delete(0, 'end')
                    salidaticket.insert(1, Autos[3])  
                    costoticket.delete(0, 'end')
                    costoticket.insert(1, Autos[4])                  
                    return
                except Exception as e:
                    raise

            def reportrecurrent(self,placa): 
                sql="select * from usuarios_recurrentes where Placa LIKE '%{}%'".format(placa)
                try:
                    self.cursor.execute(sql)
                    Autos = self.cursor.fetchone()                       
                    placanombre.delete(0, 'end')
                    placanombre.insert(1, Autos[1])    
                    placamodelo.delete(0, 'end')
                    placamodelo.insert(1, Autos[2])  
                    placaanio.delete(0, 'end')
                    placaanio.insert(1, Autos[3])  
                    placapago.delete(0, 'end')
                    checdia = Autos[4]
                    if (int(checdia) > 0):
                        placapago.insert(1, "Pago al dia")   
                    else: 
                        placapago.insert(1, "Pago retrasado")
                    return
                except Exception as e:
                    raise



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
            def update_record(self,tickets,salida, valor):   
                    sql="UPDATE usuarios_ocacionales SET Salida = '{}', Valortiket = '{}' WHERE usuarios_ocacionales.Tiket = '{}'".format(salida,valor,tickets)
                    try:
                        self.cursor.execute(sql)
                        self.connection.commit()   
                        messagebox.showinfo("inf", "Registro exitoso")   
                        ShowPlaca.delete(0,'end')
                        ShowPlaca.insert(1, 'Placa')
                        ValorTime.delete(0,'end')
                        ValorTime.insert(1, 'Fecha/Hora')
                        ShowTicket.delete(0,'end')
                        ShowTicket.insert(1, 'Ticket')
                        EntradaShow.delete(0,'end')
                        EntradaShow.insert(1, 'Entrada')
                        SalidaShow.delete(0,'end')
                        SalidaShow.insert(1, 'Salida')
                        Total.delete(0,'end')
                        Total.insert(1, 'Costo total')                         
                        return
                    except Exception as e:
                        raise
            def show_record(self,placa):           
                    sql="select * from usuarios_recurrentes where Placa LIKE '%{}%'".format(placa)
                    try:
                        self.cursor.execute(sql)
                        rows_count = self.cursor.execute(sql)
                        if rows_count >0:
                            Autos = self.cursor.fetchone()                                       
                            Placa = Autos[0]
                            Nombre = Autos[1]                    
                            Modelo = Autos[2]
                            Anio = Autos[3]
                            Pago = Autos[4]
                            print("_______________")
                            print("Placa:",Placa)
                            print("Nombre:",Nombre)
                            print("Modelo:",Modelo)
                            print("Año:",Anio)
                            print("Pago:",Pago)
                            print("_______________")
                            if (Pago > 0):
                                messagebox.showinfo("inf", "Al dia, adelante")
                            if (Pago == 0):                            
                                sql="SELECT * FROM usuarios_ocacionales WHERE Placa LIKE '%{}%' AND `Salida` = '0000-00-00 00:00:00'".format(placa)
                                try:
                                    rows_count = self.cursor.execute(sql)
                                    if rows_count >0:
                                        self.cursor.execute(sql)
                                        Autos = self.cursor.fetchone()      
                                        print("_______________")
                                        print("Ticket:",Autos[0])
                                        print("Placa:",Autos[1])
                                        print("Ingreso:",Autos[2])
                                        print("Salida:",Autos[3])
                                        print("Total:",Autos[4])
                                        print("_______________")
                                        EntradaShow.delete(0,'end')
                                        EntradaShow.insert(1,Autos[2])
                                        ShowTicket.delete(0,'end')
                                        ShowTicket.insert(1,Autos[0])
                                        now = datetime.now()
                                        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
                                        SalidaShow.delete(0,'end')
                                        SalidaShow.insert(1,date_time)                                          
                                    else:
                                        messagebox.showinfo("inf", "Por favor entrar como usuario ocasional, genere un ticket por favor")                                                                      

                                    return
                                except Exception as e:
                                    raise
                        else:
                            sql="SELECT * FROM usuarios_ocacionales WHERE Placa LIKE '%{}%' AND `Salida` = '0000-00-00 00:00:00'".format(placa)
                            try:
                                rows_count = self.cursor.execute(sql)
                                if rows_count >0:
                                    self.cursor.execute(sql)
                                    Autos = self.cursor.fetchone()      
                                    print("_______________")
                                    print("Ticket:",Autos[0])
                                    print("Placa:",Autos[1])
                                    print("Ingreso:",Autos[2])
                                    print("Salida:",Autos[3])
                                    print("Total:",Autos[4])
                                    print("_______________")
                                    EntradaShow.delete(0,'end')
                                    EntradaShow.insert(1,Autos[2])
                                    ShowTicket.delete(0,'end')
                                    ShowTicket.insert(1,Autos[0])
                                    now = datetime.now()
                                    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
                                    SalidaShow.delete(0,'end')
                                    SalidaShow.insert(1,date_time)                                          
                                else:
                                    messagebox.showinfo("inf", "Por favor entrar como usuario ocasional, genere un ticket por favor")                                                                      

                                return
                            except Exception as e:
                                raise
                            
                        return
                    except Exception as e:
                        raise

            def insert_record(self,tickets,placa, fecha):           
                    sql="INSERT INTO usuarios_ocacionales (Tiket, Placa, Ingreso, Salida, Valortiket) VALUES ('{}', '{}', '{}', '', '');".format(tickets,placa,fecha)
                    try:
                        self.cursor.execute(sql)
                        self.connection.commit()   
                        messagebox.showinfo("inf", "Registro exitoso")
                        ShowPlaca.delete(0,'end')
                        ShowPlaca.insert(1, 'Placa')
                        ValorTime.delete(0,'end')
                        ValorTime.insert(1, 'Fecha/Hora')
                        ShowTicket.delete(0,'end')
                        ShowTicket.insert(1, 'Ticket')
                        EntradaShow.delete(0,'end')
                        EntradaShow.insert(1, 'Entrada')
                        SalidaShow.delete(0,'end')
                        SalidaShow.insert(1, 'Salida')
                        Total.delete(0,'end')
                        Total.insert(1, 'Costo total')                            
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
                    image = cv2.imread('placa.jpg')
                    frame = image
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
        self.label.grid(row=0, column=0, pady=10, columnspan=4)


        # Label
        self.label = ttk.Label(
            self.tab_1,
            text="Entrada / Salida",
            justify="center",
            font=("-size", 15, "-weight", "bold"),
        )
        self.label.grid(row=2, column=0, pady=10, columnspan=2, sticky="nsew")

####################################################################################################
        def leerplaca():
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
            placa = []
            image = cv2.imread('placa.jpg')
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray = cv2.blur(gray,(3,3))
            canny = cv2.Canny(gray,150,200)
            canny = cv2.dilate(canny,None,iterations=1)
            cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
            for c in cnts:
                area = cv2.contourArea(c)
                x,y,w,h = cv2.boundingRect(c)
                epsilon = 0.06*cv2.arcLength(c,True)
                approx = cv2.approxPolyDP(c,epsilon,True)
                if len(approx)==4 and area>9000:
                    print('area=',area)
                    placa = gray[y:y+h,x:x+w]
                    text = pytesseract.image_to_string(placa)
                    print('PLACA: ',text)

            ShowPlaca.delete(0, 'end')
            ShowPlaca.insert(1, text)
            
            ValorTime.delete(0, 'end')
            now = datetime.now()
            date_time = now.strftime("%Y-%m-%d %H:%M:%S")
            ValorTime.insert(1, date_time)
            



         # Button
        self.button = ttk.Button(self.tab_1, text="Leer imagen", command=leerplaca)
        self.button.grid(row=2, column=2, padx=5, pady=10, sticky="nsew")
        # Button
        self.button = ttk.Button(self.tab_1, text="On / Off", command=iniciar)
        self.button.grid(row=2, column=3, padx=5, pady=10, sticky="nsew")

        # Tab #2
        self.tab_2 = ttk.Frame(self.notebook)
        for index in [0, 1]:
            self.tab_2.columnconfigure(index=index, weight=1)
            self.tab_2.rowconfigure(index=index, weight=5)        
        self.notebook.add(self.tab_2, text="Reporte de concurrentes")

         
        # Label
        self.label = ttk.Label(
            self.tab_2,
            text="Reporte por Cliente",
            justify="center",
            font=("-size", 15, "-weight", "bold"),
        )
        self.label.grid(row=0, column=0, pady=10, columnspan=2, sticky="nsew")

        
        # Entry
        Pplaca=self.entry = ttk.Entry(self.tab_2)
        self.entry.insert(0, "Placa a buscar")        
        self.entry.grid(row=0, column=2, padx=5, pady=(0, 10), sticky="nsew") 
        # Entry
        placanombre=self.entry = ttk.Entry(self.tab_2)
        self.entry.insert(0, "Nombre")        
        self.entry.grid(row=3, column=0, padx=5, pady=(0, 10), sticky="nsew") 
        # Entry
        placamodelo=self.entry = ttk.Entry(self.tab_2)
        self.entry.insert(0, "Modelo")        
        self.entry.grid(row=4, column=0, padx=5, pady=(0, 10), sticky="nsew") 
        # Entry
        placaanio=self.entry = ttk.Entry(self.tab_2)
        self.entry.insert(0, "Año")        
        self.entry.grid(row=5, column=0, padx=5, pady=(0, 10), sticky="nsew") 
        # Entry
        placapago=self.entry = ttk.Entry(self.tab_2)
        self.entry.insert(0, "Pago al dia")        
        self.entry.grid(row=6, column=0, padx=5, pady=(0, 10), sticky="nsew") 

        def reporterecuren():
            enviar = Pplaca.get()
            obj_db1.reportrecurrent(enviar)
          # Button
        self.button = ttk.Button(self.tab_2, text="Generar reporte", command=reporterecuren)
        self.button.grid(row=6, column=2, padx=5, pady=10, sticky="nsew")

        

        # Tab #3
        self.tab_3 = ttk.Frame(self.notebook)
        for index in [0, 1]:
            self.tab_3.columnconfigure(index=index, weight=1)
            self.tab_3.rowconfigure(index=index, weight=1)
        self.notebook.add(self.tab_3, text="Reporte de ticekt ocacional")
        
        
        # Label
        self.label = ttk.Label(
            self.tab_3,
            text="Reporte por Ticket",
            justify="center",
            font=("-size", 15, "-weight", "bold"),
        )
        self.label.grid(row=0, column=0, pady=10, columnspan=2, sticky="nsew")

        
        # Entry
        Tticket=self.entry = ttk.Entry(self.tab_3)
        self.entry.insert(0, "Ticket a buscar")        
        self.entry.grid(row=0, column=2, padx=5, pady=(0, 10), sticky="nsew") 
        # Entry
        placaticket=self.entry = ttk.Entry(self.tab_3)
        self.entry.insert(0, "Placa")        
        self.entry.grid(row=3, column=0, padx=5, pady=(0, 10), sticky="nsew") 
        # Entry
        entradaticket=self.entry = ttk.Entry(self.tab_3)
        self.entry.insert(0, "Entrada")        
        self.entry.grid(row=4, column=0, padx=5, pady=(0, 10), sticky="nsew") 
        # Entry
        salidaticket=self.entry = ttk.Entry(self.tab_3)
        self.entry.insert(0, "Salida")        
        self.entry.grid(row=5, column=0, padx=5, pady=(0, 10), sticky="nsew") 
        # Entry
        costoticket=self.entry = ttk.Entry(self.tab_3)
        self.entry.insert(0, "Gasto Total")        
        self.entry.grid(row=6, column=0, padx=5, pady=(0, 10), sticky="nsew") 

        def reporteocacional():
            enviar = Tticket.get()
            obj_db1.reportocacional(enviar)            
       

          # Button
        self.button = ttk.Button(self.tab_3, text="Generar reporte", command=reporteocacional)
        self.button.grid(row=6, column=2, padx=5, pady=10, sticky="nsew")
        # Button

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
            check = ShowTicket.get()
            if check == "Ticket":
                ShowTicket.delete(0, 'end')
                ShowTicket.insert(1, ticket)
            else:                
                messagebox.showinfo("inf", "Ya tiene ticket")


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
        

        def registrarsalida():            
            ticket = ShowTicket.get()
            salida = SalidaShow.get() 
            valor = Total.get() 
            if (valor=="Costo total"):
                messagebox.showinfo("inf", "Primero calcule el costo del ticket") 
            else:
                obj_db1.update_record(ticket,salida,valor)                

        # Accentbutton
        self.accentbutton = ttk.Button(
            self.radio_frame, text="Registrar Salida", style="Accent.TButton", command=registrarsalida
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


        def revisardatosdellector():           
            placa = ShowPlaca.get() 
            obj_db1.show_record(placa)     

        # Button
        self.button = ttk.Button(self.widgets_frame, text="Analizar", command=revisardatosdellector)
        self.button.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")
        

        def registrarentrada():           
            fechaentrada=EntradaShow.get()
            ticket = ShowTicket.get()
            placa = ShowPlaca.get() 
            fecha = ValorTime.get() 
            if (ticket=="Ticket"):
                messagebox.showinfo("inf", "Primero genere ticket") 
            else:
                if (fechaentrada=="Entrada"):
                    obj_db1.insert_record(ticket,placa,fecha) 
                else:
                    messagebox.showinfo("inf", "Debe registrar salida no entrada")
                    

        # Accentbutton
        self.accentbutton = ttk.Button(
            self.widgets_frame, text="Registrar Entrada", style="Accent.TButton", command=registrarentrada
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