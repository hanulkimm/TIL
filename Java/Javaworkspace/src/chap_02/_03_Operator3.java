package chap_02;

public class _03_Operator3 {
    public static void main(String[] args) {
//        // 비교 연산자
//        System.out.println(5 > 3);
//
//        // 논리 연산자
//        boolean 김치찌개 = true;
//        boolean 계란말이 = false;
//        boolean 제육볶음 = false;
//        System.out.println(김치찌개||계란말이||제육볶음);
//        System.out.println(김치찌개&&계란말이&&제육볶음);

        int x = 3;
        int y = 3;
        // 조건 ? 참일 경우 : 거짓
        int max = (x > y) ? x : y;
        System.out.println(max);

        int min = (x<y)?x:y;
        System.out.println(min);

        boolean b = (x==y) ? true : false;
        System.out.println(b);

        String s = (x!=y) ? "달라요" : "같아요";
        System.out.println(s);

    }
}
