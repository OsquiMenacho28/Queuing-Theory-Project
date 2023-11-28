import tkinter as tk
from tkinter import ttk
import screen_config
import MMS_Model as MMS

class ResultsWindow(tk.Toplevel):
    averageQueueLengthResult: float

    def __init__(self, parent, averageQueueLengthResult):
        super().__init__(parent)
        self.averageQueueLengthResult = averageQueueLengthResult
        screen_config.setWindowInCenterOfScreen(self)
        self.title("RESULTADOS - MODELO M/M/S>1")
        ttk.Label(
            self, 
            text="RESULTADOS", 
            background="light yellow", 
            font=("Courier 20"), 
            width=100,
            justify="center"
            ).pack(expand=True)
        averageQueueLengthLabel = ttk.Label(self, font=("Courier", 10))
        averageQueueLengthLabel.pack(expand=True)
        averageQueueLengthLabel.config(text=f"Longitud promedio de la cola: {averageQueueLengthResult}")
        tk.Button(
            self, 
            text="OK", 
            command=self.destroy, 
            background="lawn green",
            activebackground="dodger blue"
            ).pack(expand=True)

class MMSModelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        screen_config.setWindowInCenterOfScreen(self)
        self.title("TEORÍA DE COLAS - MODELO CASO 2 - M/M/S>1")
        tk.Label(self, text="Ingresa Lambda (λ) :", font=("Courier", 10)).pack(expand=True)
        lambdaEntry = ttk.Entry(self, justify="center")
        lambdaEntry.focus()
        lambdaEntry.pack(expand=True)
        tk.Label(self, text="Ingresa Mi (µ) :", font=("Courier", 10)).pack(expand=True)
        miEntry = ttk.Entry(self, justify="center")
        miEntry.pack(expand=True)
        tk.Label(self, text="Ingresa el número de servidores (s) :", font=("Courier", 10)).pack(expand=True)
        serversEntry = ttk.Entry(self, justify="center")
        serversEntry.pack(expand=True)

        def open_results():
            if lambdaEntry.get() == "" or miEntry.get() == "" or serversEntry.get() == "":
                pass
            else:
                model = MMS.MMS(float(lambdaEntry.get()), float(miEntry.get()), int(serversEntry.get()))
                averageQueueLength = round(model.averageQueueLength(0), 4)
                lambdaEntry.delete(0, "end")
                miEntry.delete(0, "end")
                serversEntry.delete(0, "end")
                window = ResultsWindow(self, averageQueueLength)
                window.grab_set()
        
        tk.Button(
            self, 
            text="CALCULAR", 
            command=open_results,
            background="green yellow",
            activebackground="light sky blue"
            ).pack(expand=True)

def initialize():
    app = MMSModelApp()
    app.mainloop()