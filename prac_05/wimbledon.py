"""
CP1404 Practical
Wimbledon
Estimate: 30 minutes
Actual:   46 minutes
"""
FILE = "wimbledon.csv"


def main():
    """Takes data from file and displays Wimbledon champions and
     how many they have won as well as countries that have won the Wimbledon """
    champion_to_number_of_wins = {}
    champions = []
    countries = []
    generate_list_of_item_from_file(FILE, champions, 2)
    generate_list_of_item_from_file(FILE, countries, 1)
    generate_dictionary_of_champion_to_number_of_wins(champions, champion_to_number_of_wins)
    print("Wimbledon Champions:")
    print_champions_and_number_of_wins(champion_to_number_of_wins)
    print("")
    print("These 12 countries have won Wimbledon:")
    print(", ".join(sorted({country for country in countries})))


def generate_list_of_item_from_file(filename, out_list, index_of_line_part):
    """Generate a list of item from file from same given index"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            data = line.split(",")
            out_list.append(data[index_of_line_part])


def generate_dictionary_of_champion_to_number_of_wins(champions, champion_to_number_of_wins):
    """Generate a dictionary of Wimbledon champions and how many times they won"""
    for champion in champions:
        if champion not in champion_to_number_of_wins:
            champion_to_number_of_wins[champion] = 1
        else:
            champion_to_number_of_wins[champion] += 1


def print_champions_and_number_of_wins(champion_to_number_of_wins):
    """Print the Wimbledon champions with how many times they have won"""
    for champion, number_of_wins in champion_to_number_of_wins.items():
        print(champion, number_of_wins)


main()
