import collections

def generate_char_signatures(patternList, length):
    print("\n#### Generating char signature...")
    result_list = []
    for pattern in patternList:
        result = genetrate_single_signature(pattern, length)
        print(f'{pattern}: {result}')
    


def genetrate_single_signature(pattern, length):
    pattern = pattern[1]
    result = [0] * length
    for char in pattern:
        result[(ord(char) - ord('a')) % length] = 1
    return result


def genetrate_inverted_file(patternList):
    res = dict()
    for pattern in patternList:
        for char in pattern[1]:
            res[char] = res.get(char, list())
            res[char].append(pattern[0])
    print_inverted_file(res)
    return res

def print_inverted_file(inverted):
    print("\n#### Generating inverted file ...")
    inverted = collections.OrderedDict(sorted(inverted.items()))
    for k, v in inverted.items(): print(f"{k}, {v}")


def edit_dis(s,t):
    n = len(s)
    m = len(t)

    # matrix to store edit distance
    ED_matrix = [ [0] * (m + 1) for _ in range(n + 1)]
    # matrix to store move direction
    Direction_matrix = [ [''] * (m + 1) for _ in range(n + 1)]

    # boundary initial
    for i in range(n + 1):
        ED_matrix[i][0] = i
        Direction_matrix[i][0] = 'W'
    for j in range(m + 1):
        ED_matrix[0][j] = j
        Direction_matrix[0][j] = 'A'

    # fill the matrixs
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            up = ED_matrix[i - 1][j] + 1
            left = ED_matrix[i][j - 1] + 1
            left_up = ED_matrix[i - 1][j - 1] 
            if s[i - 1] != t[j - 1]:
                left_up += 1
            
            smallest, direction = left_up, 'X'
            if smallest > left:
                smallest, direction = left, 'A'
            if smallest > up:
                smallest, direction = up, 'W'
            
            ED_matrix[i][j] = smallest
            Direction_matrix[i][j] = direction
    print('edit distance =', ED_matrix[n][m])
    # trace bask alignment path
    edit_s = ''
    edit_t = ''
    while not(n == 0 and m == 0):
        if Direction_matrix[n][m] == 'X':
            edit_s += s[n-1]
            edit_t += t[m-1]
            n -= 1
            m -= 1
        elif Direction_matrix[n][m] == 'W':
            edit_s += s[n-1]
            edit_t += '-'
            n -= 1
        else:
            edit_s += '-'
            edit_t += t[m-1]
            m -= 1
            
    print(edit_s[::-1])
    print('|'*len(edit_s))
    print(edit_t[::-1])


