<script lang="ts">
	import { base } from '$app/paths';
</script>

<div class="nav">
	<ul class="nav-list">
		<li>
			<a href="{base}/">Home</a>
		</li>
		<li>
			<a href="{base}/profile/dataset">Dataset</a>
		</li>
		<li>
			<a href="{base}/profile/model">Model Info</a>
		</li>
	</ul>
</div>

<style>
	.nav {
		height: 100%;
		background-color: #f1f1f1;
		position: fixed;
		top: 0;
		left: 0;
		display: flex;
		flex-direction: column;
		padding: 20px;
		width: 250px;
		text-align: center;
		justify-content: center;
	}

	.nav-list {
		list-style: none;
		margin: 0;
		padding: 0;
		display: flex;
		flex-direction: column;
		margin-top: 20px;
	}

	li {
		padding: 8px 16px;
		cursor: pointer;
		border: 1px solid #ddd;
		border-radius: 5px;
		margin-bottom: 10px;
		text-align: center;
	}

	a{
		display: inline-block;
		height: 100%;
		width: 100%;
	}
	li:hover {
		background-color: #ddd;
	}
	a:link {
		text-decoration: none;
	}
	div {
		margin: 50px;
		border: 2px solid #ccc;
		border-radius: 10px;
		padding: 20px;
		max-width: 800px;
		margin: 0 auto;
	}
	ul li {
		font-size: 18px;
		margin-top: 10px;
		margin-bottom: 10px;
	}
</style>
