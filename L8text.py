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


