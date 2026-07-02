from sports.models import Match


class SearchService:
    def search(
        self,
        matches: list[Match],
        query: str,
    ) -> list[Match]:

        query = query.lower().strip()

        if not query:
            return matches

        results = []

        for match in matches:

            if (
                query in match.home_team.lower()
                or query in match.away_team.lower()
                or query in match.league.lower()
                or query in match.country.lower()
            ):
                results.append(match)

        return results