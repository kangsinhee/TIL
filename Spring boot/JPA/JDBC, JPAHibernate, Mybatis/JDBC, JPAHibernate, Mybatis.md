## Jdbc, JPA/Hibernate, Mybatis

---

> 내가 뭘 쓰고 있었는지도 뭐가 다른건지도 모르겠어서 정리합니다.🤬🤬

### 영속성(Persistence)

* 데이터를 생성한 프로그햄이 종료되더라도 사라지지 않는 데이터의 특성을 말함

* 영속성을 갖지 않는 데이터는 단지 메모리에서만 존재하므로 프로그램이 종료되면 모두 사라짐

  -> 관계형 데이터 베이스, 파일 시스템을 이용해 영속성을 부여함




### JDBC

JDBC는 DB에 접근할 수 있도록 Java에서 기본적으로 지원해 주는 API임

* 모든 Java의 Data Access 기술의 기본
* Persistence Framework는 내부적으로 JDBC를 사용함

#### 장점

* 각 데이터베이스 업체에선 자신들의 데이터베이스에 맞는 드라이버를 제공함 JDBC드라이버를 사용하면 JDBC를 지원하는 모든 데이터베이스를 사용할 수 있음 

* 모든 데이터베이스를 사용하더라도 JDBC 드라이버만 제공된다면 코드를 수정할 필요가 없음

#### 단점

* 안정적이고 유연한 기술이지만, 로우 레벨 기술로 인식됨

* 간단한 SQL을 사용하더라도 중복된 코드가 반복적으로 사용됨

  

### JPA(Java Rersistent API)

JPA는 Java Rersistent API의 약자로 자바 어플리케이션에서ORM을 통해 RDB를 사용하는 방식( 기술 명세 )을 정의한 **인터페이스**임 
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

### Mybatis

Java는 DB 접근을 위해 JDBC라는 라이브러리를 제공함
Mybatis라는 모듈을 통해 이 JDBC를 사용하기 쉽게 만들어 줌    

#### 장점

* 학습이 쉬움
* 소스코드와 쿼리를 분리할 수 있음

#### 단점

* 반복적인 작업이 반복됨

![overall_design](.\overall_design.png)

### Reference

* https://velog.io/@leeinae/Spring-Mybatis-JPA-Hibernate-%EB%B9%84%EA%B5%90
* https://suhwan.dev/2019/02/24/jpa-vs-hibernate-vs-spring-data-jpa/
* https://gmlwjd9405.github.io/2018/12/25/difference-jdbc-jpa-mybatis.html