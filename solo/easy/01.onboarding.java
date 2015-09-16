import java.util.*;
class Player {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        while(true){
           String e=in.next();
           int d=in.nextInt();
           String E=in.next();
           int D=in.nextInt();
           System.out.println((d<D)?e:E);
        }
    }
}