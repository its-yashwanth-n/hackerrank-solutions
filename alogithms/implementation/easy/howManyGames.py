def howManyGames(initial_price, discount, minimum_price, budget):
    
    current_cost = initial_price
    number_of_games = 0
    
    while (budget - current_cost) >= 0:
        number_of_games += 1
        budget -= current_cost
        if (current_cost - discount) > minimum_price:
            current_cost -= discount 
        else:
            current_cost = minimum_price
        
    return number_of_games