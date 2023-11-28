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
            Lq = (self.lambdaVariable**2) / (self.miVariable * (self.miVariable - self.lambdaVariable))
        return Lq

    def averageWaitingTimeInQueue(self, lq):
        if lq > 0:
            Wq = lq / self.lambdaVariable
        else:
            Wq = self.lambdaVariable / (self.miVariable * (self.miVariable - self.lambdaVariable))
        return Wq

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
        return Ls

    def averageWaitingTimeInSystem(self, Ls, Wq):
        if Ls > 0:
            Ws = Ls / self.miVariable
        elif Wq > 0:
            Ws = (1 / self.miVariable) + Wq
        else:
            Ws = 1 / (self.miVariable - self.lambdaVariable)
        return Ws

    # System waiting time probability
    def systemWaitingTimeProbability(self):
        Pw = self.lambdaVariable / self.miVariable
        return Pw

    # Utilization factor
    def utilizationFactor(self, n):
        p = (self.lambdaVariable / self.miVariable) ** n
        return p

    # Probability that there are N clients in a busy System
    def probabilityThatThereAreNClientsInABusySystem(self, p, n, Po):
        if Po > 0:
            Pn = (p ** n) * Po
        else:
            Pn = (1 - p) * (p ** n)
        return Pn

    # Time between arrivals
    def timeBetweenArrivals(self):
        time = 1 / self.lambdaVariable
        return time

    # Time between services
    def timeBetweenServices(self):
        time = 1 / self.miVariable
        return time

    # Probability that the waiting time is greater than a time in the System
    def probabilityThatWaitingTimeIsGreaterThanATimeInSystem(self, p, t):
        probability = e ** ((-self.miVariable * (1 - p)) * t)
        return probability

    # Probability that the waiting time is greater than a time in the Queue
    def probabilityThatWaitingTimeIsGreaterThanATimeInQueue(self, p, t):
        probability = p * (e ** ((-self.miVariable * (1 - p)) * t))
        return probability
