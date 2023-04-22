<script>
	import CircleLoadingBar from '$lib/Circle.svelte';
	import Box from './Box.svelte';
</script>

<h1>Status about the model</h1>

<div class='boxes'>
	<Box title="Number of users" number={5631} />
	<div class='box'>
		<Box title="Pneumonia cases" number={3875} />
	</div>
	<div class='box'>
		<Box title="Normal cases" number={1341} />
	</div>
</div>

<div class='circles'>
	<div class='circle'>
		<CircleLoadingBar percentage={91} label="Accuracy" />
	</div>
	<div class='circle' style="margin-left: 300px;">
		<CircleLoadingBar percentage={80} label="Precision" />
	</div>
</div>

<style>
	h1 {
		text-align: center;
		padding-left: 50px;
		padding-bottom: 50px;
	}

	.boxes{
		display: flex;
		justify-content: center;
		margin-left: 275px;
	}

	.box{
		margin-left: 200px;
	}

	.circles{
		display: flex;
		justify-content: center;
		margin-top: 50px;
	}

	.circle{
		margin-left: 50px;
	}
</style>
