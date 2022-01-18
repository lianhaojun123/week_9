import os


def main():
    expansion_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        expansion = filename.split('.')[-1]
        if expansion not in expansion_to_category:
            category = input("What category would you like to sort {} files into? ".format(expansion))
            expansion_to_category[expansion] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        os.rename(filename, "{}/{}".format(expansion_to_category[expansion], filename))


main()