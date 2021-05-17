# DI란?

> DI? 의존성 주입?

+ **의존성**  함수에 필요한 클래스 또는 참조변수나 객체에 의존하는 것

* **주입** 외부에서  객체를 생성해서 넣어주는 것, 클래스간의 결합도를 낮춰 의존성을 줄임


1. 코드에서 두 모듈간의 연결을 의미
2. 일반적으로 둘 중 하나가 다른 하나를 어떤 용도를 위해 사용함
3. 객체지향언어에서는 두 클래스 간의 관계라고도 말함
4. 클래스간의 의존성이 줄어들면 **유지보수가 편함**

---

#### 장점

+ 객체 간의 의존성을 줄이거나 없앨수 있음
+ 객체 간의 결합도(coupling)를 낮출면서 유연한 코드 가능
+ Unit Test가 용이
+ 코드의 재사용성을 높힘
+ 리펙토링 편함

#### 단점

+ 의존성 주입을 위한 선행 작업이 필요함
+ 코드를 추적하고 읽기가 힘들어짐

----

### @SpringBootApplication - @Configuration

스프링 IOC 컨테이너에게 해당 클래스를 Bean 구성 클래스임을 알려줌

> **Bean❔**
> 클래스로 인스턴스를 요청받을때 마다 생성하면 자원 낭비이므로 클래스를 서버 실행시 한번만 생성해서 컨테이너에 등록함 여기서 등록된 클래스로 만든 인스턴스를 Bean이라 함

---

### @Bean & @Component

**@Bean**과 **@Component** 어노테이션 모두 Spring IoC 컨테이너에 Bean을 등록하도록 하는 메타데이터를 기입하는 어노테이션임

#### 1. @Bean

**@Bean** 어노테이션의 경우 개발자가 직접 제어가 불가능한 외부 라이브러리들을 Bean으로 만들기 위해 사용하며 싱글톤 객체임

```kotlin
@Configuration
class Application {
    @Bean
    fun myarray(): ArrayList<String> {
        return ArrayList<String>()
    }
}
```

ArrayList같은 라이브러리등을 Bean으로 등록하기 위해서는 별도로 해당 라이브러리 객체를 반환하는 Method를 만들고 **@Bean** 어노테이션을 붙혀줘야함 위의 경우 
**@Bean** 어노테이션에 아무런 이름도 지정하지 않았으므로 Method 이름을 **CamelCase**로 변경한 것이 Bean id로 등록됨(위 경우에선 myArray가 Bean id가 됨)



```kotlin
@Configuration
class Application {
    @Bean(name="myarray")
    fun myarray(): ArrayList<String> {
        return ArrayList<String>()
    }
}
```

**@Bean** 어노테이션에 name이라는 값을 이용하면 자신이 원하는 id로 Bean을 등록할수 있음



```kotlin
@Configuration
class Application {
    @Bean(name="myarray")
    fun myarray(): ArrayList<String> {
        return ArrayList<String>()
    }
    
    @Bean
    fun Student():Student {
        return Student(myarray())
    }
}
```

Student 객체의 경우 생성자에서 ArrayList를 주입 받도록 코드를 짜놓았다 이럴때에는 Bean으로 선언된 array()메소드를 호출함으로써 의존성을 주입할 수 있음



#### 2. @Component

 **@Component**는 개발자가 직접 작성한 Class를 Bean으로 등록하기 위한 어노테이션임
 **@Service, @Repository**등의  어노테이션에 선언되어 있음

* **@Service**
  서비스 레이어, 내부 로직을 처리함
* **@Repository** 
  퍼시스턴스(데이터 처리 담당) 레이어, DB나 파일 같은 외부 I/O를 처리함

```kotlin
@Component
class Stuent {
    fun Student() {
        println("hi")
    }
}
```

*Student Class는 개발자가 사용하기 위해서 직접 작성한 클래스, 이 Class를 Bean으로 등록하기 위해 **@Component**어노테이션을 사용했음*



```kotlin
@Component(value = "mystuent")
class Stuent {
    fun Student() {
        println("hi")
    }
}
```

**@Bean**어노테이션은 name이라는 값을 사용했지만 **@Component**어노테이션은 value값이 Bean id로 사용됨 **@Component**어노테이션도 추가 정보가 없다면 class의 이름을 CamelCase로 변경해 Bean id로 사용됨



---

### @Autowired

```kotlin
@Component
class Pencil {
	...	
}
@Component(value="myStuent")
class Student {
    @Qualifier("myPencil")
    @AutoWired
    private val pencil: Pencil
    
    constructor {
        println("hi")
    }
}
```

**@Conponent**를 사용한 Bean의 의존성 주입은 **@AutoWired**어노테이션을 이용하여 할 수 있다. 위와 같이 Student가 Pencil에 대한 의존성을 가지고 있는 경우 **@AutoWire**어노테이션을 이용하여 의존성을 자동으로 주입할 수 있다. 이때 당연히 Pencil도 **@Component**어노테이션을 가지고 있어야 함

**@AutoWired** 어노테이션의 경우 형(타입)을 통해 해당 자리에 들어올 객체를 판별해 주입해 줌. 따라서 해당 자리에 들어올 수 있는 객체가 여러개인 경우, 즉 다형성의 띄고 있는 객체타입에 @AutoWired를 사용한 경우에는 **@Qualifier("Bean이름")**을 이용해 해당 자리에 주입될 Bean을 명시해줘야함

---