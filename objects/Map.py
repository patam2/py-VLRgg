from dataclasses import dataclass
from pandas import DataFrame


@dataclass
class Map:
    map_name: str
    team_1_table: DataFrame
    team_2_table: DataFrame
    score: str

    def __repr__(self) -> str:
        return f'Map(map_name={self.map_name}, score={self.score})'