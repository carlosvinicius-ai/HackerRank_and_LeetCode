package com.beecrowd;

import java.util.Scanner;

/**
 * beecrowd 1009
 * https://judge.beecrowd.com/en/problems/view/1009
 *
 * @ carlosvinicius-ai*/

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String name = sc.nextLine();
        double salary = sc.nextDouble();
        double sales = sc.nextDouble();

        double bonus = sales * 0.15;
        salary += bonus;

        System.out.println(String.format("TOTAL = R$ %.2f", salary));


        sc.close();
    }
}