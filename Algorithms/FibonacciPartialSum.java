import java.util.*;
	
public class FibonacciPartialSum {
    private static long sum(long n){
        long a = 1;
        long b  = 1;

        for (long i = 1; i < n+1; ++i) {
            long temp = (a+b)%10;
		 a=b;
		 b =temp;
        }
		
    
        return (b-1);

}
    private static long getFibonacciPartialSumNaive(long from, long to) {
        if (to <= 1)
            return to;
	   long fromsum=sum(from-1);
	   long tosum=sum(to);
		System.out.println(fromsum+" "+tosum);
	   return Math.abs((int)tosum-fromsum);
		
		
       
    }

    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long from = scanner.nextLong();
        long to = scanner.nextLong();
        System.out.println(getFibonacciPartialSumNaive(from, to));
    }
}

