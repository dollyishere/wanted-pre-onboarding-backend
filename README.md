# 0. 노션 Django 공부 & 기록
[노션 공부 & 기록](https://polyesterda.notion.site/mission-2232a7b3a6a044c4a90654555af0f8ac?pvs=4)

# 1. 프로젝트 목표
기업 채용을 위한 웹 서비스(api) 개발

# 2. 개발 환경
  ### (1) 사용 기술
  Python & Django (DRF) & PostgreSQL 사용

  ### (2) 개발 환경 및 사용한 개발 도구
  * Main (필수 개발 환경 관련)
    * Python 3.12.*
    * Django 5.0.*
    * Django Rest Framwork 3.15.*
    * 나머지는 `requirements.txt` 참조
  * 사용 개발 도구
    * Visual Studio Code
    * OpenApi(Swagger, drf-yasg)
    * Talend API Tester(검증용)
    * ERD_CLOUD
      * DB 설계용
    * pgAdmin4
      * PostgreSQL용
  ### (3) 환경 세팅하는 방법
  ```
    -- C로 이동
    cd \

    -- 루트 디렉터리 생성
    mkdir venvs

    -- 루트 디렉터리로 이동
    cd venvs

    -- 가상환경 생성(가상환경 명 wanted)
    python -m venv wanted

    -- 가상환경 실행 가능 폴더로 이동
    cd C:\venvs\wanted\Scripts

    -- 가상환경 활성화
    activate

    -- 가상환경에 기존 requirements.txt 내역 설치
    pip install -r requirements.txt

    -- django 프로젝트 실행
    python manage.py runserver

    -- 초기 로컬 호스트 주소
    http://127.0.0.1:8000/

    -- swagger 접속 주소
    http://127.0.0.1:8000/swagger/

    -- 가상환경 비활성화
    deactivate
```
### (4) env 파일 설정
* recruit_pjt > config 내에 `.env` 파일 생성해서 내부에 이하 내용 세팅할 것 (PostgreSQL DB 기준이어야 함)
```
SECRET_KEY=(django secret key)
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```
# 3. 데이터베이스 모델링(ERD)
[ERD_CLOUD LINK](https://www.erdcloud.com/d/FNPTxk8JjKRk7Razf)

![image](https://github.com/user-attachments/assets/a24bdd3a-3ba7-4b60-b524-8169af8c45a7)


# 4. 각 api 설계
* 요구된 사항만 정리 (이외는 생략)
* 모든 api url은 `/api` 를 이미 포함하고 있음(`Base URL: 127.0.0.1:8000/api`)
### (1) Recruitment(채용공고) API
| Method | URL | Parameters | Description |
|---------|---------|---------|---------|
| `GET` | `/recruitments/?search=(query string 생략 가능)` | X | 채용공고 목록 확인(검색 가능) |
| `POST` | `/recruitments/` | X | 채용공고 신규 등록 |
| `GET` | `/recruitments/{recruitment_id}` | (int) recruitment_id(pk) | 채용공고 상세 정보 확인 |
| `PUT` | `/recruitments/{recruitment_id}` | (int) recruitment_id(pk) | 채용공고 수정 |
| `DELETE` | `/recruitments/{recruitment_id}` | (int) recruitment_id(pk) | 채용 공고 삭제 |

### (2) Resume(지원) API
| Method | URL | Parameters | Description |
|---------|---------|---------|---------|
| `GET` | `/resume/` | X | 지원 목록 확인 |
| `POST` | `/resume/` | X | 지원 신규 등록 |

# 5. 요구사항 확인
### (1) 채용공고 등록
* 채용공고 등록
![wanted_r1](https://github.com/user-attachments/assets/0d4adb4d-bfa8-4216-a369-aafe343afe5b)
* 결과
![wanted_r2](https://github.com/user-attachments/assets/ce0a5e2d-23aa-4ad5-a909-67f6a17ff3ab)

### (2) 채용공고 수정
* 채용공고 수정
![wanted_r3](https://github.com/user-attachments/assets/9d36d93f-7efe-4066-bbf7-182de7f6101b)
* 결과
![wanted_r4](https://github.com/user-attachments/assets/3aa6ca27-0c88-401c-8a22-69af43348ab4)

### (3) 채용공고 삭제
* 채용공고 삭제
![wanted_r5](https://github.com/user-attachments/assets/2d4e9ae4-c4f6-4f87-bb7e-0278d5ecd06f)
* 결과
![wanted_r6](https://github.com/user-attachments/assets/b4fbd570-409c-43e3-b062-244d93c86623)

### (4-1) 채용공고 목록 조회
* 채용공고 목록 조회 결과
![wanted_r7](https://github.com/user-attachments/assets/8a5f98dc-bd53-4d57-a461-bd02191bfeaa)

### (4-2) 채용공고 검색 기능
* 채용공고 검색("원티드" 검색)
![wanted_r8](https://github.com/user-attachments/assets/e81dcd52-c46a-4158-9526-8af863b9f3b8)
![wanted_r9](https://github.com/user-attachments/assets/7a068ee5-2dda-4d7e-b7dd-3cab00c9a584)

* 채용공고 검색(검색어 배정 x)
![wanted_r10](https://github.com/user-attachments/assets/c69ea5c8-b1c1-4db9-bcb9-28fefb5c785a)
![wanted_r11](https://github.com/user-attachments/assets/87d6ec34-46b8-4654-8f27-3c261835d6f6)

### (5) 채용공고 상세 페이지 가져오기
* 채용공고 상세 조회
![wanted_r12](https://github.com/user-attachments/assets/30ba66b8-4760-4e0a-92ab-46e55b6962d5)
* 결과
![wanted_r13](https://github.com/user-attachments/assets/d8c76ea4-8e5f-4be2-98b4-41a7e619fdb7)

### (6) 채용공고에 지원 
* 채용공고에 지원
![wanted_r14](https://github.com/user-attachments/assets/86ae8d08-e9ff-4015-9393-49ef04d561b8)
* 결과
![wanted_r15](https://github.com/user-attachments/assets/1f16c367-a5ec-4b75-aa6d-63c42438cc56)

# 99. Commit Convention
- **커밋 메세지 기본 구조**
    
    ```bash
    commit -m "[type] Subject"  (Type : 앞뒤로 한칸 씩 띄우기)
    commit -m "[feat] 로그인 API 구현"
    ```
    
    - **Type**
        - feat : 새로운 기능과 관련된 것을 의미한다.
        - fix : 오류와 같은 것을 수정했을 때 사용한다.
        - docs : 문서와 관련하여 수정한 부분이 있을 때 사용한다.
        - style : 코드의 변화와 관련없는 포맷이나 세미콜론을 놓친 것과 같은 부분들을 의미한다.
        - refactor : 코드의 리팩토링을 의미한다.
        - test : test를 추가하거나 수정했을 때를 의미한다.
        - chore : build와 관련된 부분, 패키지 매니저 설정 등 여러가지 production code와 무관한 부분들을 의미한다. 말 그대로 자질구레한 일들이다.
        - remove : 파일 삭제했을 때를 의미한다.
        - rename : 폴더 또는 파일의 이름 수정 및 이동.(chore로 해도 될듯?)

- **Subject**
    - 한글버전으로 하기
    - ex )   한글버전 >>>> [feat] loginAPI 구현
        
