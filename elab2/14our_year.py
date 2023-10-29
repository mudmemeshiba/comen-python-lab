man = input("What's the result of Manchester city's match? ")
liv = input("What's the result of Liverpool's match? ")
if man == "won" and liv == "lost":
    print("Manchester city is the champion of Premier League.")
elif man == "lost" and liv == "won":
    print("Liverpool is the champion of Premier League.")
else:
    man_m = int(input("What is the margin that Manchester city won by? "))
    liv_m = int(input("What is the margin that Liverpool won by? "))
    if man_m > liv_m:
        print("Manchester city is the champion of Premier League.")
    elif liv_m > man_m:
        print("Liverpool is the champion of Premier League.")
    else:
        playoff = input("Which team won the play-off match?(Manchester city/Liverpool) ")
        if playoff == "Manchester city":
            print("Manchester city is the champion of Premier League.")
        else:
            print("Liverpool is the champion of Premier League.")