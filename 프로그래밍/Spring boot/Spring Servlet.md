### Spring Servlet

#### Servlet이란?

* 자바를 사용하여 웹 페이지를 동적으로 생성하는 서버 측 프로그램을 뜻함
  * 웹 서버 프로그램을 하기 위한 사양을 갖춘 자바 코드
* HttpServlet 클래스를 상속한 클래스
* Servlet은 Servlet Container에 의해 실행, 관리됨. 
  * HTTP Server + Server Container가 웹 서버가 필요한 대부분을 구현해 두었고,
    개발자는 Servlet을 만들어 HTTP 요청을 받아 처리하는 부분을 구현하는 것

#### Tomcat

* 웹 애플리케이션 서버 통칭 WAS의 하나로 Servlet Container, Servlet Engine이라고 표현할 수 있으며,
  자바 웹 프로그래머가 작성한 Servlet을 관리함
* Servlet을 관리한다는 것은 클라이언트가 어떤 요청을 했을때 어떤 Servlet을 실행할 것인지 제어하는 것

#### DispatcherServlet

* Servlet Container으로부터 들어오는 요청을 관제하는 컨트롤러
  Spring Mvc에서 요청을 받는 부분을 의미함

#### Servlet Filter

* Servlet 실행 전, 후에 어떤 작업을 하고자 할 때 Servlet Filter을 사용함
* Interceptor vs Filter
  * Interceptor는 Spring Container에 등록
  * Filter는 Servlet Container에 등록

##### GenericFilterBean

* 스프링에서 제공하는 기존의 Filter을 조금 더 확장한 추상클래스
* Spring의 설정 정보를 가져올 수 있게 확장됨

*Filter와 GenericFilter 빈은 매 서블릿 마다 호출이 되는 공통점이 있음*

##### OncePerRequestFilter

* 모든 서블릿에 일관된 요청을 처리하기 위해 만들어진 필터
* 사용자의 한번의 요청 당 한번 씩만 실행되는 필터를 만들 수 있음

#### Application Context

* Root Context이자 Spring에 의해 생성되는 Bean에 대한 Spring IoC Container
* BeanFactory를 상속받는 Context
* 여러 Servlet에서 공통으로 사용할 Bean을 등록하는 Context임
* @Transactional으로 트랜젝션을 이용해야 할 때 ApplicationContext에 있는 
  Service에서만 트랙젝션이 정상작동함

#### Servlet Context

* Servlet 단위로 생성되는 Context임
* Servlet Container에 DispatcherServlet과 같은 Servlet을 등록하면 
  해당 Servlet이 가지는 작은 컨테이너 같은것
* Spring  Container를 부모 Context로 사용함
* Application Context와 Servlet Context에 같은 id로 된 Bean이 있다면 
  Servlet Context에 있는 Bean을 우선 사용함
  * Bean을 찾는 순서가 Servlet에서 Servlet Context을 먼저 확인하고 Application Context를 확인하기 때문



