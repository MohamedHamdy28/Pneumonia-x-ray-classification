<script lang="ts">
	import { goto } from "$app/navigation";
	import { onMount } from "svelte";
	import { clearUser } from "../auth";
    
    onMount(()=>{
        clearUser();
        goto('/');
    })


</script>