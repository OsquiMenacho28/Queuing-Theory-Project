import tkinter as tk
import screen_config
import MM1_Model_window
import MMS_Model_window

def openModelWindow(model):
    return model.initialize()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        screen_config.setWindowInCenterOfScreen(self, 450, 300)
        self.config(background="light cyan")
        self.title("TEORÍA DE COLAS")
        tk.Label(self, text="TEORÍA DE COLAS", font=("Courier", 15), background="light sky blue").pack(expand=True)
        tk.Label(self, text="Selecciona un Modelo :", font=("Courier", 10), background="aquamarine").pack(expand=True)
        tk.Button(
            self,
            text="MODELO CASO 1 - M/M/1",
            command=lambda: openModelWindow(MM1_Model_window),
            background="green yellow",
            activebackground="light sky blue"
            ).pack(expand=True)
        tk.Button(
            self,
            text="MODELO CASO 2 - M/M/S>1",
            command=lambda: openModelWindow(MMS_Model_window),
            background="green yellow",
            activebackground="light sky blue"
            ).pack(expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()