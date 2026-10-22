import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        parts = arg.split(':')
        if len(parts) != 2:
            print(f"Error invalid parameter '{arg}'")
            continue
        item_name = parts[0]
        quantity_str = parts[1]
        if item_name in inventory:
            print(f"Redundant item '{item_name}' discarding")
            continue
        try:
            quantity = int(quantity_str)
            inventory[item_name] = quantity
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    number_of_items = len(inventory)
    total_items = sum(inventory.values())
    print(f"Total quantity of the {number_of_items} items: {total_items}")

    if total_items > 0:
        for item_name, quantity in inventory.items():
            percentage = quantity / total_items * 100
            print(f"Item {item_name} represents {round(percentage, 1)}%")

        most_item = ""
        least_item = ""
        max_qty = -1
        min_qty = -1

        for item_name, quantity in inventory.items():
            if max_qty == -1 or quantity > max_qty:
                max_qty = quantity
                most_item = item_name
            if min_qty == -1 or quantity < min_qty:
                min_qty = quantity
                least_item = item_name

        print(
            f"Item most abundant: {most_item} "
            f"with quantity {inventory[most_item]}"
        )
        print(
            f"Item least abundant: {least_item} "
            f"with quantity {inventory[least_item]}"
        )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
