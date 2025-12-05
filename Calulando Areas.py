#1. DEFINICIÓN DE FUNCIONES
#Se crean bloques separados para cada tarea.

def calcular_area_cuadrado():
    print("\n--- Área del Cuadrado ---")
    # Entrada de datos (convertirlos a float para permitir decimales)
    lado = float(input("Ingresa el valor del lado: "))
    # Procesamiento
    area = lado * lado
    # Salida
    print("El área del cuadrado es:", area)

def calcular_area_triangulo():
        print("\n--- Área del Triángulo ---")
        base = float(input("Ingresa la base: "))
        altura = float(input("Ingresa la altura: "))
        area = (base * altura) / 2
        print("El área del triángulo es:", area)

def calcular_area_circulo():
      print("\n--- Área del Círculo ---")
      radio = float(input("Ingresa el radio: "))
      pi = 3.1416
      area = pi * (radio * radio) #radio al cuadrado
      print("El área del círculo es:", area)

# 2. PROGRAMA PRINCIPAL (MENÚ)
#Uso de ciclo 'While' para mantener el programa activo

print("¡Bienvenido a la calculadora geométrica!")
mantener_programa = True

while mantener_programa:
      print("\n¿Qué deseas calcular?")
      print("1. Cuadrado")
      print("2. Triángulo")
      print("3. Círculo")
      print("4. Salir")

      # Capturamos la opción del usuario
      opcion = input("Elige una opción (1-4): ")

      # Estructura de decisión lógicca (If/Else)
      if opcion == "1":
        calcular_area_cuadrado()
      elif opcion == "2":
        calcular_area_triangulo()
      elif opcion == "3":
        calcular_area_circulo()
      elif opcion == "4":
        print("Cerrando programa...")
        mantener_programa = False #Esto rompe el ciclo
      else:
          print("Opción no válida, intenta de nuevo.")