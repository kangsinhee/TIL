## Object vs Class in Kotlin

`object` 키워드는 다음과 같은 경우에 사용됨

* 익명객체를 생성할때 
* 싱글톤 클래스로 만들때

---

#### object 싱글턴 클래스 정의

```kotlin
class Car(power: Int) {}

//class가 있어야 할 위치에 object를 입력하면 이 클래스는 싱글턴으로 동작함
object CarFactory {
    val cars = mutableListOf<Car>()

    fun makeCar(horsePowers: Int): Car {
        val car = Car(horsePowers)
        cars.add(car)
        return car
    }
}
```

```kotlin
val car = CarFactory.makeCar(100)
println(carFactory.cars.power)
```

다음 코드의 CarFactory makeCar()처럼 메소드에 접근하여 Car 객체를 생성할 수 있음
*CarFactory객체는 싱글턴으로 구현이 되었기 때문에 여러번 호출해도 한 번만 생성됨*

프로그램이 로딩될 때 생성되므로 쓰레드 안전성이 보장되지만, 내부적으로 공유자원을 사용하는 경우 
쓰레드 안전성이 보장되지 않기 때문에 동기화 코드를 작성해야 함

---

#### companion object 싱글턴 클래스 정의

```kotlin
class Car(val horsePowers: Int) {
    companion object Factory {
        val cars = mutableListOf<Car>()
        
        fun makeCar(horsePowers: Int): Car {
            val car = Car(horsePowers)
            cars.add(car)
            return car
        }
    }
}
```

다음 코드는 Car class 내부에 Factory 패턴을 정의하기 위해 `companion object`를 사용함

```kotlin
Car.makeCar()
Car.Factory.makeCar()
```

 두번째 줄의 `Car.Factory.makeCar()`가 정확한 표현이지만 
코틀린에선 편의를 위해 **Factory를 생략가능**하며 `Car.makeCar()`로 호출 할 수 있음

---

#### object 를 익명객체로 사용한 예제

`object`는 익명객체를 정의할 때도 사용됨 익명객체는 이름이 없는 객체로, 한 번만 사용되고 재사용하지 않을 때 사용함

```kotlin
interface Car {
	fun drive(): String
}

fun start(car: Car) = println(car.drive())
```

```kotlin
start(object: Car {
    override fun drive() = "Driving~"
})
```

다음 코드에서 start()의 인자로 전달되는 `object: Car{ .. }`는 익명객체임

익명객체는 Car 인터페이스를 상속받은 클래스를 객체로 생성된 것을 의미함

익명객체이기 때문에 클래스 이름은 없고, 구현부는 { .. }안에 정의해야 함

