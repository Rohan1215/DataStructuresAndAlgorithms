import java.util.*;

public class LCM {
  private static long lcm(long a, long b) {
	long x=a;
	long y=b;
    if(a==b)return a;
    if(a>b){
	while(x!=0&&y!=0){
		x=x%y;
		if(x!=0&&y!=0){
			y=y%x;
}	
}	
}
    if(b>a){
	while(x!=0&&y!=0){
		y=y%x;
		if(x!=0&&y!=0){
			x=x%y;
}	
}}
if(y==0){
	return (a*b)/x;
}
else if(x==0){
	return (a*b)/y;
}
else

	return 0;
  


  }

  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);
    long a = scanner.nextInt();
    long b = scanner.nextInt();

    System.out.println(lcm(a, b));
  }
}
