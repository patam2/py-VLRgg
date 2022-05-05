# py-VLRgg
(A buggy) VLR.gg wrapper utilizing lxml and sockets 


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

Example post_match() from examples.py:

![image](https://user-images.githubusercontent.com/88111864/166153770-1477b968-2707-4424-a535-491f1a141af1.png)
