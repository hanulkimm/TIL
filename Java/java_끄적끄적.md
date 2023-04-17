## HashSet
- 순서없음
- 중복 허용 안함
- null 허용

```java
import java.io.IOException;
import java.util.HashSet;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc= new Scanner(System.in);
        HashSet<Integer> h = new HashSet<Integer>();
        for (int i = 0; i < 10; i++) {
            int num = sc.nextInt();
            h.add(num);
        }
        sc.close();
        System.out.println(h.size());
        }
        
    }
```