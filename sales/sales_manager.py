import csv
from .sale import Sale

class SalesManager:
    def __init__(self):
        self.sales = []
        self.filename = 'sales.csv'

    def add_sale(self, sale):
        self.sales.append(sale)
        self.save_sales()

    def save_sales(self):
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                rows = list(reader)
                file_empty = len(rows) <= 1
        except FileNotFoundError:
            file_empty = True

        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)

            if file_empty:
                writer.writerow(["Type", "Year", "Model", "Color",
                                 "Frame size", "Wheel size",
                                 "Number of gears", "Price",
                                 "Quantity", "Total"])

            for sale in self.sales:
                writer.writerow([
                    sale.bicycle.__class__.__name__.replace("Bike", ""),
                    sale.bicycle.year,
                    sale.bicycle.model,
                    sale.bicycle.color,
                    sale.bicycle.frame_size,
                    sale.bicycle.wheel_size,
                    sale.bicycle.number_of_gears,
                    sale.bicycle.price,
                    sale.quantity,
                    sale.total_price()
                ])

    def calculate_total_sales_from_file(self):
        total_sales = 0.0
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    total_sales += float(row['Price']) * int(row['Quantity'])
            return total_sales
        except Exception:
            return 0.0