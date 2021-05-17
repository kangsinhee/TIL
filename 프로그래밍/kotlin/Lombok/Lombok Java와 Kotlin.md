## Why Lombok is not accessible in Kotlin

>  Lombok이 코틀린에서 사용할 수 없는 이유

#### 마 그래서 Lombok이 믄데 문디야

Lombok은 JAVA 라이브러리로 반복되는 `getter`, `setter`, `toString`등의 메서드 
작성 코드를 줄어주는 코드 다이어트 라이브러리이며, JAVA 프로젝트에서 흔히 사용됨

> 하지만 Lombok을 사용하는 프로젝트에서 Kotlin을 적용했을 때 컴파일 오류가 발생함



#### 오류 발생 원인

![빌드과정](C:\Users\kangsinhee\Desktop\programming\Study_Backend\프로그래밍\kotlin\lombok\빌드과정.png)

1. kotlin 컴파일러가 kotlin 코드가 참조하는 Java 코드를 로딩해 
   kotlin코드와 함께 컴파일해 .class 파일을 생성함
2. Java 컴파일러가 Kotlin이 컴파일한 .class 파일의 경로를 추가해 Java 코드와 함께 
   컴파일해 .class 파일을 생성함

> Kotlin 컴파일러가 동작한 뒤, **Java 컴파일러가 동작할 때 Lombok이 코드를 생성**하기 때문에 
> Kotlin 코드는 Lombok이 생성한 코드를 사용할 수 없음



#### 해결 방법

1. 빌드 순서 조정
   * Java 코드에서 Kotlin 코드를 호출 할 수 없게 됨
2. Java와 kotlin을 별도 모듈로 분리
   * 의존성 방향에 따라 서로의 코드를 호출 불가능하게 됨
3. 빌드 전처리 고정에서 Delombok 실행
   * 빌드 전 Lombok이 제공하는 Delombok기능을 사용해 코드를 미리 생성하게 함
   * Delombok이 Gradle 플러그인을 공식으로 지원하지 않아 빌드 구성이 복잡해지는 단점이 있음
4. Lombok이 적용된 코드를 Kotlin으로 변환
   * Lombok이 적용된 Java 클래스는 대부분 JPA `Entity`, `DTO` 등 **데이터를 담는 용도**의 클래스
   * Data class로 변환하면 Lombok에서 제공하는 메서드를 별도 구현없이 사용할 수 있음
   * 프로젝트의 규모가 클 때에는 일괄 변환이 안정성 측면에서 부담이 될 수 있음
5. 프로젝트에서 Lombok 제거

### Reference

* 네이버 D2 개발팀 블로그
  * https://d2.naver.com/helloworld/6685007

