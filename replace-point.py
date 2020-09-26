street = "SNEHVITVEI"
point = "PUNKT-"


def readfile():  # put domains in file in to list called 'domains'
    domains = []
    newfile = []
    namecount = 0
    file = open('output.txt', 'w')

    with open('input.kof', 'r') as infile:
        for line in infile:
            namecount += 1
            he = format(namecount, '04')
            line = line.strip()
            digg = point+he
            x = line.replace(street, digg)
            print(x)
            newfile.append(' ' + x + '\n')
            file.write(' ' + x + '\n')
        print(namecount)


if __name__ == '__main__':
    readfile()
