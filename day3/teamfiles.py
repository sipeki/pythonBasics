file = open("teams.txt", "w")

teams = "spuds \nhighlifers \nscots magic \nfantastic \nwonder team\n"
file.write(teams)

file .close()

file = open("teams.txt", "r")
file.seek(0)
textline = ""

for line in range(0,5):
    textline = file.readline()
    if line == 1 or line == 4:
        print(line, file.readline())

file .close()
