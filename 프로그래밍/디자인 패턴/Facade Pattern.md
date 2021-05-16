## 디자인 패턴 - Facade Pattern. 퍼사드 패턴

#### 퍼사드 패턴

어떤 서브시스템의 일련의 인터페이스에 대한 통합된 인터페이스를 제공함
퍼사드에서 고수준 인터페이스를 정의하기 때문에 서브시스템을 더 쉽게 정의할 수 있음



#### 예제

```kotlin
//RemoteControl.kt

class RemoteControl{
    fun turnOn() {
    	println("TV를 킴")
    }
    fun turnOff() {
        println("TV를 끔")
    }
}
```

```kotlin
//Movie.kt

class Movie(
    private var name: String
) {
    fun searchMovie() {
        println("$name 영화를 찾음")
    }
    
    fun payMovie() {
        println("영화를 결제함")
    }
    
    fun playMovie() {
        println("영화 재생")
    }
}
```

```kotlin
//Beverage.kt

class Beverage(
    private var name: String
) {
    fun prepare() {
        println("준비완료")
    }
} 
```

```kotlin
//MovieFacade.kt

class MovieFacade(
    private var beverageName: String
    private var movieName: String
) {
    fun viewMovie() {
        val beverage = Beverage(beverageName)
        val romote = RemoteControl()
        val movie = Movie(movieName)
        
        beverage.prepare()
        remote.turnOn()
        movie.apply {
            searchMovie()
            payMovie()
            playMovie()
        }
    }
}
```



```kotlin
//Main

fun main() {
   val movieFacade = MovieFacade("제로콜라", "마스")
   movieFacade.viewMovie()
}
```

