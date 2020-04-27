import java.util.*;

public class FibonacciLastDigit {
    private static int getFibonacciLastDigitNaive(int n) {
        if (n <= 1)
            return n;
	   int a=1;
	   int b=1;
	   for(int i=1;i<n-1;i++){
		int temp=(a+b)%10;
		a=b;
		b=temp;
}
		return b%10;
}    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int c = getFibonacciLastDigitNaive(n);
        System.out.println(c);
    }
}

