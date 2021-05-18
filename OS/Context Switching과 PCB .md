## Context Switching과 PCB

### Context Switching

> CPU가 이전의 프로세스 상태를 PCB에 보관하고, 또 다른 프로세스의 정보를 PCB에서 읽어 
> 레지스터에 적재하는 과정

보통 인터럽트가 발생하거나, 실행 중인 CPU 허가시간을 모두 소모하거나, 입출력을 위해 
대기해야 하는 경우에 Context Switching이 발생하게 됨

`프로세스가 Ready -> Running, Running -> Wait 등 상태변경 시 발생함`

#### Context Switching의 Overhead란?

프로세스 작업중 Overhead 즉 과부하를 감수해야 하는 상황이 있음
컨텍스트 스위칭 발생 시 CPU가 Overhead가 발생해 아무것도 안하는 상태가 옴

이때 CPU에 계속 프로세스를 수행시키도록 하기 위해 다른 프로세스를 실행 시키고 Context Switching함
**CPU가 낭비되지 않고, 빠르게 일처리를 하기 위함**

### Process Management

> CPU가 프로세스가 여러개일 때, CPU 스케줄링을 통해 관리하는 것을 뜻함

이때, CPU는 각 프로세스들이 누군지 알아야 관리가 가능함
프로세스의 데이터를 갖고 있는 것이 `Process Metadata` 임

* `Process Metadata`
  * ID
  * Status
  * Priority
  * CPU Register
  * Owner
  * CPU Usage

이 메타데이터는 프로세스가 생성되며 `PCB` 라는 곳에 저장됨

### PCB(Process Control Block)

> 프로세스 메타데이터들을 저장해 놓는 곳이며, 한 PCB에는 
> 한 프로세스의 정보가 저장됨

#### 존재 이유

CPU에서는 프로세스 상태에 따라 교체 작업이 이루어지게 되는데, 이때
**앞으로 다시 수행할 대기 중인 프로세스에 관한 저장 값을 `PCB`에 저장 해 두는 것**

#### 관리

`LinkedList` 방식으로 관리됨

`PCB` list Head에 `PCB`들이 생성될 때마다 붙게 됨 주소값으로 연결이 이루어져 있는 
연결리스트이기 때문에 삽입과 삭제가 용이함

**즉 프로세스가 생성되면 해당 `PCB`가 생성되고 프로세스 완료시 제거됨**

