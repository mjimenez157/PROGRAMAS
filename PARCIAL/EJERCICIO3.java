/*Un laboratorio registra temperaturas durante 7 días.

El sistema debe:

calcular promedio
indicar temperatura más baja
mostrar cuántas temperaturas fueron mayores a 30°

El siguiente código contiene errores.

Actividades
Corrija el programa.
Explique los errores encontrados.
El programa debe ejecutar correctamente.
*/


import java.util.Scanner;

public class Temperaturas {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int suma = 0;
        int menor = 0;
        int contador = 0;

        for (int i = 1; i <= 7; i++) {

            System.out.print("Ingrese temperatura: ");
            int temp = sc.nexInt();         /*  La temperatura estaba como texto string y la temperatura debe ser numero  */
            suma = suma + temp;
            
             if(temp < menor){
                menor = temp;
            }

            if(temp > 30){
                contador++;
            }
        }

        double promedio = suma / 7.0;
        System.out.println("Promedio: " + promedio);
        System.out.println("Menor: " + menor);
        System.out.println("Mayores a 30: " + contador);
    }
}
