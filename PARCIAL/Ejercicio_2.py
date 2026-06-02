total = 0
mayor = 0
contador = 0

for i in range(5):
    # Corrección 1: Convertir la entrada a float (número decimal)
    venta = float(input(f"Ingrese venta {i+1}: "))
    
    total = total + venta
    
    # Corrección 2: Usar '=' para asignar el nuevo valor mayor
    if venta > mayor:
        mayor = venta
        
    # Corrección 3: Comparar con un número (sin comillas)
    if venta > 1000000:
        contador += 1

promedio = total / 5
print("\n--- Resultados ---")
print("Promedio:", promedio)
print("Mayor venta:", mayor)
print("Cantidad mayores al millón:", contador)

# Error 1 
# Error 2 
# Error 3 El numero no debe tener comillas
