Bicycle Sales System

A Python OOP project using abstract classes, inheritance, the factory pattern, and CSV data storage.

This project is a console-based bicycle sales management system designed to demonstrate solid OOP principles, modular code structure, and file handling.
It is suitable for coursework, university projects, or practical learning of Python architecture.

Project Structure
project/
│
├── models/
│   ├── bicycle.py
│   ├── bicycle_types.py
│   └── factory.py
│
├── sales/
│   ├── sale.py
│   └── sales_manager.py
│
├── main.py
└── sales.csv    # Automatically created after first sale

Features
Multiple Bicycle Types

The system supports creating bicycles of various categories:

Downhill

Ebike

XC

Enduro

Trail

Gravel

Each type derives from the abstract base class Bicycle.

Add Sales

The user can input all bicycle details:

year

model

color

frame size

wheel size

number of gears

price

quantity

Every sale is saved to sales.csv.

Calculate Total Sales Revenue

The program reads the CSV file, calculates and displays total revenue.

Input Validation

User input is validated to ensure correctness:

valid bicycle type

year not exceeding 2025

color must not contain digits

valid frame and wheel sizes

gears must match allowed values

price and quantity must be positive numbers

How to Run

Install Python 3.9+

Download the project

Run:

python main.py

OOP Concepts Used
OOP Concept	Implementation Location
Abstraction	Bicycle (abstract base class)
Inheritance	All concrete bicycle classes
Polymorphism	Overridden display_info() methods
Encapsulation	Private attributes (_year, _price)
Factory Pattern	BicycleFactory
Modular Structure	Code split into multiple modules

Example CSV Output

sales.csv after adding some sales:

Type,Year,Model,Color,Frame size,Wheel size,Number of gears,Price,Quantity,Total
Enduro,2023,Rallon,Blue,l,29,12,3500,2,7000
Ebike,2024,Levo,Red,m,29,12,8900,1,8900

Technologies Used

Python 3

ABC (Abstract Base Class)

CSV Module

Factory Pattern

Modular Code Architecture

Author

Created by Philipp — Electronics Faculty, Vilnius Tech.

License

Open for educational and academic use.