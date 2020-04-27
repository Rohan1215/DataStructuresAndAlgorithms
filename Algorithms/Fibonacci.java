import java.util.Scanner;

public class Fibonacci {
  private static long calc_fib(int n) {
    if (n <= 1){
      return n;}

int array[]=new int[n+1];
    array[0]=0;
    array[1]=1;
    
    for(int i=2;i<(n+1);i++){
	array[i]=array[i-1]+array[i-2];
}
  return array[n];
  }

  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();

    System.out.println(calc_fib(n));
  }
}
