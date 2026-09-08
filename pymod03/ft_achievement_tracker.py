import random
def get_player_archievements()->set:
    all_archievements =["Crafting Genius", "World Savior", "Master Explorer", 
        "Collector Supreme", "Untouchable", "Boss Slayer", 
        "Strategist", "Unstoppable", "Speed Runner", 
        "Survivor", "Treasure Hunter", "First Steps", 
        "Sharp Mind", "Hidden Path Finder"]
    number_archiev = random.randint(5,11)
    player_archievements = random.sample(all_archievements,number_archiev)
    return set(player_archievements)

def main()->None:
    print("=== Achievement Tracker System ===")
    alice = get_player_archievements()
    bob = get_player_archievements()
    charlie = get_player_archievements()
    dylan = get_player_archievements()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    
    all_distinct = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_distinct}")
    
    common = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common}")
    
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    
    print(f"Alice is missing: {all_distinct.difference(alice)}")
    print(f"Bob is missing: {all_distinct.difference(bob)}")
    print(f"Charlie is missing: {all_distinct.difference(charlie)}")
    print(f"Dylan is missing: {all_distinct.difference(dylan)}")

if __name__=="__main__":
    main()