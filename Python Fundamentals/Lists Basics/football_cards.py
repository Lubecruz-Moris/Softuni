team_info = input().split(" ")
team_a_players = 11
team_b_players = 11
cards_given = []
condition = False
for card in team_info:
    if card not in cards_given:
        cards_given.append(card)
        if "A" in card:
            team_a_players -= 1
        elif "B" in card:
            team_b_players -= 1
        if team_a_players < 7 or team_b_players < 7:
            condition = True
            break
print(f"Team A - {team_a_players}; Team B - {team_b_players}")

if condition:
    print("Game was terminated")