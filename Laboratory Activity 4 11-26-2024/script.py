from Capybara import Capybara

capybara1 = Capybara("Biscoff", "M", 5)

test_case = int(input("Enter the test case number: "))

if test_case == 1:
    print(f"Test Case 1: Name: {capybara1.name}, Gender: {capybara1.gender}, Age: {capybara1.age} years old")