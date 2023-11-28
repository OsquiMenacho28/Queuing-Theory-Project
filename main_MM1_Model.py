import tkinter as tk
from tkinter import ttk
import MM1_Model as MM1

class Window(tk.Toplevel):
    averageQueueLengthResult: float
    def __init__(self, parent, averageQueueLengthResult):
        super().__init__(parent)
        self.averageQueueLengthResult = averageQueueLengthResult
        setWindowInCenterOfScreen(self)
        self.title("RESULTADOS - MODELO M/M/1")
        ttk.Label(
            self, 
            text="RESULTADOS", 
            background="light yellow", 
            font=("Courier 20"), 
            width=100,
            justify="center"
            ).pack(expand=True)
        averageTailLength = ttk.Label(self, font=("Courier", 10))
        averageTailLength.pack(expand=True)
        averageTailLength.config(text=f"Longitud promedio de la cola: {averageQueueLengthResult}")
        tk.Button(
            self, 
            text="OK", 
            command=self.destroy, 
            background="lawn green",
            activebackground="dodger blue"
            ).pack(expand=True)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        setWindowInCenterOfScreen(self)
        self.title("TEORÍA DE COLAS - M/M/1")
        tk.Label(self, text="Ingresa Lambda (λ) :", font=("Courier", 10)).pack(expand=True)
        lambdaEntry = ttk.Entry(self, justify="center")
        lambdaEntry.focus()
        lambdaEntry.pack(expand=True)
        tk.Label(self, text="Ingresa Mi (µ) :", font=("Courier", 10)).pack(expand=True)
        miEntry = ttk.Entry(self, justify="center")
        miEntry.pack(expand=True)

        def open_results():
            if lambdaEntry.get() == "" or miEntry.get() == "":
                pass
            else:
                model = MM1.MM1(float(lambdaEntry.get()), float(miEntry.get()))
                averageQueueLength = round(model.averageQueueLength(0), 4)
                lambdaEntry.delete(0, "end")
                miEntry.delete(0, "end")
                window = Window(self, averageQueueLength)
                window.grab_set()
        
        tk.Button(
            self, 
            text="CALCULAR", 
            command=open_results,
            background="green yellow",
            activebackground="light sky blue"
            ).pack(expand=True)

def setWindowInCenterOfScreen(window):
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    windowWidth = 500
    windowHeight = 300
    positionWidth = round(screenWidth / 2 - windowWidth / 2)
    positionHeight = round(screenHeight / 2 - windowHeight / 2)
    window.geometry(str(windowWidth)+"x"+str(windowHeight)+"+"+str(positionWidth)+"+"+str(positionHeight))

if __name__ == "__main__":
    app = App()
    app.mainloop()