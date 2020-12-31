## Spring boot 날짜 타입 Json

> Spring로 개발할 경우 Controller에서 request, response를 
> 받는 DTO에서 날짜/시간 타입을 직렬화 하는 방법을 담습니다. 

### Request Parameter

파라미터로 GET 요청을 받을때 날짜 직렬화가 필요한 경우
**@DateTimeFormat** 어노테이션을 사용함 

#### 1. @ModelAttribute

```kotlin
//Controller

@GetMapping("/get")
fun controller(getModel: GetModel) {
    println(getModel)
}

//DTO
class GetModel(
    var name: String,
    @DateTimeFormat(pattern = "yyyy-MM-dd'T'HH:mm:ss")
    var localDateTime: LocalDateTime
)
```

#### 2. @RequestParameter

```kotlin
//Controller

@GetMapping("/get")
fun controller(@DateTimeFormat(pattern = "yyyy-MM-dd'T'HH:mm:ss")
        @RequestParam("requestDateTime") 
        requestDateTime: LocalDateTime
       ) {
    println(requestDateTime)
}
```



### Request Body

Request Body에서 POST요청에서는 날짜 직렬화를 사용하기 위해
**@JsonFormat**과 **@DateTimeFormat** 모두 사용가능함

만약 두 어노테이션을 모두 적용하게 된다면 **@JsonFormat이 우선적으로 진행됨**
@JsonFormat이 틀리면 @DateTimeFormat이 맞더라도 직렬화 실패

```kotlin
//Controller

@PostMapping("/post")
fun controller(@RequestBody jsonModel: JsonModel) {
    println(jsonModel)
}

//DTO
class JsonModel(
    var name: String,
    @JsonFormat(shape = JsonFormat.Shape.STRING, 
                pattern = "yyyy-MM-dd'T'HH:mm:ss")
    @DateTimeFormat(pattern = "yyyy-MM-dd'T'HH:mm:ss")
    var localDateTime: LocalDateTime
)
```



### Response Body

앞서 진행했던 Request요청과는 다르게 
Response Body에서는 **@JsonFormat**만 직렬화가 가능함

```kotlin
//Controller

@GetMapping("/response")
fun controller(): ResponseModel {
    return ResponseModel(name="NAME",
                        localDateTime=LocalDateTime.now())
}

//DTO
class ResponseModel(
    var name: String,
    @JsonFormat(shape = JsonFormat.Shape.STRING, 
                pattern = "yyyy-MM-dd'T'HH:mm:ss")
    var localDateTime: LocalDateTime
)
```



### 정리

* Param GET 요청 시,  **@DateTimeFormat** 
* Request, Response Body, POST 요청 시, **@JsonFormat**
*  POST요청 시에도 **@DateTimeFormat**를 적용할 수 있지만 
  **@JsonFormat**이 우선순위로 작동함



### Reference

* https://jojoldu.tistory.com/361