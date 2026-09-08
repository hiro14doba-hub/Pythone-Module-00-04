import math
def get_player_pos()->tuple:
    while True:
        user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = user_input.split(',')
        error_found = False
        if len(parts)!=3:
            print("Invalid syntax")
            continue
        for part in parts:
            try:
                float(part)
            except ValueError as e:
                print(f"Error on parameter '{part}': {e}")
                error_found = True
                break
        if not error_found:
            return(float(parts[0]),float(parts[1]),float(parts[2]))

      
def main()->None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    dis_center = math.sqrt(pos1[0]**2+pos1[1]**2+pos1[2]**2)
    print(f"Distance to center: {round(dis_center,4)}")
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    dis_between = math.sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2+(pos1[2]-pos2[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(dis_between,4)}")

if __name__== "__main__":
    main()
