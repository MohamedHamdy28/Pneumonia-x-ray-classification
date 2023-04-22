<script lang="ts">
	import { error } from '@sveltejs/kit';
	import { onMount } from 'svelte';
	import { element } from 'svelte/internal';

	let fileSelector: HTMLInputElement;
	let fileDragger: HTMLDivElement;
	let fileName: string;

	interface ResponseData{
		result?: string;
		error?: string;
	}

	function draggerHandler(event: DragEvent) {
		const files = event.dataTransfer?.files;
		if (files?.length){
			const file = files[0];
			uploadFileHandler(file);
		}

	}

	function selectorHandler(event: Event) {
		const inputElement = event.target as HTMLInputElement;
		const file = inputElement.files?.[0] as File;

		if (!file) return;

		uploadFileHandler(file);
	}

	async function uploadFileHandler(file: File) {
		const formData = new FormData();
		formData.append('file', file);
		
		const response = await fetch('/upload',{
			method: 'POST',
			body: formData
		});

		await handleResponse(response);
	}

	async function handleResponse(response: Response):Promise<string>{
		if (response.status == 200){
			const data: ResponseData = await response.json();
			if (data.result){
				alert(`Result: ${data.result}`)
				return data.result;
			}
			else{
				throw new Error(`ERROR: ${JSON.stringify(data)}`);
			}
		}else{
			const errorData: ResponseData = await response.json();
			const errorMessage: string = errorData.error || 'Unknown error occured';
			alert(errorMessage)
			throw new Error(errorMessage);
		}
	}
</script>

<div
	id="container"
	bind:this={fileDragger}
	on:drop|preventDefault={(e) => draggerHandler(e)}
	on:dragover|preventDefault={() => {}}
>
	<div id="titleInfo">
		<h1>Lung X-Ray</h1>
		<span>Determines the presence of lung inflammation by X-ray image</span>
	</div>
	<input
		type="file"
		id="fileSelector"
		accept="image/*"
		on:change|preventDefault={(e) => selectorHandler(e)}
		hidden
		bind:this={fileDragger}
	/>
	<label for="fileSelector">Select File</label>
	<span style="margin-top: -90px; text-align:center;">Or Drag and Drop it <br />{fileName}</span>
</div>

<style>
	#container {
		height: 100%;
		width: 100%;
		display: flex;
		flex-direction: column;
		justify-content: flex-start;
		gap: 96px;
		align-items: center;
		background-color: #f3f0ec;
		color: #22577a;
		font-size: 24px;
	}
	#titleInfo {
		display: flex;
		flex-direction: column;
		justify-content: flex-start;
		align-items: center;
	}
	label {
		height: 6rem;
		width: 22rem;
		border: none;
		border-radius: 10px;
		background-color: #57cc99;
		color: #f3f0ec;
		font-size: 36px;
		text-align: center;
		line-height: 6rem;
		transition: all 0.2s ease-in;
	}
	label:hover {
		background-color: #38a3a5;
	}
</style>
