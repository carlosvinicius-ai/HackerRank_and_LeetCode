package com.beecrowd;

import java.util.Scanner;

/**
 * beecrowd 1004
 * https://judge.beecrowd.com/en/problems/view/1004
 *
 * @ carlosvinicius-ai*/

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();

        int PROD = A * B;

        System.out.println(String.format("PROD = %d",PROD));
    }
}