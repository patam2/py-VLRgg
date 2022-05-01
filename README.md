# py-VLRgg
VLR.gg wrapper


Usage ->
```python
client = VLR.VLRgg()

#Get match data:
parsed = client.parse_match_page(client.get_match_page(85531))
```

parsed page methods/params:
* map_names - list[str]
* score - str
* first - str
* second - str
* winner - str
* loser - str
* match_data - list[pd.DataFrame]
* maps - list[Map]

Map methods:
* map_name - str
* team_1_table - pd.DataFrame
* team_2_table - pd.DataFrame
* score - str
