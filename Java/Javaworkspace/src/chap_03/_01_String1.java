package chap_03;

public class _01_String1 {
    public static void main(String[] args) {
        String s = "I like Java and Python and C.";
//        System.out.println(s);
//        System.out.println(s.length());
//        System.out.println(s.toLowerCase());
//        System.out.println(s.contains("Java")); //포함
//        System.out.println(s.indexOf("Java")); // index
//        System.out.println(s.indexOf("C#")); // -1
//        System.out.println(s.lastIndexOf("and"));
//        System.out.println(s.startsWith("i like"));

        System.out.println(s.replace("and", ","));
        System.out.println(s.substring(7));
        System.out.println(s.substring(s.indexOf("Java")));
        System.out.println(s.substring(s.indexOf("Java"), s.indexOf(".")));
        s = "          I hate Java.     ";
        System.out.println(s);
        System.out.println(s.trim());
        String s1 = "Java";
        String s2 = "Python";
        System.out.println(s1+","+s2);
        System.out.println(s1.concat(",").concat(s2));
    }
}
