#  TDD

### TDD란

 '테스트 주도 개발' **TDD**(Test Driven Development)은 설계 이후 코드 개발 및 테스트케이스를 작서하는 기존ㅇ의 개발 프로세스와 다르게 테스트 케이스를 작성 한 후 실제 코드를 개발하여 리펙토링하는 절차를 따른다.

 <img src="C:\Users\kangsinhee\AppData\Roaming\Typora\typora-user-images\image-20200723202643172.png" alt="image-20200723202643172" style="zoom:50%;" />

*기존 프로세스*

<img src="C:\Users\kangsinhee\AppData\Roaming\Typora\typora-user-images\image-20200724001118983.png" alt="image-20200724001118983" style="zoom: 40%;" />

*TDD 프로세스*





----

array라는 클래스는 sum이라는 funtion을 가짐 sum의 입력값은 아래와 같음

* 첫 번째 Argument는 덧셈에 필요한 숫자의 개수를 전달한다.
* 두 번째 Argument는 덧셈에 필요한 숫자를 공백을 포함한 문자열의 형태로 전달한다.

그리고 출력 값은 아래와 같음

- 두 번째 Argument로 전달된 숫자들의 합을 반환한다.
- 첫 번째 Argument의 숫자와 두 번째 Argument의 숫자의 개수가 같은지 체크하고 틀리다면 예외를 발생시킨다.

### **INPUT**

Case 1.

```python
> 6
> 1 2 3 4 5
```

*예외 발생*

Case 2.

```python
> 6
> 1 2 3 4 5 6
```

*첫 번째 전달인자에는 6개이라면 두번째 전달인자에서는 6개의 숫자와 공백을 포함하는 문자열을 전달함*

### OUTPUT

```python
21
```

