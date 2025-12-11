from models.factory import BicycleFactory
from sales.sales_manager import SalesManager
from sales.sale import Sale

def main():
    manager = SalesManager()

    allowed_types = ["downhill", "ebike", "xc", "enduro", "trail", "gravel"]
    allowed_frame_sizes = ["xs", "s", "m", "m/l", "l", "xl", "xxl"]
    allowed_wheel_sizes = ["26", "27.5", "28", "29"]
    allowed_gears = [9, 10, 11, 12, 13]

    while True:
        print("\nBicycle Sales System")
        print("1. Add Sale")
        print("2. Calculate Total Sales from File")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            bike_type = input("Enter bicycle type: ").lower()
            if bike_type not in allowed_types:
                print("Error: Unknown bicycle type.")
                continue

            try:
                year = int(input("Enter year (...-2025): "))
                if year > 2025:
                    print("Error: Year cannot be greater than 2025")
                    continue
            except ValueError:
                print("Error: Year must be a number.")
                continue

            model = input("Enter model: ")
            color = input("Enter color: ")
            if any(char.isdigit() for char in color):
                print("Error: Color must not contain numbers.")
                continue

            frame_size = input("Enter frame size: ").lower()
            if frame_size not in allowed_frame_sizes:
                print("Error: Invalid frame size.")
                continue

            wheel_size = input("Enter wheel size: ")
            if wheel_size not in allowed_wheel_sizes:
                print("Error: Invalid wheel size.")
                continue

            try:
                gears = int(input("Enter number of gears: "))
                if gears not in allowed_gears:
                    print("Error: Invalid number of gears.")
                    continue
            except ValueError:
                print("Error: Gears must be a number.")
                continue

            try:
                price = float(input("Enter price (€): "))
                if price <= 0:
                    print("Error: Price must be positive.")
                    continue
            except ValueError:
                print("Error: Price must be a number.")
                continue

            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Error: Quantity must be positive.")
                    continue
            except ValueError:
                print("Error: Quantity must be a number.")
                continue

            bicycle = BicycleFactory.create_bicycle(
                bike_type, year, model, color, frame_size, wheel_size, gears, price
            )
            manager.add_sale(Sale(bicycle, quantity))
            print("Sale added.")

        elif choice == '2':
            total = manager.calculate_total_sales_from_file()
            print(f"Total Sales: €{total:.2f}")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()