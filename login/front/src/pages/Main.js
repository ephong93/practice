import { useState } from 'react';
import { useHistory } from 'react-router-dom';


function Main() {
    const [ loggedIn, setLoggedIn ] = useState(false);
    const history = useHistory();

    let res = fetch('http://localhost:5000/api/authenticate',
        {
            method: 'GET',
            credentials: 'include'
        }
    ).then(res => res.json())
    .then(res => {
        if (res.status === 'success') 
            setLoggedIn(true);
        else
            history.push('/login');
    })

    return (
        <div>
            { loggedIn && <div>로그인 성공~!</div> }
        </div>
    )
}

export default Main;