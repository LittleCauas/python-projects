def celsius_fahren(temperatura):
    return (temperatura * 1.8) + 32

resultado = int (input("Informe a temperatura que deseja converter para Fahrenheit: "))

print(celsius_fahren(resultado))