# Opens save game and searches for the 5-byte sequence '93 e5 23 06 03'
# Extracts and reverses the preceeding 4 bytes (32-bit signed integer)
# That is the Game Seed (+1 for the Map Seed)

with open("LADY SIX SKY - Roraima.Civ6Save", 'rb') as civ6_sav:
# with open("MENELIK - Roraima.Civ6Save", 'rb') as civ6_sav:
# with open("MENELIK - Torres del Paine.Civ6Save", 'rb') as civ6_sav:
    data = civ6_sav.read()
    file_position = data.find(b'\x93\xe5\x23\x06\x03')
    
    raw_seed = ((data[file_position-1] * 2**24) +
                (data[file_position-2] * 2**16) +
                (data[file_position-3] * 2**8) +
                (data[file_position-4]))
    print("Raw Seed:", raw_seed)
    
    max_positive_seed = 2**31 - 1
    print("Max Positive Seed:", max_positive_seed)

    if raw_seed > max_positive_seed:
        raw_seed -= 2**32

game_random_seed = raw_seed
map_random_seed = raw_seed + 1

print("Game Random Seed: ", game_random_seed, "\nMap Random Seed:  ", map_random_seed)