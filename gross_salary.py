import sys

def calculate_gross_salary(basic_salary, hra_percent, da_percent):
    hra = basic_salary * hra_percent / 100
    da = basic_salary * da_percent / 100
    gross_salary = basic_salary + hra + da

    print("Basic Salary =", basic_salary)
    print("HRA =", hra)
    print("DA =", da)
    print("Gross Salary =", gross_salary)

    return gross_salary

if __name__ == "__main__":
    basic_salary = float(sys.argv[1])
    hra_percent = float(sys.argv[2])
    da_percent = float(sys.argv[3])

    calculate_gross_salary(basic_salary, hra_percent, da_percent)