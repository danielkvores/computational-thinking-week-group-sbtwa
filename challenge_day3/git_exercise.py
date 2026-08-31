from ainas import print_ainas
from alex import print_alex
from sylwia import print_sylwia
from daniel import print_daniel
from nathan import print_nathan
from paige import print_paige


def team_print():
    print("This is Team SBTWA. We are:")
    members = [
        print_ainas(),
        print_alex(),
        print_sylwia(),
        print_daniel(),
        print_nathan(),
        print_paige(),
    ]
    for member in members:
        print(member)


if __name__ == "__main__":
    team_print()