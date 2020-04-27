import java.util.*;

public class FibonacciSumSquares {
    private static long getFibonacciSumSquaresNaive(long n) {
        if (n <= 1)
            return n;
	   long a=1;
	   long b=1;
	   for(long i=0; i<n-1;i++){
		long temp=a+b;
		a=b;
		b=temp;
 
		
		}
		return ((a%10)*(b%10))%10;
}    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        long s = getFibonacciSumSquaresNaive(n);
        System.out.println(s);
    }
}

