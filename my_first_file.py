import sympy as sp

# Определение переменной
x = sp.Symbol('x')

# Определение функции, которую нужно интегрировать
func = sp.sin(x)  # Например, sin(x)

# Вычисление определённого интеграла
integral = sp.integrate(func, (x, 0, sp.pi))

print(f"Результат интеграла: {integral}")
print(f"123")
print("local")
