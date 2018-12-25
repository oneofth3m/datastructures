import sys

def main(filename, UF_class):
    fp = open(filename)
    size = int(fp.readline())

    uf = UF_class(size)
    connections = []
    for line in fp:
        p = int(line.split(' ')[0])
        q = int(line.split(' ')[1])
        if not uf.connected(p, q):
            uf.union(p, q)

    """
    while True:
        line = sys.stdin.readline()
        p = int(line.split(' ')[0])
        q = int(line.split(' ')[1])

        if uf.connected(p, q):
            print p, q, "are connected"
        else:
            print p, q, "are not connected"
    """

if __name__ == "__main__":
    classname = sys.argv[1]
    filename = sys.argv[2]

    module = __import__(classname)
    class_ = getattr(module, classname)
    main(filename, class_)