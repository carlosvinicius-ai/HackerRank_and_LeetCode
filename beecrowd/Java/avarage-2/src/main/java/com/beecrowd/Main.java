package com.beecrowd;

import java.util.Scanner;

/**
 * beecrowd 1006
 * https://judge.beecrowd.com/en/problems/view/1006
 *
 * @ carlosvinicius-ai*/

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        float A = sc.nextFloat();
        float B = sc.nextFloat();
        float C = sc.nextFloat();

        float media = (float) ((A * 2.0) + (B * 3.0) + (C * 5.0)) / (float) (2.0 + 3.0 + 5.0);

        System.out.println(String.format("MEDIA = %.1f", media));
    }
}
