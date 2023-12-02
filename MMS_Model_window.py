import tkinter as tk
from tkinter import ttk
import screen_config
import MMS_Model as MMS

class ResultsWindow(tk.Toplevel):
    utilizationFactorResult: float
    probabilityThatThereAreNoClientsInSystemResult: float
    averageQueueLengthResult: float
    averageWaitingTimeInQueueResult: float
    averageSystemLengthResult: float
    averageWaitingTimeInSystemResult: float
    probabilityThatThereAreNClientsInABusySystemResult: float

    def __init__(self, parent, utilizationFactorResult, probabilityThatThereAreNoClientsInSystemResult, 
                 averageQueueLengthResult, averageWaitingTimeInQueueResult, averageSystemLengthResult, 
                 averageWaitingTimeInSystemResult, probabilityThatThereAreNClientsInABusySystemResult):
        super().__init__(parent)

        self.utilizationFactorResult = utilizationFactorResult
        self.probabilityThatThereAreNoClientsInSystemResult = probabilityThatThereAreNoClientsInSystemResult
        self.averageQueueLengthResult = averageQueueLengthResult
        self.averageWaitingTimeInQueueResult = averageWaitingTimeInQueueResult
        self.averageSystemLengthResult = averageSystemLengthResult
        self.averageWaitingTimeInSystemResult = averageWaitingTimeInSystemResult
        self.probabilityThatThereAreNClientsInABusySystemResult = probabilityThatThereAreNClientsInABusySystemResult

        screen_config.setWindowInCenterOfScreen(self, 800, 500)
        self.title("RESULTADOS")
        ttk.Label(
            self, 
            text="RESULTADOS - MODELO M/M/S>1", 
            background="spring green", 
            font=("Courier", 20), 
            justify="center"
            ).pack(expand=True)
        setResult(self, f"Factor de utilización (p): {round(utilizationFactorResult * 100, 2)}%")
        setResult(self, f"Probabilidad de que hayan 0 clientes en el sistema (Po): {round(probabilityThatThereAreNoClientsInSystemResult * 100, 2)}%")
        setResult(self, f"Longitud promedio de la cola (Lq): {round(averageQueueLengthResult, 2)} clientes.")
        setResult(self, f"Tiempo promedio de espera en la cola (Wq): {round(averageWaitingTimeInQueueResult, 4)} horas.")
        setResult(self, f"Longitud promedio del sistema (Ls): {round(averageSystemLengthResult, 2)} clientes.")
        setResult(self, f"Tiempo promedio de espera en el sistema (Ws): {round(averageWaitingTimeInSystemResult, 4)} horas.")
        setResult(self, f"Probabilidad de que hayan N clientes en el sistema (Pn): {round(probabilityThatThereAreNClientsInABusySystemResult * 100, 2)}%")
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
        screen_config.setWindowInCenterOfScreen(self, 550, 600)
        self.title("TEORÍA DE COLAS - MODELO CASO 2 - M/M/S>1")
        tk.Label(self, text="Ingresa Lambda (λ) :", font=("Courier", 10)).pack(expand=True)
        lambdaEntry = ttk.Entry(self, justify="center")
        lambdaEntry.focus()
        lambdaEntry.pack(expand=True)
        tk.Label(self, text="clientes / hora", font=("Courier", 10), foreground="red").pack(expand=True)
        tk.Label(self, text="Ingresa Mi (µ) :", font=("Courier", 10)).pack(expand=True)
        miEntry = ttk.Entry(self, justify="center")
        miEntry.pack(expand=True)
        tk.Label(self, text="clientes / hora", font=("Courier", 10), foreground="red").pack(expand=True)
        tk.Label(self, text="Ingresa el número de servidores (s) :", font=("Courier", 10)).pack(expand=True)
        nServers = ttk.Entry(self, justify="center")
        nServers.pack(expand=True)
        tk.Label(self, text="servidores", font=("Courier", 10), foreground="green").pack(expand=True)
        tk.Label(self, text="¿Tienes número de clientes? (n):", font=("Courier", 10)).pack(expand=True)
        nClients = ttk.Entry(self, justify="center")
        nClients.pack(expand=True)
        tk.Label(self, text="clientes", font=("Courier", 10), foreground="green").pack(expand=True)

        def open_results():
            if lambdaEntry.get() == "" or miEntry.get() == "" or nServers.get() == "":
                pass
            else:
                model = MMS.MMS(int(lambdaEntry.get()), int(miEntry.get()), int(nServers.get()))
                utilizationFactor = model.utilizationFactor()
                probabilityThatThereAreNoClientsInSystem = model.probabilityThatThereAreNoClientsInSystem()
                averageQueueLength = model.averageQueueLength(probabilityThatThereAreNoClientsInSystem, utilizationFactor)
                averageWaitingTimeInQueue = model.averageWaitingTimeInQueue(averageQueueLength)
                averageSystemLength = model.averageSystemLength(averageQueueLength, averageWaitingTimeInQueue)
                averageWaitingTimeInSystem = model.averageWaitingTimeInSystem(averageQueueLength, averageWaitingTimeInQueue, utilizationFactor, probabilityThatThereAreNoClientsInSystem)
                if nClients.get() == "":
                    probabilityThatThereAreNClientsInABusySystem = model.probabilityThatThereAreNClientsInABusySystem(0, probabilityThatThereAreNoClientsInSystem)
                else:
                    probabilityThatThereAreNClientsInABusySystem = model.probabilityThatThereAreNClientsInABusySystem(int(nClients.get()), probabilityThatThereAreNoClientsInSystem)
                lambdaEntry.delete(0, "end")
                miEntry.delete(0, "end")
                nServers.delete(0, "end")
                nClients.delete(0, "end")
                window = ResultsWindow(
                    self, 
                    utilizationFactor, 
                    probabilityThatThereAreNoClientsInSystem, 
                    averageQueueLength, 
                    averageWaitingTimeInQueue, 
                    averageSystemLength, 
                    averageWaitingTimeInSystem, 
                    probabilityThatThereAreNClientsInABusySystem
                    )
                window.grab_set()
        
        tk.Button(
            self, 
            text="CALCULAR", 
            command=open_results,
            background="green yellow",
            activebackground="light sky blue"
            ).pack(expand=True)

def setResult(window, resultText):
    resultLabel = ttk.Label(window, text=resultText, font=("Courier", 10))
    resultLabel.pack(expand=True)

def initialize():
    app = MMSModelApp()
    app.mainloop()