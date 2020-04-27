import java.util.*;

public class FibonacciHuge {
    private static long Pisano(long m){
		long f=1;
		long s=1;
		int pisano=0;
		for(int i=1; i<(m*m)-1;i++){
			long a=(f+s)%m;
			f=s;
			s=a;
			if(f==0&&s==1){
				pisano=i+1;
				break;
}
}
		return pisano;
}
    private static long getFibonacciHuge(long n, long m) {
        if (n <= 1)
            return n;
			 
		 long n1=n % Pisano(m);
		 long x =0;
		 long y=1;
		 for(int i=1; i<n1;i++){
		 	long a=(x+y)%m;
			x=y;
		 	y=a;
    }
	return y;}
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        long m = scanner.nextLong();
        System.out.println(getFibonacciHuge(n, m));
    }
}
