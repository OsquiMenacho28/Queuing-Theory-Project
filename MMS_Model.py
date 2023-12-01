import math

class MMS:
    lambdaVariable: float
    miVariable: float
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
        Lq = (Po * ((self.lambdaVariable / self.miVariable) ** self.servers)) / (factorial * ((1 - p) ** 2))
        return round(Lq, 4)

    def averageWaitingTimeInQueue(self, lq):
        Wq = lq / self.lambdaVariable
        return round(Wq, 4)
    
    # SYSTEM FUNCTIONS
    def averageSystemLength(self, Lq, Wq):
        if Lq > 0:
            Ls = Lq + (self.lambdaVariable / self.miVariable)
        else:
            Ls = self.lambdaVariable * (Wq + (1 / self.miVariable))
        return round(Ls, 4)

    def averageWaitingTimeInSystem(self, Lq, Wq, p, Po):
        i = 0
        if Lq > 0:
            Ws = (Lq / self.lambdaVariable) + (1 / self.miVariable)
        elif Po > 0:
            factorial = 1
            while (i <= self.servers):
                factorial = factorial * i
                i = i + 1
            Ws = ((Po * ((self.lambdaVariable / self.miVariable) ** self.servers) * p) / (factorial * ((1 - p) ** 2) * self.lambdaVariable)) + (1 / self.miVariable)
        elif Wq > 0:
            Ws = Wq + (1 / self.miVariable)
        else:
            Ws = 1 / (self.miVariable - self.lambdaVariable)
        return round(Ws, 4)
    
    # Utilization factor
    def utilizationFactor(self):
        p = self.lambdaVariable / (self.servers * self.miVariable)
        return round(p, 4)
    
    # Probability that there are 0 clients in the System
    def probabilityThatThereAreNoClientsInSystem(self):
        factorial = 1
        i = 1
        while (i <= self.servers):
            factorial = factorial * i
            i = i + 1
        n = 0
        sumatoria = 0
        while n <= (self.servers - 1):
            factorial2 = 1
            t = 1
            while (t <= n):
                factorial2 = factorial2 * t
                t = t + 1
            sumatoria = ((self.lambdaVariable / self.miVariable) ** n) / factorial2
            n += 1
        Po = 1 / (sumatoria + ((((self.lambdaVariable / self.miVariable) ** self.servers) / factorial) * (1 / (1 - (self.lambdaVariable / (self.servers * self.miVariable))))))
        return round(Po, 4)
    
    # Probability that there are N clients in a busy System
    def probabilityThatThereAreNClientsInABusySystem(self, n, Po):
        factorial = 1
        i = 1
        while (i <= n):
            factorial = factorial * i
            i = i + 1
        factorial2 = 1
        j = 1
        while (j <= self.servers):
            factorial2 = factorial2 * j
            j = j + 1
        if (0 <= n <= self.servers):
            Pn = (((self.lambdaVariable / self.miVariable) ** n) / factorial) * Po
        else:
            if (n >= self.servers):
                Pn = (((self.lambdaVariable / self.miVariable) ** n) / (factorial2 * ((self.servers) ** (n - self.servers)))) * Po
        return round(Pn, 4)