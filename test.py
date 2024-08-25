from ClaseCalculadoraSimple import Calculator
arit = Calculator()
print(f"1 sumar\n2 restar\n3 multiplicar\n4 dividir\n5 salir")
"introduccion de valores"
valor_1 = float(input("introducir valor 1: "))
valor_2 = float(input("introducir valor 2: "))
arit.pedir_valores(valor_1, valor_2)
opcion = 0

while opcion != "5":
    opcion = input("elija una operacion: ")
    match opcion:
        case "1":
            print(f"la suma es: {arit.sumar()}")
        case "2":
            print(f"la resta es: {arit.restar()}")
        case "3":
            print(f"la multiplicacion es: {arit.multiplicar()}")
        case "4":
            print(f"la division es: {arit.devidir()}")