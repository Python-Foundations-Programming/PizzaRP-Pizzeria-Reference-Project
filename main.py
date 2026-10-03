import os
import glob

MENU_FILE = "menu.txt"


# ---------- File Handling ----------

def load_menu():
    menu = []
    if not os.path.exists(MENU_FILE):
        # create starter menu if not found
        starter = [
            "Margherita;Medium;12.50",
            "Salami;Large;15.00",
            "Funghi;Small;9.00"
        ]
        with open(MENU_FILE, "w", encoding="utf-8") as f:
            f.write("\n".join(starter))

    with open(MENU_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")
            if len(parts) == 3:
                name, size, price = parts
                try:
                    menu.append({"name": name, "size": size, "price": float(price)})
                except ValueError:
                    print(f"⚠️ Skipping invalid line: {line.strip()}")
    return menu


def get_next_invoice_filename():
    existing = glob.glob("invoice_*.txt")
    numbers = [int(f.split("_")[1].split(".")[0]) for f in existing if f.startswith("invoice_")]
    next_num = max(numbers) + 1 if numbers else 1
    return f"invoice_{next_num:03d}.txt"


def write_invoice(order, total, discounts_applied):
    filename = get_next_invoice_filename()
    with open(filename, "w", encoding="utf-8") as f:
        f.write("🍕 PIZZA RP INVOICE\n")
        f.write("---------------------\n")
        for p in order:
            f.write(f"{format_item(p)}\n")
        f.write("---------------------\n")
        if discounts_applied:
            for d in discounts_applied:
                f.write(f"Discount: {d}\n")
        f.write(f"TOTAL: CHF {total:.2f}\n")
    print(f"✅ Invoice saved as {filename}")


# ---------- Ordering Logic ----------

def show_menu(menu):
    print("\n--- 🍕 Pizza Menu ---")
    for i, p in enumerate(menu, start=1):
        print(f"{i}. {p['name']} ({p['size']}) - CHF {p['price']:.2f}")
    print("---------------------")


def item_total(unit_price, quantity):
    # a quantity of 0 or smaller never results in a negative amount
    if quantity <= 0:
        return 0.0
    return unit_price * quantity


def format_item(item):
    total = item_total(item['price'], item['quantity'])
    return f"{item['quantity']}x {item['name']} ({item['size']}) - CHF {total:.2f}"


def ask_quantity():
    while True:
        quantity = input("Enter quantity: ").strip()
        if not quantity.isdigit() or int(quantity) < 1:
            print("⚠️ Invalid quantity.")
            continue
        return int(quantity)


def calculate_subtotal(order):
    return sum(item_total(p['price'], p['quantity']) for p in order)


def create_order(menu):
    order = []
    while True:
        choice = input("Enter pizza number (or 'done'): ").strip()
        if choice.lower() == "done":
            break
        if not choice.isdigit() or not (1 <= int(choice) <= len(menu)):
            print("⚠️ Invalid choice.")
            continue
        pizza = menu[int(choice) - 1]
        quantity = ask_quantity()
        item = {"name": pizza['name'], "size": pizza['size'], "price": pizza['price'], "quantity": quantity}
        order.append(item)
        print(f"Added! Current subtotal: CHF {calculate_subtotal(order):.2f}")
    return order


def calculate_total(order):
    total = calculate_subtotal(order)
    discounts = []

    pizza_count = sum(p['quantity'] for p in order)
    if pizza_count > 3:
        cheapest = min(order, key=lambda p: p['price'])
        total -= cheapest['price']
        discounts.append(f"Free pizza: {cheapest['name']} (-CHF {cheapest['price']:.2f})")

    if total >= 50:
        discount = total * 0.10
        total -= discount
        discounts.append(f"10% discount (-CHF {discount:.2f})")

    return total, discounts


# ---------- Main Program ----------

def main():
    menu = load_menu()

    while True:
        print("\n=== 🍕 PizzaRP ===")
        print("1. Show menu")
        print("2. Create order and print invoice")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_menu(menu)
        elif choice == "2":
            show_menu(menu)
            order = create_order(menu)
            if not order:
                print("⚠️ No pizzas selected.")
                continue
            total, discounts = calculate_total(order)
            print("\n--- ORDER SUMMARY ---")
            for p in order:
                print(format_item(p))
            for d in discounts:
                print(d)
            print(f"TOTAL: CHF {total:.2f}")
            write_invoice(order, total, discounts)
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("⚠️ Invalid choice.")


if __name__ == "__main__":
    main()
