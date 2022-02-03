import os

def getEVTpath():
    evt_fld = input("Enter events path:\n")
    return evt_fld

def makeBase(): #makes a base txt file with the pak file names and some markers for the filtering

    events_folder = getEVTpath()
    with open('PAKs.txt', 'w') as f:
        for root, dirs, files in os.walk(events_folder):
            for file in files:
                if file.endswith(".PAK"): #puts the stuff into a txt file
                    f.write("disp")
                    f.write(" msg")
                    f.write(" nd")
                    f.write('\n')
                    print(os.path.join(file))
                    f.write(os.path.join(file))
                    f.write('\n')

def codeFilter(): #filters the base txt into a persona 5 flow code file

    #everything under here just filters the names so that its code 
    infile = "PAKs.txt"
    outfile = "first_pass.txt"

    delete_list = ["_",]
    with open(infile) as fin, open(outfile, "w+") as fout:
        for line in fin:
            for word in delete_list:
                line = line.replace(word, ",")
            fout.write(line)

    infile = "first_pass.txt"
    outfile = "second_pass.txt"

    delete_list = [".PAK",]
    with open(infile) as fin, open(outfile, "w+") as fout:
        for line in fin:
            for word in delete_list:
                line = line.replace(word, ");")
            fout.write(line)

    infile = "second_pass.txt"
    outfile = "third_pass.txt"

    delete_list = ["e"]
    with open(infile) as fin, open(outfile, "w+") as fout:
        for line in fin:
            for word in delete_list:
                line = line.replace(word, "CALL_EVENT(")
            fout.write(line)

    infile = "third_pass.txt"
    outfile = "forth_pass.txt"
    delete_list = ["disp"]
    with open(infile) as fin, open(outfile, "w+") as fout:
        for line in fin:
            for word in delete_list:
                line = line.replace(word,"MSG_WND_DSP();\nMSG_MIND(")
            fout.write(line)

    infile = "forth_pass.txt"
    outfile = "fifth_pass.txt"
    global msgNum
    msgNum = -0.333333333333333333 #some bull so it doesnt count by 3
    delete_list = ["msg"]
    with open(infile) as fin, open(outfile, "w+") as fout:
        for line in fin:
            roundmsg = round(msgNum) #round the stupid number
            roundmsg = str(roundmsg)
            msgstr = "_" + roundmsg
            for word in delete_list:
                line = line.replace(word,msgstr) 
            if (line.find(word)):
                msgNum += 0.333333333333333333
                
            fout.write(line)

    infile = "fifth_pass.txt"
    outfile = "flow.txt"
    delete_list = ["nd"]
    with open(infile) as fin, open(outfile, "w+") as fout:
        for line in fin:
            for word in delete_list:
                line = line.replace(word,", 0 );\nMSG_WND_CLS();")
            fout.write(line)

def removeTemp(): # removes temp files used for filtering
    os.remove("first_pass.txt")
    os.remove("second_pass.txt")
    os.remove("third_pass.txt")
    os.remove("forth_pass.txt")
    os.remove("fifth_pass.txt")
    os.remove("PAKs.txt")
    os.rename("flow.txt", "flow.flow")

def main():
    makeBase()
    codeFilter()
    removeTemp()

main()