# Opens save game and searches for the 5-byte sequence '93 e5 23 06 03'
# Extracts and reverses the preceeding 4 bytes (32-bit signed integer)
# That is the Game Seed (+1 for the Map Seed)

# save_game = "MENELIK - Roraima"
# save_game = "MENELIK - Torres del Paine"
# save_game = "LADY SIX SKY - Roraima"
# save_game = "PETER - Sahara el Beyda"
# save_game = "PETER - Valetta"
save_game = "PETER - Torres del Paine"

print("Save Game File:", save_game)

with open(save_game + ".Civ6Save", 'rb') as Civ6Save:
    data = Civ6Save.read()
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