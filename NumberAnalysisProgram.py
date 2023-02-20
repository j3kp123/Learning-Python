def main():
    print("\n** Number Analysis Program **")
    print("-----------------------------")

    print("Pick 6 random numbers to see the lowest, \nhighest, and sum of them all.")
    random_numbers()

def random_numbers():
    numbers = []
    total = 0
    for i in range(6):
        number = int(input('Enter a random number: '))
        numbers.append(number)
        total += number
                   
    print('The lowest number in the list is', min(numbers))
    print('The highest number in the list is', max(numbers))
    print('The sum of all numbers in the list is', total)

main()
