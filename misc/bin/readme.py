import subprocess
from indent import block


def main():
    print("")
    print("example")
    print("----------------------------------------")
    print("")

    print("data.yaml")
    with block("yaml"):
        with open("examples/readme/data.yaml") as rf:
            for line in rf:
                print(line.rstrip())

    with block("bash"):
        print("$ nejimaki examples/readme/data.yaml --position=examples/readme")
        cmd = "make -C examples/readme"
        p = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in p.stderr.decode("utf-8").split("\n"):
            print(line)

        cmd = "tree examples/readme/conf"
        print("$ {}".format(cmd))
        p = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in p.stdout.decode("utf-8").split("\n"):
            print(line)


if __name__ == "__main__":
    main()
