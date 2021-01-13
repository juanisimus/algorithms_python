voted = {}

def check_voter(name):
    if voted.get(name):
        print("get the fuck out of here")
    else:
        voted[name] = True
        print("Go to vote")