import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        double total = 0;
        double total_score = 0;
        for (int i = 0; i < 20 ; i++) {
            StringTokenizer st = new StringTokenizer(sc.next());
            String major = st.nextToken();
            double score = Double.parseDouble(st.nextToken());

            total_score += score;
            double add = 0;
            String grade = st.nextToken();
            if (grade.charAt(0)=='A') {
                if (grade.charAt(1)=='+') {
                    add = score * 4.5;
                } else {
                    add = score * 4;
                }
            } else if (grade.charAt(0)=='B') {
                if (grade.charAt(1)=='+') {
                    add = score * 3.5;
                } else {
                    add = score * 3;
                }
            } else if (grade.charAt(0)=='C') {
                if (grade.charAt(1)=='+') {
                    add = score * 2.5;
                } else {
                    add = score * 2;
                }
            } else if (grade.charAt(0)=='D') {
                if (grade.charAt(1)=='+') {
                    add = score * 1.5;
                } else {
                    add = score * 1;
                }
            }
            total += add;
        }
        System.out.println(total/total_score);
    }
}

