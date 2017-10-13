class Agent:
    def __init__(self, selfN, selfE, selfD, foreignN, foreignE):
        self.selfN = selfN
        self.selfE = selfE
        self.selfD = selfD

        self.foreignN = foreignN
        self.foreignE = foreignE

    def encrypt(self, m):
        c = pow(m, self.selfD, self.selfN)
        return pow(c, self.foreignE, self.foreignN)

    def decrypt(self, c):
        m = pow(c, self.selfD, self.selfN)
        return pow(m, self.foreignE, self.foreignN)

if __name__ == '__main__':
    # Alice
    n1 = 3055735673
    e1 = 913395991
    d1 = 2654688175

    # Bob
    n2 = 2704140587
    e2 = 764752679
    d2 = 2409407639

    m = 111

    alice = Agent(n1, e1, d1, n2, e2)
    bob = Agent(n2, e2, d2, n1, e1)

    c = alice.encrypt(m)
    print(m)
    print(c)
    print(bob.decrypt(c))
