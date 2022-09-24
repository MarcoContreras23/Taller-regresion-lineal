class regresionLineal:

    def __init__(self, datosX, datosY):
        self.datosX = datosX
        self.datosY = datosY
        self.intercepcion = 0
        self.pendiente = 0
        self.x = 0
        self.y = 0
        self.xy = 0
        self.x2 = 0
    
    def iniciar(self):
        self.calcularDatos()
        self.calcularPendiente()
        self.calcularIntercepcion()

    def calcularDatos(self):
        self.x = sum(self.datosX)
        self.y = sum(self.datosY)
        self.xy = sum([self.datosX[i] * self.datosY[i] for i in range(len(self.datosX))])
        self.x2 = sum([self.datosX[i] * self.datosX[i] for i in range(len(self.datosX))])

    def calcularPendiente(self):
        n = len(self.datosX)
        self.pendiente = (n * self.xy - self.x * self.y) / (n * self.x2 - self.x * self.x)

    def calcularIntercepcion(self):
        n = len(self.datosX)
        self.intercepcion = (self.y * self.x2 - self.x * self.xy) / (n * self.x2 - self.x * self.x)

    def prediccion(self, datoPredecir):
        return self.pendiente * datoPredecir + self.intercepcion

    def listaPrediccion(self, datoPredecir):
        return [self.pendiente * data + self.intercepcion for data in datoPredecir]
      