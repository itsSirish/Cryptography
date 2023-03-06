
def rail_cipher(ciphertext: str, rails: int, mask: bool):

    fence = [[] for i in range(rails)]
    rail = 0
    direction = 1
    plaintext = ""

    for i in range(len(ciphertext)):
        fence[rail].append(None)
        rail += direction
        if rail == rails or rail == -1:
            direction = -direction
            rail += 2 * direction

    index = 0
    for rail in fence:
        for i in range(len(rail)):
            if rail[i] is None:
                rail[i] = ciphertext[index]
                index += 1

    rail = 0
    direction = 1
    for i in range(len(ciphertext)):
        plaintext += fence[rail][0]
        if mask:
            plaintext += " "
        fence[rail] = fence[rail][1:]
        rail += direction
        if rail == rails or rail == -1:
            direction = -direction
            rail += 2 * direction

    return plaintext

def char(cphr: str, m: int, M: int):

    temp = rail_cipher(cphr, m, False)
    for i in range(M-1):
        temp = rail_cipher(temp, m, False)
    return temp

def x_rep(cphr: str, X: str):

    return cphr.replace(X, " ")

def word(CipherText: str, n: int, N: int):
    tmp = rail_cipher(CipherText.split(), n, True)
    for i in range(N-1):
        tmp = rail_cipher(tmp.split(), n, True)
    return tmp

if __name__ == "__main__":
    inputs = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        inputs.append(line)
    N, n, M, m, X, CipherStr = inputs
    N = int(N)
    n = int(n)
    M = int(M)
    m = int(m)
    print(word(x_rep(char(CipherStr, m, M), X), n, N))

