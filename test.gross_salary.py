from gross_salary import calculate_gross_salary

def test_salary_1():
    assert calculate_gross_salary(50000, 20, 10) == 65000

def test_salary_2():
    assert calculate_gross_salary(10000, 20, 10) == 13000

def test_salary_3():
    assert calculate_gross_salary(20000, 15, 5) == 24000