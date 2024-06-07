package com.beecrowd;

import java.util.Scanner;

/**
 * beecrowd 1005
 * https://judge.beecrowd.com/en/problems/view/1005
 *
 * @ carlosvinicius-ai*/

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        float A = sc.nextFloat();
        float B = sc.nextFloat();

        float media = (float) ((A * 3.5) + (B * 7.5))  / (float) (3.5 + 7.5);

        System.out.println(String.format("MEDIA = %.5f", media));
    }
}