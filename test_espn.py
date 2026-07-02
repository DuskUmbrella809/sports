from sports.providers.espn import ESPNProvider

provider = ESPNProvider()

matches = provider.get_matches()

print(f"Matches: {len(matches)}")

for match in matches[:5]:
    print(match)