## Unit & Nothing Type in Kotlin

> 코틀린에서는 데이터와 관계없이 상황을 표현하기 위한 Unit과 Nothing이라는 타입을 제공함

#### Unit 

Unit은 자바에서 Void에 해당하는 예약어로써 아무것도 반환하지 않는 것을 의미함
또한 Unit은 일반적으로 생략이 가능함

자바의 Void와 다른 점

1. Unit은 싱글톤 인스턴스이기에 객체임과 동시에 타입임

2. Unit 또한 Any의 서브 클래스에 포함됨

#### Nothing

Nothing은 어떠한 값도 포함하지 않는 타입임
Private constructor로 정의 되어 있어 인스턴스를 생성할 수 없음

Nothing은 다음과 같은 상황에서 사용함

* 함수가 리턴될 일이 없을 경우
* 예외를 던지는 함수의 리턴 타입



### Reference

* https://readystory.tistory.com/143
* https://skasha.tistory.com/m/55?category=800418