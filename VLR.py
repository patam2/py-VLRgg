import re
import lxml.html

from objects.Match import Match
import simple_http.reqs as reqs
from tableops import matchtable


class VLRgg:
    def __init__(self) -> None:
        self.session = reqs.Session("https://www.vlr.gg")

    def get_match_page(self, page) -> str:
        req = self.session.get(f"https://www.vlr.gg/{page}")
        if req.status_code != 200:
            return None
        pattern = re.compile("(\t)|(\n)")
        return re.sub(pattern, "", req.body)

    def parse_match_page(self, page: str) -> Match:
        lxml_main = lxml.html.fromstring(page)
        # get played & non-played maps
        maps = [
            elem.text_content()[1:]
            for elem in lxml_main.find_class("vm-stats-gamesnav-item")
        ][1:]  # Skips 1st character & 'all maps' tab
        # Scoreline table:
        map_data = []
        for header in lxml_main.find_class("vm-stats-game-header"):
            map_data.append(list(header.itertext()))
        table_elem = lxml_main.xpath("//tr")

        # Agents
        agents = filter(
            None,
            [
                [img.attrib["title"] for img in elem.xpath(".//td/div/span/img")]
                for elem in table_elem
            ],
        )
        match_data = list(
            filter(
                lambda x: x not in [None, " ", "/"] and not "\r" in x,
                [text for elem in table_elem for text in elem.itertext()],
            )
        )
        match_data = matchtable.parse_table_data(match_data, agents)
        # Get map_scorelines
        # get score:
        match_header = lxml_main.find_class("match-header-vs")[0]
        # get winner & loser:
        first, second = map(
            lambda x: x.text_content(), match_header.find_class("wf-title-med")
        )
        # get scoreline:
        sline = match_header.xpath('//div[@class="js-spoiler "]')[0].text_content()
        # Total stats appears after 1st map, instead of being the first item or the last one. Switching them makes future work easier.
        match_data[0:2], match_data[2:4] = match_data[2:4], match_data[0:2]
        return Match(
            map_names=maps,
            match_data=match_data,
            first=first,
            second=second,
            score=sline,
            _map_data=map_data,
        )
