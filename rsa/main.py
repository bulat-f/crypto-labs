from random import randrange
from random import getrandbits, randint

def gcd(a, b):
    if a == 0:
        return [b, 0, 1]

    [d, x1, y1] = gcd(b % a, a)
    return [d, y1 - (b // a) * x1, x1]

def check(a, s, d, n):
    x = pow(a, d, n)
    if x == 1:
        return True
    for i in range(s - 1):
        if x == n - 1:
            return True
        x = pow(x, 2, n)
    return x == n - 1

def miller_rabin(n, k=10):
    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False

    return True

def prime(bits = None, phi = None):
    while True:
        p = getrandbits(bits) if bits else randint(3, phi - 1)
        if miller_rabin(p):
            return p

class Agent:
    def __init__(self):
        p = prime(bits = 16)
        q = prime(bits = 16)
        phi = (p - 1)*(q - 1)

        self.selfN = p * q
        self.selfE = prime(phi = phi)

        [__dontNeed1, __dontNeed2, selfD] = gcd(phi, self.selfE)

        self.selfD = selfD if selfD > 0 else phi + selfD

    def getPublicKey(self):
        return [self.selfE, self.selfN]

    def setForeignKey(self, publicKey):
        [self.foreignE, self.foreignN] = publicKey

    def encrypt(self, m):
        c = pow(m, self.selfD, self.selfN)
        return pow(c, self.foreignE, self.foreignN)

    def decrypt(self, c):
        m = pow(c, self.selfD, self.selfN)
        return pow(m, self.foreignE, self.foreignN)

if __name__ == '__main__':
    alice = Agent()
    bob = Agent()

    alice.setForeignKey(bob.getPublicKey())
    bob.setForeignKey(alice.getPublicKey())

    m = 111
    c = alice.encrypt(m)

    print(m)
    print(c)
    print(bob.decrypt(c))
