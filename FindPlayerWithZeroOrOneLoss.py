def player(matches):
    winners = {}
    losers = {}
    
    for match in matches:
        winner, loser = match[0], match[1]
        winners[winner] = winners.get(winner, 0) + 1
        losers[loser] = losers.get(loser, 0) + 1
    
    one_time_losers = sorted([player for player, count in losers.items() if count == 1])
    clean_sheet_players = sorted([player for player in winners.keys() if player not in losers])
    
    return [clean_sheet_players, one_time_losers]
print(player([[1,3],[2,3],[5,4],[6,4]]))