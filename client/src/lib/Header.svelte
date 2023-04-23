<script lang="ts">
    import { page } from "$app/stores";
    import { base } from '$app/paths';
	import { onDestroy, onMount } from "svelte";
	import { getUser, setUser} from "../routes/auth";
    import { user } from "../stores";
    $: routeId = $page.route.id;

    let username = '';

    const unsubscribe = user.subscribe(
        value => {
            if(!value){
                username = '';
            }else{
                username = value.username;
            }
        }
    );

    onMount(async ()=>{
        setUser(await getUser());
    })
    onDestroy(unsubscribe);
</script>

<div id="navbar">
    <div id="logo">X-SCAN</div>
    <div id="links-container">
        <a href="{base}/" class:active={routeId == "/"}>Lung X-Ray</a>
        <a href="{base}/soon" class:active={routeId == "/soon"}>Coming Soon</a>
    </div>
    {#if !username }
        <a href="{base}/login">
            <div id="login">
                Login
            </div>
        </a>
    {:else}
    <div id="links-container">
        <a href="{base}/profile">
            <div id="profile">
                Profile
            </div>
        </a>
        <a href="{base}/logout">
            <div id="logout">
                Logout
            </div>
        </a>
    </div>
    {/if}
    
</div>

<style>
    #navbar{
        min-height: 70px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap:64px;
        padding: 0 4rem;
        flex-shrink: 0;
        color: #22577A;
        background-color: #fff;
        z-index: 5;
        font-size: 24px;
        -webkit-box-shadow: 0px 7px 10px -1px rgba(34, 60, 80, 0.2);
        -moz-box-shadow: 0px 7px 10px -1px rgba(34, 60, 80, 0.2);
        box-shadow: 0px 7px 10px -1px rgba(34, 60, 80, 0.2);
    }

    #links-container{
        display: flex;
        flex: 1;
        font-size: 24px;
        font-weight: bold;
        justify-content: center;
        gap: 24px;
    }

    #logo{
        font-size: 32px;
        font-weight: bold;  
    }

    .active{
        color: #57cc99;
    }

    #login{
        background-color: #f3f0ec;
        height: 100%;
        width: 110px;
        line-height: 70px;
        text-align: center;
        font-weight: bold;
    }

    #login:hover{
        background-color: #c7f9cc;
    }
</style>