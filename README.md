# Bicycle Sales Management System

This is a console-based Python project designed for managing bicycle sales and tracking total revenue.

## Features

* **Bicycle Definition:** Supports multiple bicycle types (Downhill, Ebike, Enduro, Trail, XC, Gravel) with attributes like year, model, color, frame size, wheel size, number of gears, and price.
* **Factory Pattern:** Dynamically creates bicycle objects based on type.
* **Sales Management:** Records sales with quantity and calculates total price.
* **Persistent Storage:** Automatically saves sales to a CSV file named **`sales.csv`** and can calculate total sales from the file.
* **Console Interface:** Can be extended to provide a simple command-line menu for adding and viewing sales.

## Project Structure

The project is organized into the following main files:

* **`models/bicycle.py`**: Contains the abstract `Bicycle` class.
* **`models/bicycle_types.py`**: Contains concrete bicycle subclasses (`DownhillBike`, `Ebike`, `EnduroBike`, `TrailBike`, `XCBike`, `GravelBike`).
* **`factory/bicycle_factory.py`**: Contains `BicycleFactory` for creating bicycles by type.
* **`sales/sale.py`**: Contains the `Sale` class to represent a sale of a bicycle.
* **`sales/sales_manager.py`**: Contains `SalesManager` class to manage sales and persist them to `sales.csv`.
* **`sales.csv`**: The file used for persistent sales data (created automatically on first save).

## Getting Started

### Prerequisites

This project requires **Python 3.x**. No external libraries are required beyond the Python standard library.

### Installation and Execution

1. **Clone the repository:**
    ```bash
    git clone [Your Repository URL]
    cd [project-folder-name]
    ```

2. **Run the application (example usage in a script):**
    ```bash
    python main.py
    ```

### Usage

Example workflow in code:

1. **Create a bicycle:**
    ```python
    from factory.bicycle_factory import BicycleFactory

    bike = BicycleFactory.create_bicycle(
        bike_type="Downhill",
        year=2025,
        model="DHX-300",
        color="Red",
        frame_size="M",
        wheel_size=29,
        number_of_gears=12,
        price=2500
    )

    print(bike.display_info())
    # Output: Downhill Bike - DHX-300, €2500
    ```

2. **Record a sale:**
    ```python
    from sales.sale import Sale
    from sales.sales_manager import SalesManager

    manager = SalesManager()
    sale = Sale(bike, quantity=2)
    manager.add_sale(sale)
    ```

3. **Calculate total sales:**
    ```python
    total = manager.calculate_total_sales_from_file()
    print(f"Total sales: €{total}")
    ```

All changes are automatically saved to the `sales.csv` file.

## Class Overview

### `Bicycle` (in `models/bicycle.py`)

Abstract base class representing a bicycle.

| Attribute | Description | Type |
| :--- | :--- | :--- |
| `year` | Production year | `int` |
| `model` | Bicycle model | `str` |
| `color` | Bicycle color | `str` |
| `frame_size` | Frame size | `str` |
| `wheel_size` | Wheel diameter | `int` |
| `number_of_gears` | Number of gears | `int` |
| `price` | Price in euros | `float` |

| Method | Description |
| :--- | :--- |
| `display_info()` | Abstract method to return formatted bicycle info. |

### `BicycleFactory` (in `factory/bicycle_factory.py`)

Creates bicycles based on a string type.

| Method | Description |
| :--- | :--- |
| `create_bicycle(bike_type, year, model, color, frame_size, wheel_size, number_of_gears, price)` | Returns a new bicycle object of the specified type. |

### `Sale` (in `sales/sale.py`)

Represents a bicycle sale.

| Attribute | Description |
| :--- | :--- |
| `bicycle` | Bicycle object | `Bicycle` |
| `quantity` | Number of bicycles sold | `int` |

| Method | Description |
| :--- | :--- |
| `total_price()` | Returns the total price of the sale (`price * quantity`). |

### `SalesManager` (in `sales/sales_manager.py`)

Manages sales and persists them to CSV.

| Method | Description |
| :--- | :--- |
| `add_sale(sale)` | Adds a sale and saves it to `sales.csv`. |
| `save_sales()` | Writes all sales to the CSV file. |
| `calculate_total_sales_from_file()` | Reads `sales.csv` and calculates total sales. |
