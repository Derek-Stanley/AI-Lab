def clean():
    print("At location 'A'\n")
    ans=input("Is it dirty ? (Y/N)")
    if ans=='Y':
        print("Operation : Dirt sucked")
    print("Operation : Move to Location 'B'\n")
    print("At location 'B'\n")
    ans=input("Is it dirty ? (Y/N)")
    if ans=='Y':
        print("Operation : Dirt sucked")
    print("Operation : Move to Location 'A'\n")

def main():
    choice=input("Start CLeaning ? (Y/N)")

    if choice=='Y':
        while choice=='Y':
            clean()
            choice=input("Dirt Left ? (Y/N)")

main()

