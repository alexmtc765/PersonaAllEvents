import os

def makeBase():#makes a base txt file with the pak file names and some msg file formating
    global paknum
    paknum = 0
    with open('PAKs.txt', 'w') as f:
        for root, dirs, files in os.walk("G:\Emulation\Ps3\Event"):
            for file in files:
                if file.endswith(".PAK"):
                    print(os.path.join(file))
                    f.write("[msg ")
                    f.write(str(paknum))
                    f.write("]")
                    f.write('\n')
                    f.write("[s]")
                    f.write(os.path.join(file))
                    f.write("[n][w]")
                    f.write('\n')
                    f.write('\n')
                    paknum += 1
                
def msgFilter():  #filters the base txt into a persona 5 msg code file
    infile = "PAKs.txt"
    outfile = "first_pass.txt"

    delete_list = ["_",]
    with open(infile) as fin, open(outfile, "w+") as fout:
        for line in fin:
            for word in delete_list:
                line = line.replace(word, " ")
            fout.write(line)

    infile = "first_pass.txt"
    outfile = "second_pass.txt"

    delete_list = [".PAK",]
    with open(infile) as fin, open(outfile, "w+") as fout:
        for line in fin:
            for word in delete_list:
                line = line.replace(word, "")
            fout.write(line)

    infile = "second_pass.txt"
    outfile = "msg.txt"

    delete_list = ["e"]
    with open(infile) as fin, open(outfile, "w+") as fout:
        for line in fin:
            for word in delete_list:
                line = line.replace(word, "")
            fout.write(line)

def removeTemp(): # removes temp files used for filtering
    os.remove("first_pass.txt")
    os.remove("second_pass.txt")
    os.remove("PAKs.txt")



