# ☁️ [Schooloud](http://www.schooloud.cloud) (스쿨라우드) ☁️
학교 프로젝트 환경 제공용 오픈스택 기반 클라우드 인프라 제공 서비스 <br><br>


## :thought_balloon:프로젝트 개발배경
최근 클라우드 서비스 시장의 성장으로 학생들이 학교에서 프로젝트를 진행함에 있어 클라우드 인프라의 수요가 증가하고 있습니다. 학생들의 경제적인 부담을 덜어줄 수 있는 학교 클라우드 인프라 서비스를 기획하게 되었습니다. <br>

클라우드 인프라를 제공하기 위해서는 많은 공인 IP가 필요하다는 비용적 문제점이 있습니다. 학교에서 운용할 수 있는 공 인 IP의 개수는 제한되어 있을 때, schooloud는 이에 대한 해결책을 제시합니다. <br><br>
schooloud는 제한된 공인 IP 자원으로 클라우드 서비스를 제공하기 위해, IP 포트를 이용하여 Reverse Proxy 서버를 거쳐 OpenStack 내의 인스턴스에 접근하는 방법을 사용합니다. <br>
이 방식을 이용하면 학교는 적은 비용으로 학생들에게 클라우드 서비스를 제공할 수 있고, 학생들은 경제적인 부담없이 클라우드 리소스를 사용하여 프로젝트를 진행할 수 있을 것으로 기대됩니다.

<br>

## :pushpin:목차
- [가이드](#✔️가이드)
- [사용방법](#hammer사용-방법)
  - [학생](#학생)
  - [교수](#교수)
  - [관리자](#관리자)
- [시스템 아키텍쳐](#floppy_disk시스템-아키텍쳐)
<br><br>
## ✔️가이드
Schooloud 실행을 위한 모든 사항은 아래 문서를 참고해주세요.
- **License**: <a href="LICENSE">GPL v2.0</a>
- **Install**:
- **Execute**:
- **Contribute**:

<br><br>
## :hammer:사용 방법
schooloud 서비스 사용자는 크게 3가지 역할로 분류됩니다. 
### 학생
<br>

- **회원가입/로그인** <br>
학생은 회원가입을 통해 서비스를 이용할 수 있습니다. 회원가입 및 로그인은 [schooloud](http://www.schooloud.cloud) 홈페이지에서 가능합니다.
<br>

- **프로젝트 제안서** <br>
좌측 바의 write proposal 버튼을 통해 프로젝트 제안서를 작성할 수 있습니다.<br>
프로젝트 이름, 목적, 사용량(quota), 사용 기간을 입력하고 제안서를 제출합니다.<br>
![image](https://github.com/schooloud/schooloud_back-end/assets/86493874/453e7b2e-d7ac-4d12-89d1-120eecf4c160)
좌측 바의 Proposal 버튼을 눌렀을 때 Waiting List를 통해 아직 검토중인 제안서 목록을 확인할 수 있고, Processed List를 통해 검토된 제안서 목록을 확인할 수 있습니다.<br>
제안서가 검토되기 전에 삭제할 수 있습니다.
<br>

- **대시보드** <br>
교수 또는 관리자가 제안서를 승인하면 학생은 프로젝트를 이용할 수 있습니다.<br>
대시보드에서 생성된 프로젝트에 다른 학생(사용자)를 초대할 수 있습니다. <br>
대시보드에서 프로젝트의 사용량(Quota usage)을 확인할 수 있습니다. 용량이 부족한 경우에는 쿼터 변경 요청을 할 수 있습니다. <br>
쿼터 변경 요청 리스트 버튼을 통해 이전에 요청했던 쿼터 변경 요청 기록을 확인할 수 있습니다.
![image](https://github.com/schooloud/schooloud_back-end/assets/86493874/43e35a15-3ddc-4fa5-801e-c093d0bcac16)
<br>

- **인스턴스** <br>
좌측 바에서 인스턴스 버튼을 통해 인스턴스를 관리할 수 있습니다.<br>
인스턴스를 생성, 중지, 재시작, 삭제할 수 있습니다. <br>
![image](https://github.com/schooloud/schooloud_back-end/assets/86493874/47413590-5f63-4221-aed8-1c85cc09ad4c)
인스턴스를 클릭할 시 선택한 인스턴스의 정보를 확인할 수 있습니다. <br>
![image](https://github.com/schooloud/schooloud_back-end/assets/86493874/e4e71dc1-0775-4d03-a00f-c7fcc5c7624d)
네트워크 탭에서 선택한 인스턴스에 대해 도메인을 할당 및 제거할 수 있습니다.
![image](https://github.com/schooloud/schooloud_back-end/assets/86493874/60f2f18c-28d2-480c-9393-664b3d5ed152)
접속정보 탭에서 선택한 인스턴스의 접속 방법을 확인할 수 있습니다.
![image](https://github.com/schooloud/schooloud_back-end/assets/86493874/86d66680-a581-4fa2-8662-c9e8fa3d64f5)
**(인스턴스 생성 후 접속하는 데 몇 분 정도 소요시간이 있습니다.)**
![image](https://github.com/schooloud/schooloud_back-end/assets/86493874/ea928d28-af94-4d2e-9d6c-7ebfed6e0f26)
<br>
<br>

- **키페어** <br>
인스턴스 생성 시 필요한 키페어를 생성 및 삭제할 수 있습니다.
![image](https://github.com/schooloud/schooloud_back-end/assets/86493874/468e4263-3d7e-414f-a6d0-fb08341322ad)



### 교수
사전에 등록된 사용자만 교수 페이지를 이용할 수 있습니다.
- **프로젝트 제안서 승인/반려** <br>
학생이 제출한 제안서를 클릭하여 승인 또는 반려할 수 있습니다.
교수가 프로젝트 제안서를 승인하게 된 순간 부터, 학생은 프로젝트를 사용할 수 있습니다.
![image](https://github.com/schooloud/schooloud_back-end/assets/86493874/d3df3485-5390-4364-b789-dce34e25029a)


### 관리자
사전에 등록된 사용자만 관리자 페이지를 이용할 수 있습니다. <br>

- **대시보드** <br>
관리자는 대시보드에서 schooloud 서비스에서 사용 가능한 전체 용량과 사용량을 확인할 수 있습니다.<br>
또한, 프로젝트 제안서 요청과 쿼터 변경 요청 리스트를 볼 수 있습니다.
![image](https://github.com/schooloud/schooloud_back-end/assets/86493874/4de35ea2-5c83-47cb-9990-6fa56de327dc)
<br>
  
- **쿼터** <br>
좌측 바의 Quota 버튼을 통해 현재 대기 중인 쿼터 변경 요청과 처리된 쿼터 변경 요청 리스트를 확인할 수 있습니다.
<br>

- **제안서** <br>
좌측 바의 Proposal 버튼을 통해 현재 대기 중인 제안서 요청과 처리된 제안서 리스트를 확인할 수 있습니다.<br>
대기 중인 제안서를 눌러 승인 또는 반려할 수 있습니다.<br>
<br>

- **프로젝트** <br>
좌측 바의 Project 버튼을 통해 프로젝트 목록을 볼 수 있습니다.<br>
프로젝트를 선택하면 현재 프로젝트의 사용량, 생성 날짜, 멤버 목록 등을 확인할 수 있고 프로젝트를 삭제할 수 있습니다.<br>
![image](https://github.com/schooloud/schooloud_back-end/assets/86493874/9b4ed2aa-759d-43bb-906b-797e756debde)
<br>

- **프록시** <br>
좌측 바의 Proxy 버튼을 통해 SSH List에서 생성된 인스턴스 목록과 프록시 서버에 설정된 포트를 확인할 수 있습니다.<br>
또한, Domain List에서 현재 인스턴스에 할당된 도메인 현황을 볼 수 있습니다.<br>
![image](https://github.com/schooloud/schooloud_back-end/assets/86493874/06c8e58d-3188-4530-8fd2-e18072151c7e)
![image](https://github.com/schooloud/schooloud_back-end/assets/86493874/12471539-d251-4b49-b58a-9d6a10d61cb7)

 
- **사용자** <br>
좌측 바의 User 버튼을 통해 학생 목록과 교수 목록을 확인할 수 있습니다.<br>
<br>

## :floppy_disk:시스템 아키텍쳐
![image](https://github.com/schooloud/schooloud_back-end/assets/86493874/4d570787-d4f4-4d5a-969d-52793e475e4d)

![image](https://github.com/schooloud/schooloud_back-end/assets/86493874/4e9d9d07-2c07-41e4-8ee9-455c47988e42)

