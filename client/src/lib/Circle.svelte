<script lang="ts">
	import { onMount } from 'svelte';

	export let percentage: number = 91;
	export let label: string = 'Accuracy';

	const radius = 80;
	const circumference: number = 2 * Math.PI * radius;
	let offset: number = (circumference * (100 - percentage)) / 100;

	function updateOffset() {
		offset = (circumference * (100 - percentage)) / 100;
	}

	onMount(() => {
		updateOffset();
	});

	$: {
		updateOffset();
	}
</script>

<svg width="200" height="200">
	<circle
		class="circle-loading-bar-bg"
		cx="100"
		cy="100"
		r="80"
		stroke="#e6e6e6"
		stroke-width="15"
		fill="none"
	/>
	<circle
		class="circle-loading-bar-progress"
		cx="100"
		cy="100"
		r="80"
		stroke="#00cc99"
		stroke-width="15"
		fill="none"
		stroke-dasharray="{circumference}, {circumference}"
		stroke-dashoffset={offset}
	/>
	<text
		class="circle-loading-bar-label"
		x="50%"
		y="50%"
		dominant-baseline="middle"
		text-anchor="middle"
	>
		{label} {percentage}%
	</text>
</svg>

<style>
	.circle-loading-bar-bg {
		stroke-dasharray: 502.65;
	}

	.circle-loading-bar-progress {
		stroke-dasharray: 502.65;
		stroke-linecap: round;
		transition: stroke-dashoffset 0.5s ease;
	}

	.circle-loading-bar-label {
		font-size: 20px;
		font-weight: bold;
		fill: #444;
	}
</style>
