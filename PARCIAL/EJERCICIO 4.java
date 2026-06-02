/*Un laboratorio desea analizar una secuencia de ADN.

Entrada:
ATCGGATAA

Salida esperada:
    A: 4
    T: 2
    C: 1
    G: 2
*/

import java.util.Scanner;

public class Adn {

    static int contar(String adn, char base) {
        int contador = 0;

        for (int i = 0; i < adn.length(); i++) {
            if (adn.charAt(i) == base) {
                contador++;
            }
        }

        return contador;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Ingrese ADN: ");
        String adn = sc.nextLine();

        int a = contar(adn, 'A');
        int t = contar(adn, 'T');
        int c = contar(adn, 'C');
        int g = contar(adn, 'G');

        System.out.println("A: " + a);
        System.out.println("T: " + t);
        System.out.println("C: " + c);
        System.out.println("G: " + g);
    }
}
