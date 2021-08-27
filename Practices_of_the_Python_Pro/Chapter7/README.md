# 확장성과 유연성
### 확장 가능한 코드란?
- 새로운 동작을 추가해도 기존 동작에 거의 영향을 미치지 않는 코드
- ex) 크롬의 확장 프로그램

### 새로운 동작 추가하기
- 산탄총 수술 (shotgun surgery): 새로운 기능을 추가하기 위해 여기저기 코드를 수정해야 하는 경우

### 느슨한 결합
- 확장성은 느슨하게 결합한 시스템에서 나온다.


## 경직에 대한 해결책
### 놓아주기: 제어 반전 (inversion of control)
```python
class Tire:
    def __repr__(self):
        return 'A rubber tire'

class Frame:
    def __repr__(self):
        return 'An aluminum frame'

class Bicycle:
    def __init__(self):
        self.front_tire = Tire()
        self.back_tire = Tire()
        self.frame = Frame()

    def print_specs(self):
        print(f'Frame: {self.frame}')
        print(f'Front tire: {self.front_tire}, back_tire: {self.back_tire}')

if __name__ == '__main__':
    bike = Bicycle()
    bike.print_specs()
```

- Bicycle은 Tire, Frame 등 필요한 다른 부품에 의존적이다. 만약 CarbonFiberFrame을 원한다면 기존 코드를 깨뜨리고 다시 만들어야 한다.
- 제어 반전은 클래스 내에서 종속적인 인스턴스를 생성하는 대신에 클래스에 대한 기존의 인스턴스를 전달하여 사용할 수 있다고 말한다.

```python
class Bicycle:
    def __init__(self, front_tire, back_tire, frame):
        self.front_tire = front_tire
        self.back_tire = back_tire
        self.frame = frame

    def print_specs(self):
        print(f'Frame: {self.frame}')
        print(f'Front tire: {self.front_tire}, back tire: {self.back_tire}')

if __name__ == '__main__':
    bike = Bicycle(Tire(), Tire(), Frame())
    bike.print_specs()
```

- 제어반전을 사용하면 테스트하기 쉬운 코드가 된다. (ex. 테스트할 때 MockTire 인스턴스를 전달)
- 테스트하기 힘든 코드 -> 이해하기 힘든 코드
- 테스트 하기 쉬운 코드 -> 이해하기 쉬운 코드

### 악마는 디테일에 있다: 인터페이스에 의존하기
- 상위 코드가 하위 종속성의 세부 사항에 강력하게 의존하는 경우, 인터페이스를 사용해서 결합을 느슨하게 해야 한다.
- 파이썬에 덕타이핑이 있어 엄격한 인터페이스가 필요하지는 않음. 어떤 인터페이스를 구성할지는 개발자에게 달렸다.
- 밀접하게 관련된 코드는 인터페이스에 의존할 필요가 없다.
- 다른 클래스나 모듈에 있는 코드는 이미 분리되었으므로 다른 클래스에 직접 접근하는 것보다 공유된 인터페이스를 사용하는 것이 좋다.

### 엔트로피와의 싸움: 견고성의 원칙
- 자신이 하는 일에는 보수적으로 하고, 다른 사람으로부터 받아들일 때는 너그럽게 하라.
- 입력을 유연하게 하고 출력은 제한된 범위에서 한다. 정보의 흐름을 제한하고 예상가능한 범위로 향하게 한다.