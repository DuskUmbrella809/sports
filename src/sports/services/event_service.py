from sports.providers.events import EventProvider


class EventService:
    def __init__(self):
        self.provider = EventProvider()

        # Cache events by fixture ID
        self.cache: dict[int, list[dict]] = {}

    def get_events(self, fixture_id: int) -> list[dict]:
        # Return cached events if we already have them
        if fixture_id in self.cache:
            return self.cache[fixture_id]

        # Otherwise fetch from the API
        events = self.provider.get_events(fixture_id)

        # Save in cache
        self.cache[fixture_id] = events

        return events

    def clear_cache(self) -> None:
        self.cache.clear()