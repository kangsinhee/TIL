## Null Safely in Kotlin

> 코틀린의 대표되는 장점 중 하나인 안전한 Null 처리를 알아보자

코틀린에서는 자바보다 null처리를 좀더 명확하게 함
*NPE 발생 빈도를 현저히 낯출 수 있음*

#### Type의 Null able

* 코틀린은 기본적으로 객체를 불변으로 취급하며, null값을 허용하지 않음
* null을 허용 하려면 별도의 연산자를 사용해 초기화해야 함
* null값이 허용된 자료형을 사용할 때 별도 연산자를 통해 안전하게 호출해야 함

```kotlin
fun gerLen(str: String?): Int? = str?.length
```

타입에 ? 연산자를 붙임으로서 null이 가능한 변수임을 명시적으로 표현함

#### Null safe operator

null을 안전하게 처리하기 위해 코틀린은 `?.` 연산자를 지원함

`?.` 연산자를 사용하면, 앞의 변수가 null이 아닐때만 오른쪽 함수가 실행되고 null이면 null을 반환함

```kotlin
fun Person.countryName(): String { 
    val country = this.company?.address?.country 
    return country
    	?: "Unknown"
}
```

다음과 같이 연속적인 사용도 가능함

#### Evis operator

`?.` 연산자는 좌항이 null이면 null을 반환함
`?:` 연산자는 null인경우 동작하는 연산자임

위 코드의 `return country
    	?: "Unknown"`를 엘비스 연산자라 함
우항으로 `throw`나 `return`등 다양한 활용이 가능함

#### Safe cast

스마트 캐스트인 `is` 를 이용하면 **`as`**를 사용하지 않고도 type을 변환할 수 있음
단 as를 바로 사용하여 casting을 할때 **type이 맞지 않으면 `ClassCastException`이 발생**함

Kotlin에선 이를 방지하기 위해 `as?`를 지원함
`as?` 는 casting을 시도하고, **casting이 불가능 하면 null을 반환**함

#### 강제 not null 처리

변수를 `nullable`로 설정한다면 해당 변수는 사용할 때마다 null처리를 진행해야 함
코드 flow상 null 이 들어가지 않는 경우에도 계속 null 처리를 진행하는 비효율이 발생함

*강제로 `nullable`로 설정된 프로퍼티를 not null로 바꿔주는 `!!` 연산자를 지원함*

만약 `!!`연산자를 설정해 놓고 null이 들어가게 된다면 NPE가 발생하게 됨

### let 함수

코틀린에선 `not null`인 경우에만 코드를 실행 시켜주는 `let`이라는 scope 함수를 지원함
`let` 함수를 사용하면 자신의 receiver 객체를 람다식 내부로 넘겨줌

#### nullable Type의 확장 함수

null이 가능한 객체에 확장 함수를 사용할 수 있음

`isNullorEmpty()`, `isNullorBlank()`등의 null을 체크할 수 있는 확장 함수들을 지원함

#### Generic의 Nullable

Generic을 사용하면 이는 무조건 `nullable`로 인식 됨

```kotlin
fun <T> printHashCode(t: T) { 
    println(t?.hashCode()) 
} 

fun main(args: Array) { 
    printHashCode(null) 
}
```

T에 `?` operator가 붙지 않았지만 붙은것과 다름이 없음

*따라서 함수 내부에 반드시 null check를 해줘야 함*

`non-null`이 디폴트인 Generic을 사용하기 위해선 **upper bound에 대한 제한**을 명시적으로 넣어야 함

```kotlin
fun <T: Any> printHashCode(t: T) { 
    println(t.hashCode()) 
} 

fun main(args: Array) { 
    printHashCode(null) 
}
```

T는 Any의 상한제한을 갖기 때문에 이제 T는 `Not null` type임



### Reference🌌

* [투털씨의 리얼 블로그](https://tourspace.tistory.com/114?category=797357)

