# URL, URI 정리



> 여기서는 URI와 URL만 다룬다.

## URL(Uniform Resource Locator)

* 자원

* 웹 상에 서비스를 제공하는 각 서버들에 있는 파일의 위치를 표시하기 위함

  * http://www.test.com/one/test.pdf test.com에서 one 폴더의 test.pdf를 요청

* 웹사이트 주소가 요청하는 파일이라기 보다는, 구분자로 보는것

  

## URI(Uniform Resource Identifier)

* 통합 자원 식별자
* 인터넷에 있는 자원을 나타내는 유일한 주소
* URI의 존재는 인터넷에서 요구되는 기본 조건이므로 인터넷 프로토콜이 항상 붙어다님
  * https://www.test.com (http프로토콜임을 명시함)
* URI의 하위개념에 URL, URN이 포함됨

* URI의 보편적인 혀태가 URL인데, URI의 부분집합으로 볼수 있음
* http://www.test.com/one/test.pdf까지는 URL(주소의 위치)
  * http://www.test.com/one/test.pdf?docid=12 이렇게까지 URI
    * docid=12라는 값에 따라 결과가 달라지게 됨 -> 식별자 역할을 하고 있음
    * 같은 URL을 가졌지만 URI는 다름

## 정리 

* URI에는 URL, URN이 포함되있음. URL은 URI이지만 URI는 URL은 아님
* URL은 인터넷 상의 자원 위치를 나타냄
* URI는 인터넷 상의 자원을 식별하기 위한 문자열의 구성

