import {user} from '../stores'

export async function login(username: string, password: string): Promise<User>{
    const response = await fetch('/api/login',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({username, password})
    });

    if (!response.ok){
        throw new Error('Login failed');
    }

    const loggedUser: User = await response.json(); 
    return loggedUser;
}


export async function getUser(): Promise<User | null>{
    try{
        const response = await fetch('/api/getuser');
        
        if (response.ok){
            const body = await response.json();
            if (body){
                return body as User;
            }else{
                throw new Error('Response body is empty.');
            }
        }else{
            throw new Error(`Status:${response.status}; Error: ${response.statusText} `);
        }
    }catch(error){
        console.error(`ERROR: ${error}`);
    }

    return null;
}


export function setUser(newUser: User | null){
    user.update(x=>newUser);
}


export async function clearUser(){
    await fetch('/api/logout');
    setUser(null);
}