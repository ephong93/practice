import { Link } from 'react-router-dom';

function Enter() {
    return (
        <div>
            <Link to='/login'>로그인</Link>
            <Link to='/join'>가입</Link>
            <Link to='/main'>메인 화면</Link>
        </div>
    )
}

export default Enter;