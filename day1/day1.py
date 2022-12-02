import sys

class Elf:
    def __init__(self, id):
        self.id = id
        self.calories = 0
        
def main():
    # get the input from AoC Website
    try:
        with open('day1_input.txt', 'r') as file:
            input_data = file.read()
        file.closed

        elves = []
        elf = 0
        elves.append(Elf(0))
        for x in input_data.splitlines():
            if x == '':
                elf = elf + 1
                e = Elf(elf)
                elves.append(e)
                continue

            elves[elf].calories += int(x)
    
        sorted_elves = sorted(elves, key=lambda x: x.calories, reverse=True)

        print(f"Elf {sorted_elves[0].id} has the most calories at {sorted_elves[0].calories}")

        total_cals = 0
        print("The top three elves are: ")
        for x in range(0,3):
            total_cals += sorted_elves[x].calories
            print(sorted_elves[x].id)
            
        print(f"Top 3 elves are carrying: {total_cals} calories")
    except Exception as e:
        print(e)
        sys.exit()


        
if __name__ == "__main__":
    main()
