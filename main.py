# Henry Le
# CSCE 3110.002(8630)
# Professor Suleyman Olcay Polat
# Genshin Impact Gacha Simulator
# This program will simulate
# Genshin Impact's Wish Program

# Bugs so far:
# output results: "none" at certain times
# Python random module doesn't work well to simulate genshin impact, so multiple 4 stars and sometimes multiple 5 stars will appear
import random


def data_creation(char5star, char4star, weap4star, weap3star):
    database = open("Genshin_data\data.txt", 'r')

    count = 0  # This value will count empty lines in .txt file for rarity separation

    # 5-star character list
    for line in database:
        if line == '\n':
            count += 1
            continue
        elif line != '\n' and count == 0:  # if count is 0 then 5-star characters will be added
            char5star.append(line)
        elif line != '\n' and count == 1:  # if count is 1 then 4-star characters will be added
            char4star.append(line)
        elif line != '\n' and count == 2:  # if count is 2 then 4-star weapons will be added
            weap4star.append(line)
        elif line != '\n' and count == 3:  # if count is 3 then 3-star weapons will be added
            weap3star.append(line)

    database.close()


def menu(char5star, char4star, weap4star, weap3star):
    # Pity counts
    pity = 0        # pity counts before 5-star
    feature = 0     # if 50/50 is lost, then next 5-star is guaranteed featured 5-star
    reward = ""

    # Create Menu Options
    start = True
    option = -1
    while start:
        # chances list (will empty in every loop)
        nums = []
        count = 0  # feature and pity variable counter

        print("\nGENSHIN IMPACT GACHA SIMULATOR:\n"
              "1. Single Draw\n"
              "2. 10x Draw\n"
              "3. End Program")
        option = int(input("Choose an option: "))

        # Single Pull
        if option == 1:
            reward = pull(char5star, char4star, weap4star, weap3star, pity, feature)
            nums.append(reward)

            for i in char5star:
                if i == nums[0]:
                    if count == 0:
                        pity = 0
                        feature = 0
                    elif count > 0:
                        pity = 0
                        feature = 1
                else:
                    count += 1

            print("Results:\n", nums[0], end="")

        # 10-Pull
        elif option == 2:
            for i in range(10):
                reward = pull(char5star, char4star, weap4star, weap3star, pity, feature)
                nums.append(reward)
                pity += 1

                for j in nums:
                    for k in char5star:
                        if j == k:
                            if count == 0:
                                pity = 0
                                feature = 0
                            elif count > 0:
                                pity = 0
                                feature = 1
                        else:
                            count += 1

            print(nums)
            print("Results:")
            for i in nums:
                print(i, end="")

        # End While
        elif option == 3:
            start = False
            break


def pull(char5star, char4star, weap4star, weap3star, pity, feature):
    # base values for 3, 5-star categories
    base5 = .600
    base4 = 5.100
    base3 = 94.300

    # current percentage for 5-star
    current5 = (int(pity) * base5) + base5  # x(.600) + .600 if pity == 90, instant guarantee
    current3 = base3 - (int(pity) * base5)

    # Randomizer
    chance = random.uniform(0, 100)

    # 5-star character calculation
    if 0 < chance <= current5:
        chance = random.randint(0, 1)
        if chance == 0 or feature == 1:
            return char5star[feature]
        elif chance == 1:
            chance = random.randint(1, 5)
            return char5star[chance]

    # 4-star character & weapon calculation
    elif base5 <= chance < base3:
        chance = random.randint(0, 1)
        # 4-star characters
        if chance == 0:
            chance = random.uniform(0, 3)
            # featured 4-stars
            if chance > 1:
                chance = random.randint(0, 2)
                return char4star[chance]
            # non-featured 4-stars
            elif chance <= 1:
                chance = random.randint(3, 19)
                return char4star[chance]
        # -star weapons
        elif chance == 1:
            chance = random.randint(0, 17)
            return weap4star[chance]

    # 3-star weapon calculation
    elif base4 <= chance < current3:
        chance = random.randint(0, 12)
        return weap3star[chance]



def main():
    # Create Lists
    char5star = []
    char4star = []
    weap4star = []
    weap3star = []

    # Call functions
    data_creation(char5star, char4star, weap4star, weap3star)
    menu(char5star, char4star, weap4star, weap3star)


main()
