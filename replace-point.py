street = "NESEVEIEN"
point = "LLLLLLL000"
point = "PUNKTID000"

def readfile():  # put domains in file in to list called 'domains'
    domains = []
    newfile = []
    namecount = 0
    file = open('newfile.txt', 'w')
    #file = open('newfile.txt', 'a')

    with open('neseveien.kof', 'r') as infile:
        for line in infile:
            line = line.strip()
            digg = point+str(namecount)
            x = line.replace(street, digg)
            namecount += 1
            print(x)
            newfile.append(' ' + x + '\n')
            file.write(' ' + x + '\n')
        print(namecount)


if __name__ == '__main__':
    readfile()
