while True:
    try:
        boots = []
        pairs = 0

        for x in range(int(input())):
            num, size = [x for x in input().split()]
            boots.append([num, size])

            for boot in boots:
                if boot[0] == num and boot[1] != size:
                    pairs += 1
                    break
        print(pairs)

    except EOFError:
        break