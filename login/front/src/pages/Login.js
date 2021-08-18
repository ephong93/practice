import { useState } from 'react';
import { Link } from 'react-router-dom';
import { useHistory } from "react-router";

function Login() {
    const [ username, setUsername ] = useState('');
    const [ password, setPassword ] = useState('');
    const [ loginFailed, setLoginFailed ] = useState(false);
    const history = useHistory();

    const login = async () => {
        let res = await fetch('http://localhost:5000/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            credentials: 'include',
            body: JSON.stringify({
                username: username,
                password: password
            })
        });
        res = await res.json();

        if (res.status === 'success') {
            history.push('/main');
        } else {
            setLoginFailed(true);
        }
    }


    return (
        <>
            <h1>Login</h1>
            <div>
                username: <input type='text' value={username} onChange={e => setUsername(e.target.value)}></input><br/>
                password: <input type='password' value={password} onChange={e => setPassword(e.target.value)}></input><br/>
                { loginFailed && <div>로그인 실패했습니다</div> }
                <button onClick={login}>submit</button>
            </div>
            <Link to='/join'>go to join</Link>
        </>
    )
}

export default Login;