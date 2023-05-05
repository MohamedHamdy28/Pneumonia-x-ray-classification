<script lang="ts">
	export let title: string;
	export let number: number;
</script>

<div class="box">
	<h3>{title}</h3>
	<p>{number}</p>
</div>

<style>
	.box {
		background-color: white;
		border: 2px solid #ddd;
		border-radius: 5px;
		box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
		padding: 40px;
		text-align: center;
        display: inline-block;
	}

	h3 {
		margin-top: 0;
		margin-bottom: 10px;
	}

	p {
		font-size: 2em;
		margin: 0;
	}

	.box:hover {
		border-color: #4caf50;
	}

	.box:focus {
		outline: none;
		border-color: #4caf50;
		box-shadow: 0 0 5px rgba(76, 175, 80, 0.5);
	}
</style>
