## JPA와 Mybatis

---

내가 뭘 쓰고 있었는지도 뭐가 다른건지도 모르겠다 ㅅ~ㅂ

### JPA(Java Rersistent API)

JPA는 Java Rersistent API의 약자로 자바 어플리케이션에서 RDB를 사용하는 방식(기술명세)을 정의한 **인터페이스**임 
흔히 JPA와 Spring Data JPA, Hibernate를 혼동하기 쉬움

*JPA는 말 그대로 인터페이스이며 구현이 없으므로 특정 기능을하는 라이브러리가 아님*

#### 장점

* CRUD 쿼리 자동 생성
* Entity에 속성만 추가하면 쿼리를 건들 필요 x

#### 단점

* 상대적(Mybatis)으로 학습이 어려움
* 복잡한 쿼리 작성이 어려움

#### Hibernate

**Hibernate는 JPA의 구현체**
*JPA라는 인터페이스를 구현한 **라이브러리임***

JPA를 사용하기 위해 반드시 Hibernate를 사용할 필요가 전혀 없으며, JPA의 구현체는 Hibernate만 있는 것이 아님. 직접 JPA를 구현해 사용할 수도 있음



#### Spring Data JPA

Spring Data JPA는 Spring에서 제공하는 모듈 중 하나로 개발자가 JPA를 더 쉽고 편하게 사용할 수 있도록 도와줌

DB에 접근할 필요가 있는 대부분의 상황에서 **EntityManager**이 아닌 **Repository**라는 인터페이스를 정의해 메소드에 입력하면 Spring이 알아서 메소드 이름에 적합한 쿼리를 날리는 구현체를 만들어 Bean으로 등록해줌

![overall_design](C:\Users\kangsinhee\Desktop\programming\Study_Backend\Spring boot\JPA와 Mybatis\overall_design.png)

### Mybatis

Java는 DB 접근을 위해 JDBC라는 라이브러리를 제공함
Mybatis라는 모듈을 통해 이 JDBC를 사용하기 쉽게 만들어 줌    

#### 장점

* 학습이 쉬움
* 소스코드와 쿼리를 분리할 수 있음

#### 단점

* 반복적인 작업이 반복됨



### Reference

* https://velog.io/@leeinae/Spring-Mybatis-JPA-Hibernate-%EB%B9%84%EA%B5%90
* https://suhwan.dev/2019/02/24/jpa-vs-hibernate-vs-spring-data-jpa/