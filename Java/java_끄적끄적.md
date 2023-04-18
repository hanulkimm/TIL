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

## String
### 특정 문자 출력
`System.out.println(s.charAt(i-1))`
### slice
`System.out.println(s.substring(i-1,i))`

## charAt
- 아스키 코드로 변환해주기 때문
- `-0`을 해주기

## 배열 이쁘게 출력
`System.out.println(Arrays.toString(arr))`