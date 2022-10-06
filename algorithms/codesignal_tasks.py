def removeKElems(a, k):
    n = len(a)
    result = lambda arr, idx: arr[0:(idx - 1)] + arr[(idx + 1):n]
    return [ result(a, i) for i in range(n - k + 1) ]

def cyclicQueue(commands):

    maxSize = 10
    queue = [0] * maxSize
    answer = []
    head = 0
    tail = 0
    currentSum = 0

    for i in range(len(commands)):
        if commands[i] == '-':
            currentSum -= queue[head]
            head += 1
        else:
            value = 0
            for j in range(1, len(commands[i])):
                value = value * 10 + ord(commands[i][j]) - ord('0')
            currentSum += value
            queue[tail] = value
            tail = (tail + 1) % maxSize
        answer.append(currentSum)

    return answer

def possibleHeights(parent):

    edges = [[] for i in range(len(parent))]
    height = [0 for i in range(len(parent))]
    isPossibleHeight = [False for i in range(len(parent))]

    def initGraph(parent):
        for i in range(1, len(parent)):
            edges[parent[i]].append(i)

    def calcHeight(v):
        for u in edges[v]:
            ...

        countHeights = [[] for i in range(len(edges))]
        for i in range(len(edges[v])):
            u = edges[v][i]
            countHeights[height[u]].append(u)
        edges[v] = []
        for i in range(len(edges) - 1, -1, -1):
            for j in range(len(countHeights[i])):
                edges[v].append(countHeights[i][j])

    def findNewHeights(v, tailHeight):
        isPossibleHeight[max(height[v], tailHeight)] = True
        firstMaxHeight = tailHeight + 1
        secondMaxHeight = tailHeight + 1
        if len(edges[v]) > 0:
            firstMaxHeight = max(firstMaxHeight, height[edges[v][0]] + 2)
        if len(edges[v]) > 1:
            secondMaxHeight = max(secondMaxHeight, height[edges[v][1]] + 2)
        if len(edges[v]) > 0:
            findNewHeights(edges[v][0], secondMaxHeight)
        for i in range(1, len(edges[v])):
            findNewHeights(edges[v][i], firstMaxHeight)

    initGraph(parent)
    calcHeight(0)
    findNewHeights(0, 0)

    heights = []
    for i in range(len(parent)):
        if isPossibleHeight[i]:
            heights.append(i)
    return heights


class Generator:
    def __init__(self):
        self.names = {}

    def create(self, key):
        if key in self.names:
            self.names[key] += 1
        else:
            self.names[key] = 1
        return key + str(self.names[key])

    def delete(self, string):
        import re
        pattern = "(.+)\d+"
        if re.search(pattern, string):
            key = re.search(pattern, string).group(1)
            self.names.pop(key)




def usernameGenerator(queries):
    generator = Generator()
    ans = []
    for query in queries:
        task = query.split(' ')
        if task[0] == 'create':
            ans.append(generator.create(task[1]))
        if task[0] == 'delete':
            generator.delete(task[1])
    return ans


def hostAllocation(queries):
    tracker = Tracker()
    ans = []
    for query in queries:
        task = query.split(' ')
        if task[0] == 'A':
            ans.append(tracker.allocate(task[1]))
        if task[0] == 'D':
            tracker.deallocate(task[1])
    return ans


def beautifulString(inputString):
    result = False
    counters = {}
    for c in inputString:
        if ord(c) in counters:
            counters[ord(c)] += 1
        else:
            counters[ord(c)] = 1
    array = sorted(counters.keys(), reverse=True)
    for i in array:
        if counters[array[i]] <= counters[array[i + 1]]:
            result = True
        else:
            result = False
    return result


def plagiarismCheck(code1, code2):
    import re
    pattern = "([a-zA-Z_]+)"
    result = False
    if len(code1) == len(code2):
        for i in range(len(code1)):
            tokens1 = code1[i].split()
            tokens2 = code2[i].split()
            if len(tokens1) == len(tokens2):
                for index, value in enumerate(tokens1):
                    if tokens1[index] != tokens2[index]:
                        print(tokens1[index])
                        variable_state = 0
                        # create reg_ex for token1
                        regex = ""
                        for c in tokens1[index]:
                            if c.isalnum() or c == "_":
                                variable_state = 1

                            else:
                                if variable_state:
                                    regex += "[a-zA-Z_0-9]+"
                                    variable_state = 0
                                if c == "(" or c == ")" or c == "[" or c == "]":
                                    regex += "\\" + c
                                else:
                                    regex += c
                        if re.search(regex, tokens2[index]):
                            result = True
                        else:
                            break
    return result


if __name__ == "__main__":
    #print(usernameGenerator(["create alex","create alex","delete alex1","create alex","create john"]))
    #print(beautifulString("aabbb"))
    #print(beautifulString("z"))
    print(plagiarismCheck(["def is_even_sum(a, b):"], ["def is_even_sum(summand_1, summand_2):"]))
