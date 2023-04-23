import { writable } from "svelte/store";

export let user = writable<User | null>(null);