# TDD Counter
참조: [React Testing Library로 TDD개발환경 구축하기](https://benjaminwoojang.medium.com/react-testing-library%EB%A1%9C-tdd%EA%B0%9C%EB%B0%9C%ED%99%98%EA%B2%BD-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0-26e55fe33e01)


1. create-react-app 으로 프로젝트를 생성하면 test에 필요한 library가 자동으로 설치된다.
```
npx create-react-app tdd-counter
```

2. setupTests.js에 테스팅 라이브러리를 import한다.
```js
// setupTests.js
import '@testing-library/jest-dom'
```

3. test 함수를 사용해 test description, function을 작성한다.
- render: component를 렌더링 (html로 변환) 하는듯?
- getByText: 해당 text를 포함하는 dom element를 가져옴.
- expect: 테스트할 동작
```js
test('render counter', () => {
    const { getByText } = render(<Counter />);
    const titleElement = getByText(/counter/i);
    expect(titleElement).toBeInTheDocument(); // counter라는 텍스트를 포함하는 element가 document에 존재하는지 확인
});
```

4. fireEvent 함수로 이벤트를 발생시킬 수 있다.
```js
const plusElement = getByText('+');
expect(plusElement).toBeInTheDocument();

fireEvent.click(plusElement); // plusElement에서 click 이벤트를 발생시킴
const countElement2 = getByText('1');
expect(countElement2).toBeInTheDocument();
```