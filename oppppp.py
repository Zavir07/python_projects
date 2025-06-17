import random
computar_num=random.randint(0,2)


game_item=["rock","paper","scissor"]

computer_item_from_list = game_item[computar_num]

player_item=int(input("select\n 1.rock\n 2.paper\n 3.scissor\n: "))
player_item_from_list = game_item[player_item-1]

print(f"computer has selected : {computer_item_from_list}")

if (computer_item_from_list == "rock" and player_item_from_list == "paper"):
    print("player wins")

if (computer_item_from_list == "rock" and player_item_from_list == "scissor"):
    print("computer wins")

if (computer_item_from_list == "paper" and player_item_from_list == "scissor"):
    print("player wins")

if (computer_item_from_list == "paper" and player_item_from_list == "rock"):
    print("computer wins")

if (computer_item_from_list == "scissor" and player_item_from_list == "rock"):
    print("player wins")

if (computer_item_from_list == "scissor" and player_item_from_list == "paper"):
    print("computer wins")




















