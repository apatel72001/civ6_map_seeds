# Open save game and search for the 5-byte sequence '93 e5 23 06 03'

with open("MENELIK.Civ6Save", 'rb') as civ6_sav:
# with open("LADY SIX SKY.Civ6Save", 'rb') as civ6_sav:
    data = civ6_sav.read()
    file_position = data.find(b'\x93\xe5\x23\x06\x03')
    
    raw_seed = ((data[file_position-1]*256*256*256) +
                (data[file_position-2]*256*256) +
                (data[file_position-3]*256) +
                (data[file_position-4]))
    print("Raw Seed: ", raw_seed)
    
    max_positive_seed = 2**31 - 1
    print("Max Positive Seed: ", max_positive_seed)

    if raw_seed > max_positive_seed:
        raw_seed -= 2**32
        print("Modified Raw Seed: ", raw_seed)

game_random_seed = raw_seed
map_random_seed = raw_seed + 1

print("Game Random Seed:  ", game_random_seed, "\nMap Random Seed:   ", map_random_seed)