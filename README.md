
### 게임 스크린샷
-----
<div>
<img width="400" alt="game_srceenshot2" src="https://github.com/UNGGU0704/CV_mediaPipe/assets/130115689/ecbaff5a-9a7f-4d84-8e1f-90b26ee9411f">
<img width="400" alt="game_srceenshot1" src="https://github.com/UNGGU0704/CV_mediaPipe/assets/130115689/1f6015eb-8254-4d66-a582-8a5ebbbcaef4">
</div>

----- 

  ## 개요

### 실습 내용설명

본 실습은 2023-1 전북대학교 컴퓨터비전(오일석 교수) 수업을 듣고 학습한 내용을 스스로 실습한 내용입니다.

모델을 통해 CV기술에 대한 실습을 진행하고 추후 해당 기술을 다른 프로젝트에서 연계할 능력을 갖추는것을 목표로 진행하였습니다.

본 프로그램은 ***Mediapipe***의 ***Blazehand***모델을 활용하여 컴퓨터와의 가위바위보 게임을 구현하였습니다. 

플레이어의 손 모양을 자동으로 검출하여 가위, 바위, 보 중 하나를 15초 동안 탐색하 여 마지막으로 탐지된 손 모양을 가지고 컴퓨터와 대결을 합니다. 

손 모양을 검출하는 데에는 웹캠을 통해 실시간으로 탐색합니다. 현재 어떤 손 모양을 탐색하였는지는 좌측 상단에 표시합 니다. 전체적인 GUI는 ***pyqt5***를 활용합니다.

참조 깃 링크 :https://github.com/google/mediapipe 

---

### 사용기술

***Python*** : 프로그래밍 언어로서의 주요 기반*Mediapipe*: 구글에서 개발한 프레임워크로, 손 모양 인식을 위해 ***Blazehand*** : 모델을 사용
***OpenCV*** : 영상 처리 및 디스플레이를 위한 라이브러리*PyQt5*: GUI 프레임워크로서 버튼과 화면 출력을 위해 사용

---

### BlazeHand

***BlazeHand***는 구글이 개발한 손모양을 위한 신경망 기반 모델입니다. ***Mediapipe*** 프레임 워크를
통해 사용할 수 있으며, 실시간으로 손 모양을 추적합니다.
저는 이 손 모양 인식을 통해 가위바위보 게임을 구현하기 위해 ***BlazeHand***의 출력인
`hand_landmarks` 객체를 활용해 주요 키포인트를 추출하기로 하였습니다.

---

## 코드 설명

### import 모듈

- ***sys**, **QApplication**, **QWidget**, **QVBoxLayout**, **QPushButton**:* PyQt5를 사용하기 위한 모듈입니다.
- ***cv2***: OpenCV를 사용하기 위한 모듈입니다.
- ***mediapipe as mp***: Mediapipe 라이브러리를 사용하기 위한 모듈입니다.
- ***ImageFont**, **ImageDraw**, **Image***: PIL 라이브러리를 사용하기 위한 모듈입니다.
- ***numpy as np**, **random**, **time***: 기타 필요한 모듈입니다.

### MyApp Class

- **MyApp** 클래스는 실제적으로 기능을 담당하는 부분입니다. `initUI` 메서드에서는 PyQt5의 위젯을 초기화하고 화면에 표시합니다.
- `run_code` 메서드에서는 가위바위보 게임을 실행합니다.
- 컴퓨터의 선택을 랜덤으로 생성합니다.
- 웹캠을 통해 영상을 입력받고, 손 모양을 인식합니다.
- 손모양에따라가위,바위,보중하나를결정하고,화면에텍스트로출력합니다.
- 타이머가 종료되면 게임 결과를 결정하고 화면에 출력합니다.
