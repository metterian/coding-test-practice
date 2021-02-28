# 10828번 - 스택   
## 문제   
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.   
   
명령은 총 다섯 가지이다.   
   
## 입력   
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.   
   
## 출력   
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.   
   
## 예제 입력 1   
```   
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
```   
```   
2
2
0
2
1
-1
0
1
-1
0
3
```   
## 예제 출력 1   
```   
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
```   
```   
2
2
0
2
1
-1
0
1
-1
0
3
```   
## 예제 입력 2   
```   
7
pop
top
push 123
top
pop
top
pop
```   
```   
-1
-1
123
123
-1
-1
```   
## 예제 출력 2   
```   
7
pop
top
push 123
top
pop
top
pop
```   
```   
-1
-1
123
123
-1
-1
```   

### 출처
https://www.acmicpc.net/problem/10828