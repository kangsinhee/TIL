## [JPA] 영속성 컨텍스트와 플러시

#### Entity Manager, Entity Manager Factory

Jpa는 요청보다는 Entity Manager Factory에서 Entity Manager를 생성함

* 엔티티를 영구 저장하는 환경
  * persist()를 통해 db에 저장하는 것이 아닌 영속성 컨텍스트를 통해 엔티티를 영속화 함 DB 저장은 다음 단계

* 엔티티 매니저, 컨텍스트
  * 눈에 보이지 않음
  * 논리적인 개념
  * 엔티티 매니저를 통해 영속성 컨텍스트에 접근함

*스프링 프레임 워크와 같은 컨테이너 환경에서는 엔티티 메니저와 컨텍스트가 N:1*