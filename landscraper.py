### Landscaper Game

# Initial Prompt
print("""     \033[1m Landscaping Business Game!
      There is alot of work to do and you can cut the grass with a variety of tools.
      Good Luck!!!\033[0m
      """)

game_over = 'GAME OVER...........'

## Landscaper Game 
landscaping_game = {"tool": 0, "money": 0}

toolsForLandscaping = [  {"toolname": "teeth", "profit": 1, "cost_to_buy": 0 },
  {"toolname": "rusty scissors", "profit": 5, "cost_to_buy": 5 },
  {"toolname": "old-lawnmower", "profit": 50, "cost_to_buy": 25 },
  {"toolname": "fancy power lawnmower", "profit": 100, "cost_to_buy": 250 },
  {"toolname": "team of starving students", "profit": 250, "cost_to_buy": 500 } ]

## user_choice = input("Please select tool for cutting grass on lawns. [1]teeth [2]rusty scissors [3].... ")

## cut lawn function
def cut_lawn():
    tool = toolsForLandscaping[landscaping_game["tool"]]
    
    ## checking if the profit in landscaping game is 1000 to win game
    if landscaping_game['money'] >= 1000 or landscaping_game["tool"] >= 5:
        check_user_won_game()
    else:
        if tool['toolname'] == "teeth":
            landscaping_game['money'] = landscaping_game['money'] + tool['profit']
            print(f"If you keep using your \033[4m\033[1m{tool['toolname']}\033[0m\033[0m, you can keep mowing the lawn to earn \033[4m\033[1m${tool['profit']}\033[0m\033[0m for each lawn for a single day. You can keep doing this as long as you cut the lawn with your \033[4m\033[1m{tool['toolname']}\033[0m\033[0m and the running profit is \033[4m\033[1m${landscaping_game['money']}\033[0m\033[0m")
        elif tool['toolname'] == "rusty scissors":
            landscaping_game['money'] = landscaping_game['money'] + tool['profit']
            print(f"If you keep using your \033[4m\033[1m{tool['toolname']}\033[0m\033[0m, you can keep mowing the lawn to earn \033[4m\033[1m${tool['profit']}\033[0m\033[0m for each lawn for a single day. You can keep doing this as long as you cut the lawn with your \033[4m\033[1m{tool['toolname']}\033[0m\033[0m and the running profit is \033[4m\033[1m${landscaping_game['money']}\033[0m\033[0m")
        elif tool['toolname'] == "old-lawnmower":
            landscaping_game['money'] = landscaping_game['money'] + tool['profit']
            print(f"If you keep using your \033[4m\033[1m{tool['toolname']}\033[0m\033[0m, you can keep mowing the lawn to earn \033[4m\033[1m${tool['profit']}\033[0m\033[0m for each lawn for a single day. You can keep doing this as long as you cut the lawn with your \033[4m\033[1m{tool['toolname']}\033[0m\033[0m and the running profit is \033[4m\033[1m${landscaping_game['money']}\033[0m\033[0m")
        elif tool['toolname'] == "fancy power lawnmower":
            landscaping_game['money'] = landscaping_game['money'] + tool['profit']
            print(f"If you keep using your \033[4m\033[1m{tool['toolname']}\033[0m\033[0m, you can keep mowing the lawn to earn \033[4m\033[1m${tool['profit']}\033[0m\033[0m for each lawn for a single day. You can keep doing this as long as you cut the lawn with your \033[4m\033[1m{tool['toolname']}\033[0m\033[0m and the running profit is \033[4m\033[1m${landscaping_game['money']}\033[0m\033[0m")
        elif tool['toolname'] == "team of starving students":
            landscaping_game['money'] = landscaping_game['money'] + tool['profit']
            print(f"If you keep using your \033[4m\033[1m{tool['toolname']}\033[0m\033[0m, you can keep mowing the lawn to earn \033[4m\033[1m${tool['profit']}\033[0m\033[0m for each lawn for a single day. You can keep doing this as long as you cut the lawn with your \033[4m\033[1m{tool['toolname']}\033[0m\033[0m and the running profit is \033[4m\033[1m${landscaping_game['money']}\033[0m\033[0m")
        
## status of user in game
def checking_stats_of_landscaping_of_user():
    tool = toolsForLandscaping[landscaping_game['tool']]
    print(f"Your stats for this landscaping game includes the tool for cutting lawns which is \033[4m\033[1m{tool['toolname']}\033[0m\033[0m and the generated money for profit from this game is \033[4m\033[1m${landscaping_game['money']}\033[0m\033[0m")

## changing/upgrading tools
def changing_upgrade_checkingCosts_tools():
    if landscaping_game["tool"] >= (len(toolsForLandscaping) - 1):
        print("\033[4m\033[1m No more tools to change or upgrade to \033[0m\033[0m......")
    
    next_tool_landscaping = toolsForLandscaping[landscaping_game["tool"] + 1]
    ## checking if user has the money to purchase the tools
    if landscaping_game["money"] < next_tool_landscaping["cost_to_buy"]:
        print("\033[4m\033[1m Not enough money to buy the tools.... \033[0m\033[0m")
    else:
        print(f"Changing/Upgrading to the next tool known as \033[4m\033[1m {next_tool_landscaping['toolname']}\033[0m\033[0m")
        ## Subtracting the costs to buy tools from the total amount accumulated from landscaping
        landscaping_game["money"] -= next_tool_landscaping["cost_to_buy"]
        ## changing tool
        landscaping_game["tool"] += 1

## resetting the total profit in the landscaping game
def resetting_values():
    landscaping_game["money"] = 0;
    landscaping_game["tool"] = 0;
    print(f"The Landscaping game tool specification has been reduced to {landscaping_game['tool']} and the Landscaping game accumulated money profit amount has been reduced to {landscaping_game['money']}")

## checking if user won game
def check_user_won_game():
    #if landscaping_game['money'] >= 1000:
    if landscaping_game['money'] >= 1000:
        print("You won the Landscaping Game. \033[4m\033[1mCongratulations.......\033[0m\033[0m")
        return True
    else:
        return False
    #    while landscaping_game['money'] == 1000 or landscaping_game['tool'] >= 5:
    #        break
        
#    else:
#        return False

## quit/kill the game
def quit_kill_game():
    print(f"\033[4m\033[1m {game_over} \033[0m\033[0m")

## starting the landscaping game
while(True):
    ## selecting landscaping game option for operation and function and checking if input is a integer and is between 1-5
        user_game_option_choice = input("Please start the Landscaping Game by selecting one of the following options: \033[4m\033[1m[1] Mow Lawn\033[0m\033[0m \033[4m\033[1m[2] Upgrade Landscaping Tool\033[0m\033[0m \033[4m\033[1m[3] Check Stats\033[0m\033[0m \033[4m\033[1m[4] Resetting Values in Game\033[0m\033[0m \033[4m\033[1m[5] Quit\033[0m\033[0m.........")
        user_game_choice = int(user_game_option_choice)
        
    ## cutting lawns with landscaping game
        if(user_game_choice == 1):
            cut_lawn()
    ## generate the stats within the landscaping game
        elif(user_game_choice == 2):
            changing_upgrade_checkingCosts_tools()
      
    ## generate the stats within the landscaping game
        elif(user_game_choice == 3):
            checking_stats_of_landscaping_of_user()

    ## generate the stats within the landscaping game
        elif(user_game_choice == 4):
            resetting_values()

    ## quiting the landscaping game
        elif(user_game_choice == 5):
            quit_kill_game()
            break;
  
    ## checking if user won the landscaping game
        elif check_user_won_game():
            break


