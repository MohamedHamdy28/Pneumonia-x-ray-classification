<script lang="ts">
	import { onMount } from 'svelte';
	import { element } from 'svelte/internal';

	let fileSelector: HTMLInputElement;
	let fileDragger: HTMLDivElement;
	let fileName: string;

	function draggerHandler(e: any) {
		let file = e.dataTransfer?.files[0] as File;
		uploadFileHandler(file);
	}

	function selectorHandler(e: any) {
		//To Do
		let file = e.target.files?.[0] as File;
		console.log(e);
		uploadFileHandler(file);
	}

	function uploadFileHandler(file: File) {
		console.log(file);
		fileName = file.name;
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
