# Entry point of the Git practice project
from datetime import date
from utils import add, subtract, multiply, divide

print("Name: Shihab Sarar")
print("Today's Date:", date.today())

print("Add:", add(5, 3))
print("Subtract:", subtract(10, 4))
print("Multiply:", multiply(4, 5))
print("Divide:", divide(10, 0))