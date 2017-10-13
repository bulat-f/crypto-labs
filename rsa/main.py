def gcd(a, b):
    if a == 0:
        return [b, 0, 1]

    [d, x1, y1] = gcd(b % a, a)
    return [d, y1 - (b // a) * x1, x1]

class Agent:
    def __init__(self, p, q, selfE, foreignN, foreignE):
        phi = (p - 1)*(q - 1)
        [__dontNeed1, __dontNeed2, selfD] = gcd(phi, selfE)

        self.selfN = p * q
        self.selfE = selfE
        self.selfD = selfD  if selfD > 0 else phi + selfD

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
    p1 = 46819
    q1 = 65267
    e1 = 913395991

    # Bob
    p2 = 53161
    q2 = 50867
    e2 = 764752679

    m = 111

    alice = Agent(p1, q1, e1, p2 * q2, e2)
    bob = Agent(p2, q2, e2, p1 * q1, e1)

    c = alice.encrypt(m)
    print(m)
    print(c)
    print(bob.decrypt(c))
