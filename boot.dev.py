def count_names(list_of_lists, target_name):
    counter = 0
    for l in list_of_lists:
        print(l)
        if target_name in l:
            counter += 1 
    return counter


# don't touch below this line


def test(list_of_lists, target_name):
    result = count_names(list_of_lists, target_name)
    print(f"Number of input lists: {len(list_of_lists)}")
    print(f"Instances of {target_name}: {result}")
    print("====================================")


def main():
    test(
        [
            ["George", "Eva", "George"],
            ["Diane", "George", "Eva", "Frank"],
        ],
        "George",
    )
    test(
        [
            ["Amy", "Bob", "Candy"],
            ["Diane", "George", "Eva", "Frank"],
            ["Diane", "George"],
            ["George", "name", "George"],
        ],
        "George",
    )
    test(
        [
            ["Alex", "name", "Chloe"],
            ["Eric", "name", "Fred"],
            ["Hector", "name"],
            ["Hector", "name"],
            ["Hector", "name"],
            ["George"],
        ],
        "Hector",
    )


main()
