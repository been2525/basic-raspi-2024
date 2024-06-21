# basic-raspi-2024
IoT 개발자과정 IoT오픈하드웨어 플랫폼활용

## 1일차(2024-06-20)
- 옴의 법칙 - 회로를 통과해 흐르는 전류는 회로의 양단에 가해진 전압에 비례한다는 규칙
    - 전류(I) - 전하의 흐름
    - 전압(V) - 일정한 전기장에서 단위 전하를 한 지점에서 다른 지점으로 이동하는데 필요한 일(에너지)로 정의된다.
    - 저항(R) - 전류의 흐름을 방해하는 역할
- 키르히호프의 법칙
    - 제1법칙(접합점법칙or전류법칙)
        - 회로내의 어느 점을 취해도 그곳에 흘러들어오거나 흘러나가는 전류를 음양의 부호를 붙여 구별하면, 들어오고 나가는 전류의 총계는 0이 된다.
        - 즉, 전류가 흐르는 길에서 들어오는 전류와 나가는 전류의 합이 같다.
    - 제2법칙(폐회로법칙, 고리법칙 또는 전압법칙)
        - 임의의 닫힌 회러에서 회로내의 모든 전위차의 합은 0이다.
        - 즉, 임의의 폐회로를 따라 한 바퀴 돌 때 그 회로의 기전력의 총합은 각 저항에 의한 전압 강하의 총합과 같다.
        - 회로의 도는 방향을 정하고 그 방향으로 돌아가는 기전력E와 전압강하 IR의 부호를 정한다. 전류와 저항과의 곱의 총계는 고 속에 포함된 기전력의 총계와 같다
- pinout
- 라즈베리파이에서 visuall studio 안쓰고 파일 실행할려면 파일명앞에 python 입력하면 됨
- GPIO 설정함수
    - GPIO.setmode(GPIO.BOARD) - wpi
    - GPIO.setmode(GPIO.BCM) - BCM
    - GPIO.setup(channel, GPIO.mode)
        - channel: 핀번호, mode:IN/OUT
    - GPIO.cleanup
- GPIO 출력함수
    - GPIO.output(channel, state)
        - channel: 핀번호, state: HIGH/LOW or 1/0 or True/False
- GPIO 입력함수
    - GPIO.input(channel)
        - channel: 핀번호, 반환값: H/L or 1/0 or T/F
- 시간지연 함수
    - time.sleep(secs)
- 풀업과 풀다운
    - 풀업 - vcc에 저항연결
    - 풀다운 - gnd에 저항연결
- 풀다운 활용하여 스위치 제작
- 디지털 피아노 제작

## 2일차
- sudo git clone https://github.com/WiringPi/WiringPi -> cd WiringPi
- sudo ./build -> gpio -v
- gpio readall 좀더 자세하게 라즈베리파이 상황을 알 수 있음
- 적외선 센서 사용
- 초음파 센서 사용