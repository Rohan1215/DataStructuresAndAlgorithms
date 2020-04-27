import java.util.*;

public class FibonacciSumLastDigit {
    private static long getFibonacciSumNaive(long n) {
        if (n <= 1)
            return n;

        long a = 1;
        long b  = 1;

        for (int i = 1; i < n+1; ++i) {
            long temp = (a+b)%10;
		 a=b;
		 b =temp;
        }
		

        return (b-1);
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        long s = getFibonacciSumNaive(n);
        System.out.println(s);
    }
}

