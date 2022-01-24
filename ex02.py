# Exercise 02 

MIN = 1
MAX = 100

count = 0

print((f"Think of a number between {MIN} and {MAX}!"))

while True :
    # guess tries to offer a number located in between the minimal and maximal number.
    # With this approach we can eliminate ~50% of potential solutions.
    # The algorithm will continue to double down on potential solutions by reassigning
    # minimal and maximal values in accordance to the feedback gathered by its wrong choices.
    guess = (MIN + MAX)//2
    print(f"Is your number greater (>), equal (=), or less (<) than {guess}?",end = " ")
    ask = input("Please answer (>), (=) or (<)! ")
    
    if ask == '=':
        print("I have guessed it!")
        break
    # The condition below is used in order to detect whether the user will attempt to
    # go beyond the borders of minimal and/or maximal values (cheat) assigned
    # according to his previous choices. If caught, the loope will break.
    elif MIN == (MAX - 1) or MAX == MIN:
        print("Liar, liar - pants on fire!")
        break
    else:
        if ask == '>' :
            MIN = guess + 1
        elif ask == '<' :
            MAX = guess - 1
        else:
            print("Error! Wrong symbol!")
            # Continue here means that the loop will ask for the symbol again,
            # but it also makes sure that the count does not increase when the user
            # makes an error.
            continue
        
    count += 1
    
print(f"I needed {count} steps!")
            



    


    
    
        
        
        
        
        
    




