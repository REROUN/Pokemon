# 👾사천왕을 이겨라!!

### 📚Contents
1. 프로젝트 개요
2. 게임 소개
3. 기술 스택
4. 기능 설명
5. 게임 실행 방법
6. 문의 및 피드백

### 🌌프로젝트 개요
본 프로젝트는 SKN에서 진행하는 미니프로젝트로 UI는 pygame으로 구현하였으며 OpenAI를 활용하여 개발하였습니다.  
플레이어는 Speech to Text 기능을 활용하여 포켓몬에게는 직접 명령을 내리고 Text to Speech 기능을 통해 상황을 보고 받으며 사천왕을 이겨야합니다.

Speech to Text 기능이 포함되어 포켓몬에게는 직접 명령을 내릴 수도 있으며 Text to Speech 기능도 포함되어 매 상황을 소리로 전달받을 수 있습니다.  
종료 방법은 내가 가진 포켓몬의 체력이 전부 0이 되거나 사천왕이 지닌 포켓몬들의 체력이 0이 되면 종료됩니다.

### 🐉게임 소개
> 포켓몬 트레이너가 되어 사천왕을 이겨보자

본 게임은 시작시 자신의 MBTI를 말하면 자신의 MBTI와 어울리는 포켓몬이 주어지게 되며 포켓몬들과 사천왕을 이겨야하는 게임입니다.
Speech to Text 기능을 활용하여 포켓몬에게는 직접 명령을 내려 사천왕이 지닌 포켓몬들의 체력이 0이 되도록 싸워야 합니다.
![image](https://github.com/user-attachments/assets/e996d878-7b58-4f4d-a422-07f9a729ae1c)

### 🕹️기술 스택
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/openai-412991?style=for-the-badge&logo=openai&logoColor=white">
<img src="https://img.shields.io/badge/dall.e-3776AB?style=for-the-badge&logo=dall.e&logoColor=white">
<img src="https://img.shields.io/badge/TTS-3776AB?style=for-the-badge&logo=TTS&logoColor=white">

### 📑기능 설명
- STT를 통해 MBTI를 말하고 이 MBTI에 맞는 포켓몬 획득
- 음성 입력을 통해 포켓몬에게 공격명령을 내리고 회피, 방어 등을 지시 가능
- 체력 시스템이 존재하며 TTS를 통해 계속 상황을 브리핑 받을 수 있다.
- 각 캐릭터 및 포켓몬 이미지를 볼 수 있다.

### ⚔️게임 실행법
1️⃣ 필요한 패키지 설치
```
pip install -r requirements.txt
```
2️⃣ 환경 변수 설정 (.env 파일)
OpenAI API 키를 .env 파일에 추가하세요.
```
OPENAI_API_KEY=your_openai_api_key
```
3️⃣ 게임 실행
파이썬 파일을 실행하면 game 창이 뜨며 게임 실행
