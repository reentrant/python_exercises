results = [[]] * 5


def create_multipliers():
    return [lambda x: i * x for i in range(5)]


for i in range(5):
    for j, f in enumerate(create_multipliers()):
        results[j].append(f(i))

if __name__ == "__main__":
    print(results)
