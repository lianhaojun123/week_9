import os


def main():
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        expansion = filename.split('.')[-1]
        try:
            os.mkdir(expansion)
        except FileExistsError:
            pass
        print("{}/{}".format(expansion, filename))
        os.rename(filename, "{}/{}".format(expansion, filename))


main()