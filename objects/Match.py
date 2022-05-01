from dataclasses import dataclass
from typing import Iterable
from objects.Map import Map


@dataclass
class Match:
    map_names: list
    score: str
    first: str
    second: str
    match_data: list[Map]
    _map_data: list

    def __repr__(self) -> str:
        return f"Match(score={self.score}, first={self.first}, second={self.second}, match_data=[DataFrame,])"

    @property
    def maps(self) -> list:
        out, maps, d = [], iter(self.map_names), iter(self._map_data)
        for i in range(2, len(self.match_data), 2):
            data = next(d)
            out.append(
                Map(
                    map_name=next(maps),
                    team_1_table=self.match_data[i],
                    team_2_table=self.match_data[i + 1],
                    score=f"{data[0].strip()}-{data[-1]}",
                )
            )
        return out

    @property
    def winner(self) -> str:
        score = self.score.split(":")
        if score[0] == score[1]:
            raise Exception("No winners or losers, tied game.")
        return max(zip(score, [self.first, self.second]))[1]

    @property
    def loser(self) -> str:
        score = self.score.split(":")
        if score[0] == score[1]:
            raise Exception("No winners or losers, tied game.")
        return min(zip(score, [self.first, self.second]))[1]
