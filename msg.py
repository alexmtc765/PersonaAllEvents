import os

def getEVTpath():
    evt_fld = input("Enter events path:\n")
    return evt_fld

def makeBase():#makes a base txt file with the pak file names and some msg file formating
    global paknum
    paknum = 0
    events_folder = getEVTpath() #put the path to where your persona 5 events folder is (it might have to be on a different drive then where the script is being run cuz of how bad it is)
    with open('PAKs.txt', 'w') as f:
        for root, dirs, files in os.walk(events_folder):
            for file in files:
                if file.endswith(".PAK"):
                    print(os.path.join(file))
                    f.write("[msg ")
                    f.write("un")
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
    outfile = "third_pass.txt"

    delete_list = ["e"]
    with open(infile) as fin, open(outfile, "w+") as fout:
        for line in fin:
            for word in delete_list:
                line = line.replace(word, "")
            fout.write(line)
    
    infile = "third_pass.txt"
    outfile = "msg.txt"

    delete_list = ["un"]
    with open(infile) as fin, open(outfile, "w+") as fout:
        for line in fin:
            for word in delete_list:
                line = line.replace(word, "_")
            fout.write(line)
    
def removeTemp(): # removes temp files used for filtering
    os.remove("first_pass.txt")
    os.remove("second_pass.txt")
    os.remove("third_pass.txt")
    os.remove("PAKs.txt")
    os.rename("msg.txt", "msg.msg")

def main():
    makeBase()
    msgFilter()
    removeTemp()

main()
