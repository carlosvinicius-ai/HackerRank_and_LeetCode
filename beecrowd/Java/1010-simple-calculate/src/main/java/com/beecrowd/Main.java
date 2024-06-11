package com.beecrowd;

import java.util.Scanner;

/**
 * beecrowd 1010
 * https://judge.beecrowd.com/en/problems/view/1010
 *
 * @ carlosvinicius-ai*/

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int firstCode = sc.nextInt();
        int firstQuant = sc.nextInt();
        double firstPrice = sc.nextDouble();
        int secondCode = sc.nextInt();
        int secondQuant = sc.nextInt();
        double secondPrice = sc.nextDouble();

        double finalPrice = (firstQuant * firstPrice) + (secondQuant * secondPrice);

        System.out.println(String.format("VALOR A PAGAR: R$ %.2f", finalPrice));

        sc.close();
    }
}