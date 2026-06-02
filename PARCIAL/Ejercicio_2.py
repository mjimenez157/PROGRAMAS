total = 0
mayor = 0
contador = 0

for i in range(5):
    venta = float(input(f"Ingrese venta {i+1}: "))
    
    total = total + venta
    
    if venta > mayor:
        mayor = venta
        
    if venta > 1000000:
        contador += 1

promedio = total / 5
print("\n--- Resultados ---")
print("Promedio:", promedio)
print("Mayor venta:", mayor)
print("Cantidad mayores al millón:", contador)

# Error 1 El input guarda lo q escribe el ususario como texto, como no se puede sumar el numero con texto se usa float para convertir el texto en numero
# Error 2 El == es para comparar si son iguales en cambio = es para asignar
# Error 3 El numero no debe tener comillas
