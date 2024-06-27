package estudo.udemy;

import java.util.Scanner;

/**
 * beecrowd 1012
 * https://judge.beecrowd.com/en/problems/view/1012
 *
 * @ carlosvinicius-ai*/

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        double A = sc.nextDouble();
        double B = sc.nextDouble();
        double C = sc.nextDouble();

        double triangle = 1.0 / 2.0 * A * C;
        double circle = 3.14159 * Math.pow(C, 2);
        double trapezoid = (A + B) / 2 * C;
        double square = Math.pow(B,2);
        double rectangle = A * B;

        System.out.println(String.format("TRIANGULO: %.3f", triangle));
        System.out.println(String.format("CIRCULO: %.3f",circle));
        System.out.println(String.format("TRAPEZIO: %.3f",trapezoid));
        System.out.println(String.format("QUADRADO: %.3f",square));
        System.out.println(String.format("RETANGULO: %.3f",rectangle));

        sc.close();
    }
}