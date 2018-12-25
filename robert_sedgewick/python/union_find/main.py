import sys
import UF

def main(filename):
    size = 0
    connections = []
    with open(filename) as fp:
        size = int(fp.readline())
        for line in fp:
            p = int(line.split(' ')[0])
            q = int(line.split(' ')[1])
            connections.append((p, q))

    uf = UF.UF(size)
    for (p, q) in connections:
        uf.union(p, q)

    while True:
        line = sys.stdin.readline()
        p = int(line.split(' ')[0])
        q = int(line.split(' ')[1])

        if uf.find(p, q):
            print p, q, "are connected"
        else:
            print p, q, "are not connected"


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)