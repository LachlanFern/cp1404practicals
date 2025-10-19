"""
Wimbledon
Estimate: 50 mins
Actual:32 mins
"""
filename = "wimbledon.csv"
def main():
    champion_to_win, countries = process_data()
    display_results(champion_to_win, countries)

def process_data() :
    champion_to_win = {}
    countries = set()
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.split(",")
            champion = parts[2]
            country = parts[1]
            champion_to_win[champion] = champion_to_win.get(champion, 0) + 1
            countries.add(country)
    return champion_to_win, countries

def display_results(champion_to_win, countries):
    print("Wimbledon Champions:")
    for name, wins in champion_to_win.items():
        print(f"{name} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

main()