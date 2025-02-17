# mini program to showcase dictionary in use

def clear_console():
    print("\n" * 100)

print(art.logo)

bidders = {}

highest_bid = 0
winner = ""

end = False
while not end:

    name = input("What is your name? ")
    bid = float(input("What is your bid? "))

    bidders[name] = bid
    continue_bidding = input("Anymore bidders? Type yes or no: ")
    if continue_bidding.strip().lower() == "yes":
        clear_console()
    else:
        for name, bid in bidders.items():
            if bid > highest_bid:
                winner = name
                highest_bid = bid
        print(f"The winner is {winner} with a bid of ${highest_bid:.2f}.")
        break
    #print(bidders)
