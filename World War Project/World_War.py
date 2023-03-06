from math import sqrt
tmpDict = {0: 'A', 1: 'D', 2: 'F', 3: 'G', 4: 'X'}

def Polybus(input_string,char_matrix,n,m):

    k = 0
    for i in range(n):
        for j in range(m):
            if k < len(input_string):
                char_matrix[i][j] = input_string[k]
                k += 1

    # Printing the char_matrix
    # for i in range(n):
        # for j in range(m):
            # print(char_matrix[i][j], end=' ')
        # print()


def find_char_index(matrix, char):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == char:
                return (i, j)
    return None

def polybiusCipher(s,char_matrix):
        
        encrypt = ""
 
        # convert each character to its encrypted code
        for char in s:
            i,j=find_char_index(char_matrix,char)
            encrypt += tmpDict[i]
            encrypt += tmpDict[j]

        return encrypt

def newmat(code: str, inp: str):

    dict={}
    for i in range(len(inp)):
        dict[i]=[inp[i]]

    for i in range(len(code)):
        dict[i%len(inp)].append(code[i])

    return dict

def transpose(dict: list, inp: str):

    inp_index = []
    for i in range(len(inp)):
        inp_index.append([inp[i],i])


    final_encrypt=''
    for keyword_index in sorted(inp_index):
        index = keyword_index[1]
        final_encrypt+=''.join(dict[index][1:])

    return final_encrypt


def main():
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    input_word, input_string, input_key = contents
    n = int(sqrt(len(input_string)))
    m = n if n*n >= len(input_string) else n+1
    char_matrix = [[' ' for j in range(m)] for i in range(n)]
    Polybus(input_string,char_matrix,n,m)
    encrypt= polybiusCipher(input_key,char_matrix)
    mat = newmat(encrypt,input_word)
    print(transpose(mat,input_word))

main()