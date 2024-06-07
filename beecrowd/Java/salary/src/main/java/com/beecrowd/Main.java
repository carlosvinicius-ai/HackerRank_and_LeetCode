package com.beecrowd;

import java.util.Scanner;

/**
 * beecrowd 1008
 * https://judge.beecrowd.com/en/problems/view/1008
 *
 * @ carlosvinicius-ai*/

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int number = sc.nextInt();
        int hour = sc.nextInt();
        float salaryHour = sc.nextFloat();

        float salaryMonth = (float) hour * salaryHour;

        System.out.println(String.format("NUMBER = %d", number));
        System.out.println(String.format("SALARY = U$ %.2f", salaryMonth));
    }
}