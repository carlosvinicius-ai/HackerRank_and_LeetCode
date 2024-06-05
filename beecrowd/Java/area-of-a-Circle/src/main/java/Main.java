import java.util.Scanner;

/**
 * beecrowd 1002
 * https://judge.beecrowd.com/en/problems/view/1002
 *
 * @ carlosvinicius-ai*/

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        final double n = 3.14159;
        double A, R;

        R = sc.nextDouble();

        A = n * Math.pow(R, 2);

        System.out.println(String.format("A=%.4f", A));
    }

}
