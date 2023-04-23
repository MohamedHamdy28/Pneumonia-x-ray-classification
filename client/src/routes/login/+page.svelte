<script lang="ts">
    import {login, setUser} from '../auth'
	import { goto } from '$app/navigation';

    let username: string = '';
    let password: string = '';
    let error: string = '';

    const handleSubmit = async (event: Event) =>{
        event.preventDefault();

        try{
            setUser(await login(username, password));
            goto('/profile');
        }catch(e){
            error = 'Invalid username or password';
            console.log(error)
        }
    };

</script>


<h1>Login</h1>

{#if error !== ''}
    <p style="color:red">{error}</p>
{/if}

<form on:submit={handleSubmit}>
    <label for="username">Username:</label>
    <input type="text" id = "username" bind:value={username}/>

    <label for="password">Password:</label>
    <input type="password" id="password" bind:value={password}/>

    <button type="submit">Log In</button>
</form>
