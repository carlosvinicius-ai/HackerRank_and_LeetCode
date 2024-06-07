package com.beecrowd;

/**
 * beecrowd 1007
 * https://judge.beecrowd.com/en/problems/view/1007
 *
 * @ carlosvinicius-ai*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        int D = sc.nextInt();

        int DIFFERENCE = (A * B - C * D);

        System.out.println(String.format("DIFERENCA = %d", DIFFERENCE));
    }
}