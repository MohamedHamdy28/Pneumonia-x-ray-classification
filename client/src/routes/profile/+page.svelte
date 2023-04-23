<script lang="ts">
	import { goto } from '$app/navigation';
    import { user } from '../../stores';
	import { onMount } from 'svelte';
    
    $: username = $user?.username; 
    $: message = `Welcome ${username}`;

    onMount(()=>{
        if( username === undefined){
            goto('/');
        }
    })

</script>

<div class="just-fixed">
    <h1>{message}</h1>
</div>


<style>
    .just-fixed {
		background-color: #f1f1f1;
		position: fixed;
		top: 80px;
		left: 300px;
    }
</style>