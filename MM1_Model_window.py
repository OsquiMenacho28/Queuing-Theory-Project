import tkinter as tk
from tkinter import ttk
import screen_config
import MM1_Model as MM1

class ResultsWindow(tk.Toplevel):
    utilizationFactorResult: float
    averageQueueLengthResult: float
    averageWaitingTimeInQueueResult: float
    averageSystemLengthResult: float
    averageWaitingTimeInSystemResult: float
    systemWaitingTimeProbabilityResult: float
    probabilityThatThereAreNoClientsInSystemResult: float
    probabilityThatThereAreNClientsInABusySystemResult: float
    timeBetweenArrivalsResult: float
    timeBetweenServicesResult: float
    probabilityThatWaitingTimeIsGreaterThanATimeInSystemResult: float
    probabilityThatWaitingTimeIsGreaterThanATimeInQueueResult: float
    probabilityThatExistsMoreThanNClientsInQueueResult: float

    def __init__(self, parent, utilizationFactorResult, averageQueueLengthResult, averageWaitingTimeInQueueResult, 
                 averageSystemLengthResult, averageWaitingTimeInSystemResult, systemWaitingTimeProbabilityResult,
                 probabilityThatThereAreNoClientsInSystemResult, probabilityThatThereAreNClientsInABusySystemResult,
                 timeBetweenArrivalsResult, timeBetweenServicesResult, probabilityThatWaitingTimeIsGreaterThanATimeInSystemResult, 
                 probabilityThatWaitingTimeIsGreaterThanATimeInQueueResult, probabilityThatExistsMoreThanNClientsInQueueResult):
        super().__init__(parent)

        self.utilizationFactorResult = utilizationFactorResult
        self.averageQueueLengthResult = averageQueueLengthResult
        self.averageWaitingTimeInQueueResult = averageWaitingTimeInQueueResult
        self.averageSystemLengthResult = averageSystemLengthResult
        self.averageWaitingTimeInSystemResult = averageWaitingTimeInSystemResult
        self.systemWaitingTimeProbabilityResult = systemWaitingTimeProbabilityResult
        self.probabilityThatThereAreNoClientsInSystemResult = probabilityThatThereAreNoClientsInSystemResult
        self.probabilityThatThereAreNClientsInABusySystemResult = probabilityThatThereAreNClientsInABusySystemResult
        self.timeBetweenArrivalsResult = timeBetweenArrivalsResult
        self.timeBetweenServicesResult = timeBetweenServicesResult
        self.probabilityThatWaitingTimeIsGreaterThanATimeInSystemResult = probabilityThatWaitingTimeIsGreaterThanATimeInSystemResult
        self.probabilityThatWaitingTimeIsGreaterThanATimeInQueueResult = probabilityThatWaitingTimeIsGreaterThanATimeInQueueResult
        self.probabilityThatExistsMoreThanNClientsInQueueResult = probabilityThatExistsMoreThanNClientsInQueueResult

        screen_config.setWindowInCenterOfScreen(self, 1000, 650)
        self.title("RESULTADOS")
        ttk.Label(
            self, 
            text="RESULTADOS - MODELO M/M/1", 
            background="spring green", 
            font=("Courier", 20), 
            justify="center"
            ).pack(expand=True)
        setResult(self, f"Factor de utilización (p): {round(utilizationFactorResult * 100, 2)}%")
        setResult(self, f"Longitud promedio de la cola (Lq): {round(averageQueueLengthResult, 2)} clientes.")
        setResult(self, f"Tiempo promedio de espera en la cola (Wq): {round(averageWaitingTimeInQueueResult, 4)} horas.")
        setResult(self, f"Longitud promedio del sistema (Ls): {round(averageSystemLengthResult, 2)} clientes.")
        setResult(self, f"Tiempo promedio de espera en el sistema (Ws): {round(averageWaitingTimeInSystemResult, 4)} horas.")
        setResult(self, f"Probabilidad de tiempo de espera en el sistema P(Ws): {round(systemWaitingTimeProbabilityResult * 100, 2)}%")
        setResult(self, f"Probabilidad de que hayan 0 clientes en el sistema (Po): {round(probabilityThatThereAreNoClientsInSystemResult * 100, 2)}%")
        setResult(self, f"Probabilidad de que hayan N clientes en el sistema (Pn): {round(probabilityThatThereAreNClientsInABusySystemResult * 100, 2)}%")
        setResult(self, f"Tiempo esperado entre llegadas (1/λ): {round(timeBetweenArrivalsResult, 4)} horas.")
        setResult(self, f"Tiempo esperado entre servicios (1/µ): {round(timeBetweenServicesResult, 4)} horas.")
        setResult(self, f"Probabilidad de que el tiempo de espera en el sistema sea mayor a un tiempo determinado P(Ws > t): {round(probabilityThatWaitingTimeIsGreaterThanATimeInSystemResult * 100, 2)}%")
        setResult(self, f"Probabilidad de que el tiempo de espera en la cola sea mayor a un tiempo determinado P(Wq > t): {round(probabilityThatWaitingTimeIsGreaterThanATimeInQueueResult * 100, 2)}%")
        setResult(self, f"Probabilidad de que existan más de N clientes en la cola P(Lq > n): {round(probabilityThatExistsMoreThanNClientsInQueueResult * 100, 2)}%")
        tk.Button(
            self, 
            text="OK", 
            command=self.destroy, 
            background="lawn green",
            activebackground="dodger blue"
            ).pack(expand=True)

class MM1ModelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        screen_config.setWindowInCenterOfScreen(self, 550, 600)
        self.title("TEORÍA DE COLAS - MODELO CASO 1 - M/M/1")
        tk.Label(self, text="Ingresa Lambda (λ) :", font=("Courier", 10)).pack(expand=True)
        lambdaEntry = ttk.Entry(self, justify="center")
        lambdaEntry.focus()
        lambdaEntry.pack(expand=True)
        tk.Label(self, text="clientes / hora", font=("Courier", 10), foreground="red").pack(expand=True)
        tk.Label(self, text="Ingresa Mi (µ) :", font=("Courier", 10)).pack(expand=True)
        miEntry = ttk.Entry(self, justify="center")
        miEntry.pack(expand=True)
        tk.Label(self, text="clientes / hora", font=("Courier", 10), foreground="red").pack(expand=True)
        tk.Label(self, text="¿Tienes número de clientes? (n):", font=("Courier", 10)).pack(expand=True)
        nClients = ttk.Entry(self, justify="center")
        nClients.pack(expand=True)
        tk.Label(self, text="clientes", font=("Courier", 10), foreground="green").pack(expand=True)
        tk.Label(self, text="¿Tienes el tiempo de espera? P(W > t):", font=("Courier", 10)).pack(expand=True)
        waitTime = ttk.Entry(self, justify="center")
        waitTime.pack(expand=True)
        tk.Label(self, text="minutos", font=("Courier", 10), foreground="green").pack(expand=True)

        def open_results():
            if lambdaEntry.get() == "" or miEntry.get() == "":
                pass
            else:
                model = MM1.MM1(int(lambdaEntry.get()), int(miEntry.get()))
                utilizationFactor = model.utilizationFactor()
                averageQueueLength = model.averageQueueLength(0)
                averageWaitingTimeInQueue = model.averageWaitingTimeInQueue(averageQueueLength)
                averageSystemLength = model.averageSystemLength(averageQueueLength, 0, utilizationFactor)
                averageWaitingTimeInSystem = model.averageWaitingTimeInSystem(averageSystemLength, averageWaitingTimeInQueue)
                systemWaitingTimeProbability = model.systemWaitingTimeProbability()
                probabilityThatThereAreNoClientsInSystem = model.probabilityThatThereAreNoClientsInSystem(utilizationFactor)
                if nClients.get() == "":
                    probabilityThatThereAreNClientsInABusySystem = model.probabilityThatThereAreNClientsInABusySystem(utilizationFactor, 0, probabilityThatThereAreNoClientsInSystem)
                    probabilityThatExistsMoreThanNClientsInQueue = model.probabilityThatExistsMoreThanNClientsInQueue(1, utilizationFactor)
                else:
                    probabilityThatThereAreNClientsInABusySystem = model.probabilityThatThereAreNClientsInABusySystem(utilizationFactor, int(nClients.get()), probabilityThatThereAreNoClientsInSystem)
                    probabilityThatExistsMoreThanNClientsInQueue = model.probabilityThatExistsMoreThanNClientsInQueue(int(nClients.get()) + 1, utilizationFactor)
                timeBetweenArrivals = model.timeBetweenArrivals()
                timeBetweenServices = model.timeBetweenServices()
                if waitTime.get() == "":
                    probabilityThatWaitingTimeIsGreaterThanATimeInSystem = model.probabilityThatWaitingTimeIsGreaterThanATimeInSystem(utilizationFactor, 0)
                    probabilityThatWaitingTimeIsGreaterThanATimeInQueue = model.probabilityThatWaitingTimeIsGreaterThanATimeInQueue(utilizationFactor, 0)
                else:
                    probabilityThatWaitingTimeIsGreaterThanATimeInSystem = model.probabilityThatWaitingTimeIsGreaterThanATimeInSystem(utilizationFactor, (int(waitTime.get()) / 60))
                    probabilityThatWaitingTimeIsGreaterThanATimeInQueue = model.probabilityThatWaitingTimeIsGreaterThanATimeInQueue(utilizationFactor, (int(waitTime.get()) / 60))
                lambdaEntry.delete(0, "end")
                miEntry.delete(0, "end")
                nClients.delete(0, "end")
                waitTime.delete(0, "end")
                window = ResultsWindow(
                    self, 
                    utilizationFactor, 
                    averageQueueLength,
                    averageWaitingTimeInQueue,
                    averageSystemLength,
                    averageWaitingTimeInSystem,
                    systemWaitingTimeProbability,
                    probabilityThatThereAreNoClientsInSystem,
                    probabilityThatThereAreNClientsInABusySystem,
                    timeBetweenArrivals,
                    timeBetweenServices,
                    probabilityThatWaitingTimeIsGreaterThanATimeInSystem,
                    probabilityThatWaitingTimeIsGreaterThanATimeInQueue,
                    probabilityThatExistsMoreThanNClientsInQueue
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
    app = MM1ModelApp()
    app.mainloop()