class MMS:
    lambdaVariable: float
    miVariable: float
    servers: int

    def __init__(self, lambdaVariable, miVariable, servers):
        self.lambdaVariable = lambdaVariable
        self.miVariable = miVariable
        self.servers = servers
    
    # QUEUE FUNCTIONS
    def averageQueueLength(self, Wq):
        if Wq > 0:
            Lq = self.lambdaVariable * Wq
        else:
            Lq = (self.lambdaVariable**2) / (self.miVariable * (self.miVariable - self.lambdaVariable))
        return Lq