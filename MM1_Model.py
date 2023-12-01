from math import e

class MM1:
    lambdaVariable: float
    miVariable: float
    server = 1

    def __init__(self, lambdaVariable, miVariable):
        self.lambdaVariable = lambdaVariable
        self.miVariable = miVariable
    
    # QUEUE FUNCTIONS
    def averageQueueLength(self, Wq):
        if Wq > 0:
            Lq = self.lambdaVariable * Wq
        else:
            Lq = (self.lambdaVariable ** 2) / (self.miVariable * (self.miVariable - self.lambdaVariable))
        return round(Lq, 4)

    def averageWaitingTimeInQueue(self, lq):
        if lq > 0:
            Wq = lq / self.lambdaVariable
        else:
            Wq = self.lambdaVariable / (self.miVariable * (self.miVariable - self.lambdaVariable))
        return round(Wq, 4)

    # SYSTEM FUNCTIONS
    def averageSystemLength(self, lq, Ws, p):
        if lq > 0:
            Ls = lq + (self.lambdaVariable / self.miVariable)
        elif Ws > 0:
            Ls = self.lambdaVariable * Ws
        elif p > 0:
            Ls = p + (1 - p)
        else:
            Ls = (self.lambdaVariable) / ((self.miVariable - self.lambdaVariable))
        return round(Ls, 4)

    def averageWaitingTimeInSystem(self, Ls, Wq):
        if Ls > 0:
            Ws = Ls / self.miVariable
        elif Wq > 0:
            Ws = (1 / self.miVariable) + Wq
        else:
            Ws = 1 / (self.miVariable - self.lambdaVariable)
        return round(Ws, 4)

    # System waiting time probability
    def systemWaitingTimeProbability(self):
        Pw = self.lambdaVariable / self.miVariable
        return round(Pw, 4)

    # Utilization factor
    def utilizationFactor(self):
        p = (self.lambdaVariable / self.miVariable)
        return round(p, 4)
    
    # Probability that there are 0 clients in the System
    def probabilityThatThereAreNoClientsInSystem(self, p):
        if p > 0:
            Po = (1 - p)
        else:
            Po = (1 - (self.lambdaVariable / self.miVariable))
        return round(Po, 4)

    # Probability that there are N clients in a busy System
    def probabilityThatThereAreNClientsInABusySystem(self, p, n, Po):
        if Po > 0:
            Pn = (p ** n) * Po
        else:
            Pn = (1 - p) * (p ** n)
        return round(Pn, 4)

    # Time between arrivals
    def timeBetweenArrivals(self):
        time = 1 / self.lambdaVariable
        return round(time, 4)

    # Time between services
    def timeBetweenServices(self):
        time = 1 / self.miVariable
        return round(time, 4)

    # Probability that the waiting time is greater than a time in the System
    def probabilityThatWaitingTimeIsGreaterThanATimeInSystem(self, p, t):
        probability = e ** ((-self.miVariable * (1 - p)) * t)
        return round(probability, 4)

    # Probability that the waiting time is greater than a time in the Queue
    def probabilityThatWaitingTimeIsGreaterThanATimeInQueue(self, p, t):
        probability = p * (e ** ((-self.miVariable * (1 - p)) * t))
        return round(probability, 4)
