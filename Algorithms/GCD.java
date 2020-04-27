import java.util.*;

public class GCD {
  private static int gcd(int a, int b) {
	int x=a;
	int y=b;
    if(a==b)
		return b;

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
	return x;
}
else if(x==0){
	return y;
}
else
	return 0;
  }

  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);
    int a = scanner.nextInt();
    int b = scanner.nextInt();

    System.out.println(gcd(a, b));
  }
}
