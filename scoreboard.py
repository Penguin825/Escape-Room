def get_scores(game_id, player_scores):

    # Input name and time into text file
    with open("scoreboard.txt", "a") as file:
        a = file.write( "\n" + game_id + " " + str(player_scores))
        
    # Reads the textfile 
    with open("scoreboard.txt", "r+") as file:
        scores_list = file.readlines()
            
    names = []
    times = []

    # Remove new line in each line written in text file
    for line in scores_list:
        if line[-1] == "\n":
            line = line[:-1]
            
        # Seperate names and times by spaces between
        line = line.split()
        
        # Add name into list of names
        names.append(line[0])
        
        # Add times into list of times
        times.append(line[1])

    print("\t\t\t\t" , "   SCOREBOARD :" )
    print("\t\t\t\t" , "NAME" , "\t\t" , "TIME(s)")

    # Zip two list of names and times into tuple
    zipped = list(zip(names, times))
    zipped = sorted(zipped, key= lambda times : int(times[1]))

    # Prints names and times
    for line in zipped:
        print("\t\t\t\t" , str(line[0]) , "\t\t", str(line[1]))


def scoreboard():
    # Prints out scoreboard      
    with open("scoreboard.txt" , "r" ) as inputfile:
        lines = inputfile.readlines()
        
        names = []
        times = []
        
        # Remove new line in each line written in text file
        for line in lines:
            if line[-1] == "\n":
                line = line[:-1]
                
            # Seperate names and times by spaces between
            line = line.split()
            
            # Add name into list of names
            names.append(line[0])
            
            # Add times into list of times
            times.append(line[1])

        # Zip two list of names and times into tuple
        zipped = list(zip(names, times))
        zipped = sorted(zipped, key= lambda times : int(times[1]))

        # Prints names and times
        for line in zipped:
            print("\t\t\t\t" , str(line[0]) , "\t\t", line[1])
            

