import sys

class DSMain:
    def __init__(self, data_structure=None, classname=None):
        self._ds_str = data_structure

        module = __import__(classname)
        self._class = getattr(module, class_name)

        self._schema = {
            "stack" : {
                1: "Print",
                2: "push",
                3: "pop"
            },
            "queue" : {
                1: "Print",
                2: "enqueue",
                3: "dequeue"
            }
        }

        self._ds = self._class()

    def do_choice(self, choice):
        if choice == 1:
            print self._ds
        elif choice == 2:
            print "Enter Value : "
            value = sys.stdin.readline()
            operation = getattr(self._ds, self._schema[self._ds_str][choice])
            operation(value)
        elif choice == 3:
            operation = getattr(self._ds, self._schema[self._ds_str][choice])
            print operation()
        else:
            sys.exit(0)

    def print_menu(self):
        ds_ops = self._schema[self._ds_str]
        for choice in ds_ops:
            print choice, " : ", ds_ops[choice], self._ds_str + "."

def main(data_structure, class_name):

    ds = DSMain(data_structure, class_name)
    while True:

        ds.print_menu()

        choice = int(sys.stdin.readline())
        ds.do_choice(choice)

if __name__ == "__main__":
    data_structure = sys.argv[1]
    class_name = sys.argv[2]

    main(data_structure, class_name)
