# 배열

## 정의
- 같은 종류의 데이터를 저장하기 위한 자료 구조
- 크기가 고정되어 있음 
  - 한번 생성된 배열은 크기 바뀔 수 없음
  - 길이 변경 필요시 새로운 배열을 생성 후 내용을 옮긴다
- 배열을 객체로 취급(참조형)
- index 번호 가지고 배열 요소에 접근
  - index 번호는 0부터 시작
- 배열이름.length를 통해 배열의 길이 조회 가능

## 배열의 선언
- `타입[] 변수` (되도록이면 이 형식 사용)
- `타입 변수[]`

![image](https://user-images.githubusercontent.com/122726684/229296798-1dc4eff7-4d67-4b7a-82cb-fae8eea06759.png)


## 배열의 생성과 초기화
- 배열 생성: 자료형의 초기값의 초기화
  - `자료형[] 변수 = new 자료형[길이];`
- 배열 생성 및 값 초기화
  - ` 자료형[] 변수 = new 자료형[] {값1, 값2, 값3};`
- 선언과 동시에 초기화
  -`자료형[] 변수 = {값1, 값2, 값3};`

- 초기값
![image](https://user-images.githubusercontent.com/122726684/229297403-293073dd-8eeb-481c-b717-d0100d4c5757.png)

## for-each
- index 대신 직접 요소에 접근하는 변수 제공
- 가독성이 개선된 반복문
1. 전통적인 for 문 (특정 범위 가능)
```java
for (int i=0; i<intArr.length;i++){
  System.out.printl(scores[i]);
}
```
2. 향상된 for문
```java
int[] intArray = {1,2,3,4,5};
for (int x: intArray){
  System.out.println(x);
}
```

## 배열의 출력
1. 반복문을 통해 출력
2. Arrays.toString(배열): 배열 안의 요소를 [값1, 값2,...] 형태로 출력
```java
int[] scores = {1,2,3,4,5}
System.out.println(Arrays.toString(scores)); 
// [1, 2, 3, 4, 5]
```

## 배열의 복사
- 새로운 배열 = Arrays.copyOf(복사하고싶은배열, 새로운 배열 크기)
- 예시:
```java
int[] scores = new int[] { 1,2,3,4,5};
int[] scores2 = Arrays.copyOf(scores, scores.length*2);
System.out.println(Arrays.toString(scores2));
// [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]
```


