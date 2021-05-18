## Java와 Spring Framework 내에서의 비동기 처리

### Java에서 비동기 처리

#### ExecutorService

Jdk 1.5 부터 제공하는 **비동기 작업**을 위한 **interface**.
일반적으로 ExecutorService는 작업 할당을 위한 스레드 풀과 API를 제공함

```java
//Spring boot framework with Java
@Slf4j	//Logging을 위한 Annotation
public class FutureEx {
    public static void main(String[] args) {
        ExecutorService es = Executors.newCachedThreadPool();

        es.execute(() -> {
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {}
            log.info("Async");
        });

        log.info("Exit");
    }
}
```

```java
// 결과
09:23:31.692 [main] INFO com.example.study.FutureEx - Exit
09:23:33.628 [pool-1-thread-1] INFO com.example.study.FutureEx - Async
```



#### Future

jdk 1.5 부터 제공하는 **비동기 작업의 결과**를 나타내는 **Interface**.
비동기적인 작업을 수행한다는 것은 현재 스레드가 아닌 다른 스레드에서 작업을 수행하는 것을 의미함
이때 같은 스레드 내에서 메서드 호출에서는 결과를 리턴 받지만,
비동기 작업 수행에서는 결과값을 전달 받을 수 있는 별도의 Interface가 필요 

비동기 작업에서 runnable대신 callable interface를 이용하면 결과 값을 return 받을 수 있음 
또한 예외가 발생했을때 해당 예외가 발생한 스레드가 아닌 밖으로 던질 수 있음

```java
@Slf4j
public class FutureEx {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        ExecutorService es = Executors.newCachedThreadPool();

        Future<String> f = es.submit(() -> {
            Thread.sleep(2000);
            log.info("Async");
            return "Hello";
        });

        log.info(f.get());
        log.info("Exit");
    }
}
```

```java
// 결과
20:43:11.704 [pool-1-thread-1] INFO com.example.study.FutureEx - Async
20:43:11.706 [main] INFO com.example.study.FutureEx - Hello
20:43:11.706 [main] INFO com.example.study.FutureEx - Exit
```

Future를 통해서 비동기 결과의 값을 가져올 때는 **get 메서드**를 사용함,
하지만 작업이 완료될 때까지 **해당 스레드가 blocking(중단한 상태 대기)** 됨

Future은 이외에도 해당 작업이 완료되었는지 확인하는 isDone 메소드도 제공함

```java
@Slf4j
public class FutureEx {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        ExecutorService es = Executors.newCachedThreadPool();

        Future<String> f = es.submit(() -> {
            Thread.sleep(2000);
            log.info("Async");
            return "Hello";
        });

        log.info(String.valueOf(f.isDone()));
        Thread.sleep(2000);
        log.info("Exit");
        log.info(String.valueOf(f.isDone()));
        log.info(f.get());
    }
}
```

```java
//결과
00:26:00.501 [main] INFO com.example.study.FutureEx - false
00:26:02.502 [pool-1-thread-1] INFO com.example.study.FutureEx - Async
00:26:02.509 [main] INFO com.example.study.FutureEx - Exit
00:26:02.509 [main] INFO com.example.study.FutureEx - true
00:26:02.509 [main] INFO com.example.study.FutureEx - Hello
```



#### FutureTask

FutureTask는 비동기 작업을 생성함 위의 Future은 작업 생성과 동시에 실행이 이루어 졌다면, 
FutureTask는 작업 생성과 실행이 분리되어 진행됨

```java
@Slf4j
public class FutureEx {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        ExecutorService es = Executors.newCachedThreadPool();

        FutureTask<String> f = new FutureTask<>(() -> {
            Thread.sleep(2000);
            log.info("Async");
            return "Hello";
        });

        es.execute(f);		//실행이 따로 이루어짐

        log.info(String.valueOf(f.isDone()));
        Thread.sleep(2000);
        log.info("Exit");
        log.info(String.valueOf(f.isDone()));
        log.info(f.get());
    }
}
```

```java
// 결과
00:28:39.459 [main] INFO com.example.study.FutureEx - false
00:28:41.461 [pool-1-thread-1] INFO com.example.study.FutureEx - Async
00:28:41.467 [main] INFO com.example.study.FutureEx - Exit
00:28:41.467 [main] INFO com.example.study.FutureEx - true
00:28:41.467 [main] INFO com.example.study.FutureEx - Hello
```

FutureTask에선 handler 혹은 callback을 통해 비동기 작업의 결과를 가져올수 있음
아래 코드는 callback을 이용해 결과를 가져오는 코드임

```java
@Slf4j
public class FutureEx {
    public static void main(String[] args) {
        ExecutorService es = Executors.newCachedThreadPool();

        FutureTask<String> f = new FutureTask<String>(() -> {
            Thread.sleep(2000);
            log.info("Async");
            return "Hello";
        }) {
            @Override
            protected void done() {
                super.done();
                try {
                    log.info(get());
                } catch (InterruptedException e) {
                    e.printStackTrace();
                } catch (ExecutionException e) {
                    e.printStackTrace();
                }
            }
        };

        es.execute(f);
        es.shutdown();
        
        log.info("EXIT");
    }
}
```

```java
// 결과
01:03:04.153 [main] INFO com.example.study.FutureEx - EXIT
01:03:06.153 [pool-1-thread-1] INFO com.example.study.FutureEx - Async
01:03:06.153 [pool-1-thread-1] INFO com.example.study.FutureEx - Hello
```



### Spring boot에서 비동기 처리

#### @Async

Spring MVC 3.2 부터 Servlet 3.0 기반의 비동기 요청 처리가 가능해짐
**@Async 어노테이션**을 추가해 해당 메소드를 비동기적으로 호출할 수 있음

```java
@SpringBootApplication
@EnableAsync
@Slf4j
public class StudyApplication {

    @Service
    public static class MyService {
        @Async
        public ListenableFuture<String> hello() throws InterruptedException {
            log.info("hello()");
            Thread.sleep(1000);
            return new AsyncResult<>("Hello");
        }
    }

    public static void main(String[] args) {
        // try with resource 블록을 이용해 빈이 다 준비된 후 종료되도록 설정
        try (ConfigurableApplicationContext c = SpringApplication.run(StudyApplication.class, args)) {
        }
    }

    @Autowired
    MyService myService;

    @Bean
    ApplicationRunner run() {
        return args -> {
            log.info("run()");
            ListenableFuture<String> f = myService.hello();
            f.addCallback(s -> log.info(s), e-> log.info(e.getMessage()));
            log.info("exit");

            Thread.sleep(2000);
        };
    }
}
```

```java
// 결과
2019-04-04 23:42:46.348  INFO 44559 --- [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2019-04-04 23:42:46.348  INFO 44559 --- [           main] o.s.web.context.ContextLoader            : Root WebApplicationContext: initialization completed in 959 ms
2019-04-04 23:42:46.557  INFO 44559 --- [           main] o.s.s.concurrent.ThreadPoolTaskExecutor  : Initializing ExecutorService 'applicationTaskExecutor'
2019-04-04 23:42:46.736  INFO 44559 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http) with context path ''
2019-04-04 23:42:46.740  INFO 44559 --- [           main] com.example.study.StudyApplication       : Started StudyApplication in 1.779 seconds (JVM running for 2.306)
2019-04-04 23:42:46.742  INFO 44559 --- [           main] com.example.study.StudyApplication       : run()
2019-04-04 23:42:46.748  INFO 44559 --- [           main] com.example.study.StudyApplication       : exit
2019-04-04 23:42:46.751  INFO 44559 --- [         task-1] com.example.study.StudyApplication       : hello()
2019-04-04 23:42:47.752  INFO 44559 --- [         task-1] com.example.study.StudyApplication       : Hello
2019-04-04 23:42:48.757  INFO 44559 --- [           main] o.s.s.concurrent.ThreadPoolTaskExecutor  : Shutting down ExecutorService 'applicationTaskExecutor'
```

**@Async 어노테이션**을 사용해 해당 메서드를 비동기적으로 호출할 경우 
ThreadPool을 선언하지 않는다면, 기본적으로 **SimpleAsyncTaskExecutor**를 사용하게 됨 
해당 TaskExecutor는 각 비동기 호출마다 계속 새로운 스레드를 만들어 사용하기 때문에 비효율적임.

*이 경우 **ThreadPoolTaskExecutor**를 직접 만들어 사용하는게 효율적*

**ThreadPoolTaskExecutor**는 CorePool, QueueCapacity, MaxPoolSize를 직접 설정할 수 있음

```java
@SpringBootApplication
@EnableAsync
@Slf4j
public class StudyApplication {

    @Service
    public static class MyService {
        /*
         기본적으로 SimpleAsyncTaskExecutor를 사용한다. 스레드를 계속 새로 만들어 사용하기 때문에 비효율적이다.
         */
        @Async
        // @Async("tp") ThreadPool이 여러개일 경우 직접 지정 가능하다.
        public ListenableFuture<String> hello() throws InterruptedException {
            log.info("hello()");
            Thread.sleep(1000);
            return new AsyncResult<>("Hello");
        }
    }

    @Bean
    ThreadPoolTaskExecutor tp() {
        ThreadPoolTaskExecutor te = new ThreadPoolTaskExecutor();
        // 1) 스레드 풀을 해당 개수까지 기본적으로 생성함. 처음 요청이 들어올 때 poll size만큼 생성한다.
        te.setCorePoolSize(10);
        // 2) 지금 당장은 Core 스레드를 모두 사용중일때, 큐에 만들어 대기시킨다.
        te.setQueueCapacity(50);
        // 3) 대기하는 작업이 큐에 꽉 찰 경우, 풀을 해당 개수까지 더 생성한다.
        te.setMaxPoolSize(100);
        te.setThreadNamePrefix("myThread");
        return te;
    }

    public static void main(String[] args) {
        // try with resource 블록을 이용해 빈이 다 준비된 후 종료되도록 설정
        try (ConfigurableApplicationContext c = SpringApplication.run(StudyApplication.class, args)) {
        }
    }

    @Autowired
    MyService myService;

    // 모든 빈이 다 준비된 후 실행됨 (현재는 일종의 컨트롤러라고 생각)
    @Bean
    ApplicationRunner run() {
        return args -> {
            log.info("run()");
            ListenableFuture<String> f = myService.hello();
            f.addCallback(s -> log.info(s), e-> log.info(e.getMessage()));
            log.info("exit");

            Thread.sleep(2000);
        };
    }
}
```

```java
// 결과
2019-04-05 00:03:11.304  INFO 47863 --- [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2019-04-05 00:03:11.304  INFO 47863 --- [           main] o.s.web.context.ContextLoader            : Root WebApplicationContext: initialization completed in 1061 ms
2019-04-05 00:03:11.367  INFO 47863 --- [           main] o.s.s.concurrent.ThreadPoolTaskExecutor  : Initializing ExecutorService 'tp'
2019-04-05 00:03:11.677  INFO 47863 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http) with context path ''
2019-04-05 00:03:11.680  INFO 47863 --- [           main] com.example.study.StudyApplication       : Started StudyApplication in 1.751 seconds (JVM running for 2.208)
2019-04-05 00:03:11.681  INFO 47863 --- [           main] com.example.study.StudyApplication       : run()
2019-04-05 00:03:11.686  INFO 47863 --- [           main] com.example.study.StudyApplication       : exit
2019-04-05 00:03:11.687  INFO 47863 --- [      myThread1] com.example.study.StudyApplication       : hello()
2019-04-05 00:03:12.691  INFO 47863 --- [      myThread1] com.example.study.StudyApplication       : Hello
```



#### Servlet Async

 Spring MVC 3.2부터 Servlet 3.0 기반 비동기 처리가 가능해진 후, 기존 Controller 메서드를 
Callable로 변경함으로써 비동기로 만들수 있었음

Controller 메소드를 비동기로 변경해도 해당 처리가 서블릿 스레드가 아닌 다른 스레드에서 발생한다는 점을
제외하면 기존 Controller 메서드의 동장 방식과는 큰 차이가 없음



### Reference

https://jongmin92.github.io/2019/03/31/Java/java-async-1/