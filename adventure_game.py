def adventure_start():
 choice = input("choose your suitable location (forest, cave, beach): ")
 if choice == "forest":
     print("Be careful of snakes")
 elif choice == "cave":
    print("Be catious of bats")
 elif choice == "beach":
    print("Be careful of mermaids")
 else:
    print("invalid choice, try again")
adventure_start()

