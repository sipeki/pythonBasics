file = open("teams.txt", "w")

teams = "spuds \nhighlifers \nscots magic \nfantastic \nwonder team\n"
file.write(teams)

file .close()

file = open("teams.txt", "r")

textline = ""

for line in range(0,4):
    textline = file.readline()
    if line == 0 or line == 3:
        print(line+1, textline)

file .close()
