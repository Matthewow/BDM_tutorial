import collections

class PossibleCase():
    def __init__(self, name = None, elements = list(), probability = None):
        self.name = name
        self.elements = elements
        self.probability = probability


class uncertainTuple():
    def __init__(self, _tuple):
        self.id = _tuple[0]
        self.attributes = _tuple[1]
        self.probability = _tuple[2]


class PossibleWorld():
    def __init__(self, db):
        self.possible_world = list()
        self.db = list()
        self.construct_possible_world(db)
        self.sort_possible_world()

    
    def construct_possible_world(self, db):

        for tuples in db:
            if not len(self.possible_world):
                index = 1
                for tp in tuples:
                    curTp = uncertainTuple(tp)
                    pc = PossibleCase(f"P{index}", [curTp], curTp.probability)
                    index += 1
                    self.possible_world.append(pc)
            else:
                new_pw = list()
                index = 1
                for tp in tuples:
                    curTp = uncertainTuple(tp)
                    for existing_pc in self.possible_world:
                        pc = PossibleCase(f"P{index}", existing_pc.elements + [curTp], round(existing_pc.probability * curTp.probability, 10) )
                        index += 1
                        new_pw.append(pc)
                self.possible_world = new_pw
    

    def sort_possible_world(self):
        for pc in self.possible_world:
            pc.elements.sort(key = lambda x:x.attributes, reverse = True)


    def print_possible_world(self):
        print("\n#### Generating Possible World...\n")
        for pc in self.possible_world:
            print(f"{pc.name}, {','.join(tp.id for tp in pc.elements)}, {pc.probability}")

    
    def UtopK(self, k = 1):
        print("\n#### Generating U-topK...\n")
        res = dict()
 
        for pc in self.possible_world:
            res_tp = [tp.id for tp in pc.elements[:k]]
            res_tp = tuple(res_tp)
            res[res_tp] = res.get(res_tp, 0) + pc.probability

        sortedRes = collections.OrderedDict(sorted(res.items(), key = lambda x: x[1], reverse = True))
        for k, v in sortedRes.items(): print(f"{k}, {v}")

    
    def U_K_Ranks(self, k):
        print("\n#### Generating U-K-Ranks ...\n")
        for i in range(k):
            res = dict()
            for pc in self.possible_world:
                res[pc.elements[i].id] = res.get(pc.elements[i].id, 0) + pc.probability
            print(f"Rank: {i}: \n {res}")


    def PT_K(self, k, threshold = 1):
        print("\n#### Generating PT-K ...\n")
        res = dict()
        for pc in self.possible_world:
            for i in range(k):
                res[pc.elements[i].id] = res.get(pc.elements[i].id, 0) + pc.probability
        for k, v in res.items():
            print(f"{k}, {v}{'  √' if v >= threshold else ''}" )

    def global_top_K(self, k):
        self.PT_K(k)



db = [
    [
        ("t1", 100, 0.4),
        ("t2", 80, 0.6)
    ],
    [
        ("t3", 90, 0.8),
        ("t4", 60, 0.2)
    ],
    [
        ("t5", 70, 1)
    ]
]



pw = PossibleWorld(db)
pw.print_possible_world()
pw.UtopK(2)
pw.print_possible_world()
pw.U_K_Ranks(2)
pw.PT_K(2, 0.5)
pw.global_top_K(2)
            
                
