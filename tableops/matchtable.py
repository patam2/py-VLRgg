from typing import Iterator
from pandas import DataFrame


def get_headers(table: list, i: int) -> list:
    temp_headers = table[i : i + 10] + ["FirstK/D-Diff"]

    headers = ["Name", "Agent", "Team"]
    for header in temp_headers:
        headers += [header, f"{header}_T", f"{header}_CT"]
    return headers


def parse_table_data(table: list, agents: Iterator[str]):
    # Get header indexes:
    # print(table)
    indexes, tables = [], []
    index = table.index("ACS")
    indexes.append(index)

    # See where tables start etc
    while True:
        try:
            index = table.index("ACS", index + 1)
            indexes.append(index)
        except ValueError:
            break
    # Make table
    for i in indexes:
        headers = get_headers(table, i)
        new_table = [headers]
        i += 11

        for j in range(0, 5):  # Todo -> what if more than 6?
            segment = table[i + 35 * j : i + j * 35 + 35]
            if "\xa0" in segment:
                if segment[2:] == ["\xa0"] * 33:
                    return make_DataFrame(tables)
            segment.insert(1, next(agents))
            new_table.append(segment)  # there has to be a better way
        tables.append(new_table)
    # Make list of tables, add column
    return make_DataFrame(tables)


def make_DataFrame(tables):
    for enum in range(len(tables)):
        t = DataFrame(tables[enum])
        t.columns = t.iloc[0]
        t = t[1:]
        tables[enum] = t
    return tables
