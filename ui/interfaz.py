import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as figureCanvas
from src.lecturaJson import lecturaJson
from src.regresionLineal import regresionLineal

class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.frameBtn = tk.Frame(self.root, bg="white")
        self.frameGraph = tk.Frame(self.root, bg="white")
        self.canvas = None
        self.table = None
        self.datosAPredecir = None
        self.prediccionDeDatos = None
        
        self.frameBtn.pack(side=tk.LEFT, expand=True, padx=20)
        self.frameGraph.pack(side=tk.RIGHT, expand=True)
    
    def start(self):
        self.root.title("Regresión Lineal")
        self.root.geometry("770x450")
        self.root.configure(bg="white")

        loadLabel = tk.Label(self.frameBtn, text="Seleccione el archivo JSON para operar con sus datos", bg="white", font="Arial 10")
        loadLabel.pack()

        loadFileBtn = tk.Button(self.frameBtn, text="Load File", command=self.readFile)
        loadFileBtn.pack()

        graphLabel = tk.Label(self.frameGraph, text="Gráfico de Regresión Lineal", font="Arial 15 bold", bg="white")
        graphLabel.pack(pady=0)

        self.graph("", "", [], [], regresionLineal([], []))

        self.root.mainloop()

    def readFile(self):
        path = askopenfile(mode='r', filetypes=[('JSON Files', '*.json')])
        
        if path is not None:
            xName, yName, xData, yData, datosAPredecir = lecturaJson(path.name).leer()
            self.ejecutarRegresion(xName, yName, xData, yData, datosAPredecir)

    def ejecutarRegresion(self, xName, yName, xData, yData, datosAPredecir):
        regresion = regresionLineal(xData, yData)
        regresion.iniciar()
        prediccionDeDatos = regresion.prediccion(datosAPredecir)
        
        print("Para {} = {} la predicción {} es {}".format(xName, datosAPredecir, yName, prediccionDeDatos))
    
        xData.append(datosAPredecir)
        yData.append(prediccionDeDatos)

        self.graph(xName, yName, xData, yData, regresion)

    def graph(self, xName, yName, xData, yData, regresionLineal):
        figure = plt.Figure(figsize=(5, 4), dpi=100)
        ax = figure.add_subplot(111)
        canvas = figureCanvas(figure, self.frameGraph)
        ax.clear()
        canvas.draw()
        canvas.get_tk_widget().pack()
        self.canvas = canvas
        
        plt.scatter(xData, yData, color='red')
        plt.plot(xData, regresionLineal.listaPrediccion(xData), color='green')
        plt.show()