import java.util.Scanner;

class Main{
   public static void main(String[] args){
       Scanner sc = new Scanner(System.in);
       int a = sc.nextInt();
       int b = sc.nextInt();
       int c = sc.nextInt();
       
       int x = (a+b)%c;
       int y = (a*b)%c;
           
       System.out.println(x);
       System.out.println(x);
       System.out.println(y);
       System.out.println(y);
   } 
}