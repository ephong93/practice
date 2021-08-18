import { useState } from 'react';
import { useHistory } from 'react-router';
import { Link } from 'react-router-dom';

function Join() {
    const [ username, setUsername ] = useState('');
    const [ password, setPassword ] = useState('');
    const [ joinFailed , setJoinFailed ] = useState(false);

    const history = useHistory();
    
    const join = async () => {
        let res = await fetch('http://localhost:5000/api/join', {
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
            history.push('/login');
        } else {
            setJoinFailed(true);
        }
    }

    return (
        <>
            <h1>Join</h1>
            <div>
                username: <input type='text' value={username} onChange={e => setUsername(e.target.value)}></input><br/>
                password: <input type='password' value={password} onChange={e => setPassword(e.target.value)}></input><br/>
                { joinFailed && <div> 가입 실패 </div> }
                <button onClick={join}>submit</button>
            </div>
            <Link to='/login'>go to login</Link>
        </>
    )
}

export default Join;