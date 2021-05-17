## SpringSecurity 세션정책

---

```kotlin
http
.sessionManagement()
.sessionCreationPolicy(SessionCreationPolicy.정책) 
```

* ALWAYS
  * 스프링시큐리티가 항상 세션을 생성
* IF_REQUIRED
  * 스프링시큐리티가 필요시 생성(DEFAULT)
* NEVER
  * 스프링시큐리티가 생성하지 않지만, 기존에 존재하면 사용
* STATELESS
  * 스프링시큐리티가 생성하지도 않고 기존것도 사용하지 않음
  * JWT 같은 토큰 방식을 사용할때 설정 