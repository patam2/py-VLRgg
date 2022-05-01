import VLR


client = VLR.VLRgg()
parsed = client.parse_match_page(client.get_match_page(85531))


def post_match():
    print(f"{parsed.first} {parsed.score} {parsed.second}\n")

    for mapo in parsed.maps:
        print(mapo.map_name, '-', mapo.score)

    for enum, mapo in enumerate(parsed.maps, 1):
        print(f'Map #{enum}: {mapo.map_name}\n')
        print(f'{parsed.first}')
        print(f'{mapo.team_1_table[["Name", "Agent","ACS", "K", "D", "A", "FK"]]}\n')
        print(f'{parsed.second}')
        print(f'{mapo.team_2_table[["Name", "Agent","ACS", "K", "D", "A", "FK"]]}\n')

    print('Total series:')
    print(f'{parsed.match_data[0][["Name", "Agent","ACS", "K", "D", "A", "FK"]]}\n')
    print(f'{parsed.match_data[1][["Name", "Agent","ACS", "K", "D", "A", "FK"]]}')

post_match()    