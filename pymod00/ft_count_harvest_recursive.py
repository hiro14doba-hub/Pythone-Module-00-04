def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count_helper(current=1):
        if current > days:
            print("Harvest time!")
            return (0)
        print("Day", current)
        count_helper(current+1)
    count_helper()
