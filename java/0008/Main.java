import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        try (Scanner sc = new Scanner(System.in)) {
            while (sc.hasNextLong()) {
                int a = sc.nextInt();
                int b = 0;
                for (int i=0;i<10;i++){
                    for (int j=0;j<10;j++){
                        for (int k=0;k<10;k++){
                            for (int l=0;l<10;l++){
                                if (i+j+k+l == a){
                                    b++;
                                }
                            }
                        }
                    }
                }
                System.out.println(b);
            }
        }
    }
}