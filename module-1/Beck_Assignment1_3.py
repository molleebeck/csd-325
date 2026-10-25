
# Mollee Beck
# October 25, 2026
# Assignment: On the Wall
# Purpose: Count down the number of bottles of beer on the wall.

def countdown(bottles):
    while bottles > 0:
        if bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down, pass it around, no more bottles of beer on the wall.")
        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down, pass it around, {bottles - 1} bottles of beer on the wall.")
        print()
        bottles -= 1


def main():
    bottles = int(input("How many bottles of beer are on the wall? "))
    countdown(bottles)
    print("Time to buy more beer!")


if __name__ == "__main__":
    main()