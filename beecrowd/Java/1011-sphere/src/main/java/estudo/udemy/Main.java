package estudo.udemy;

import java.util.Scanner;

/**
 * beecrowd 1011
 * https://judge.beecrowd.com/en/problems/view/1012
 *
 * @ carlosvinicius-ai*/


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int r = sc.nextInt();

        double volume = (4.0/3.0) * 3.14159 * Math.pow(r,3);

        System.out.println(String.format("VOLUME = %.3f", volume));
    }
}