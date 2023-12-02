import math

class MMS:
    lambdaVariable: int
    miVariable: int
    servers: int

    def __init__(self, lambdaVariable, miVariable, servers):
        self.lambdaVariable = lambdaVariable
        self.miVariable = miVariable
        self.servers = servers
    
    # QUEUE FUNCTIONS
    def averageQueueLength(self, Po, p):
        factorial = 1
        i = 1
        while (i <= self.servers):
            factorial = factorial * i
            i = i + 1
        Lq = (Po * ((self.lambdaVariable / self.miVariable) ** self.servers) * p) / (factorial * ((1 - p) ** 2))
        return Lq

    def averageWaitingTimeInQueue(self, lq):
        Wq = lq / self.lambdaVariable
        return Wq
    
    # SYSTEM FUNCTIONS
    def averageSystemLength(self, Lq, Wq):
        if Lq > 0:
            Ls = Lq + (self.lambdaVariable / self.miVariable)
        else:
            Ls = self.lambdaVariable * (Wq + (1 / self.miVariable))
        return Ls

    def averageWaitingTimeInSystem(self, Lq, Wq, p, Po):
        if Lq > 0:
            Ws = (Lq / self.lambdaVariable) + (1 / self.miVariable)
        elif Po > 0:
            i = 1
            factorial = 1
            while (i <= self.servers):
                factorial = factorial * i
                i = i + 1
            Ws = ((Po * ((self.lambdaVariable / self.miVariable) ** self.servers) * p) / (factorial * ((1 - p) ** 2) * self.lambdaVariable)) + (1 / self.miVariable)
        elif Wq > 0:
            Ws = Wq + (1 / self.miVariable)
        return Ws
    
    # Utilization factor
    def utilizationFactor(self):
        p = self.lambdaVariable / (self.servers * self.miVariable)
        return p
    
    # Probability that there are 0 clients in the System
    def probabilityThatThereAreNoClientsInSystem(self):
        i = 1
        factorial = 1
        while (i <= self.servers):
            factorial = factorial * i
            i = i + 1
        n = 0
        sumatoria = 0
        while n <= (self.servers - 1):
            t = 1
            factorial2 = 1
            while (t <= n):
                factorial2 = factorial2 * t
                t = t + 1
            sumatoria = sumatoria + ((self.lambdaVariable / self.miVariable) ** n) / factorial2
            n += 1
        Po = 1 / (sumatoria + ((((self.lambdaVariable / self.miVariable) ** self.servers) / factorial) * (1 / (1 - (self.lambdaVariable / (self.servers * self.miVariable))))))
        return Po
    
    # Probability that there are N clients in a busy System
    def probabilityThatThereAreNClientsInABusySystem(self, n, Po):
        factorial = 1
        i = 1
        while (i <= n):
            factorial = factorial * i
            i = i + 1
        factorial2 = 1
        g = 1
        while (g <= self.servers):
            factorial2 = factorial2 * g
            g = g + 1
        if (0 <= n <= self.servers):
            Pn = (((self.lambdaVariable / self.miVariable) ** n) / factorial) * Po
            return Pn
        else:
            if (n >= self.servers):
                Pn = (((self.lambdaVariable / self.miVariable) ** n) / (factorial2 * ((self.servers) ** (n - self.servers)))) * Po
                return Pn