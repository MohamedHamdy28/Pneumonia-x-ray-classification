<div id="container">
	<div>
		<h1>Information about the Model</h1>
		<p>This model was trained to classify X-ray scans of the chest as pneumonia or normal.</p>

		<p>
			It was trained on a dataset from <a
				href="https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia">Kaggle</a
			> using a Google Colab notebook.
		</p>

		<h3>Information about the training process:</h3>

		<ul style="list-style-type: none; padding-left: 0;">
			<li>Training time: 30 mins</li>
			<li>Number of epochs: 163</li>
			<li>Batch size: 32</li>
			<li>Starting learning rate: 0.001</li>
			<li>Minimum learning rate: 0.000001</li>
		</ul>
	</div>
</div>

<style>
	#container {
		border: none;
		display: flex;
		justify-content: center;
		align-items: center;
		height: 100%;
		width: 100%;
	}

	div {
		margin: 50px;
		border: 2px solid #ccc;
		border-radius: 10px;
		padding: 20px;
		margin: 0 auto;
	}

	h1 {
		font-size: 36px;
		margin-bottom: 20px;
	}

	h3 {
		margin-top: 40px;
		margin-bottom: 20px;
	}

	p {
		font-size: 20px;
		margin-top: 20px;
		margin-bottom: 20px;
	}

	ul li {
		font-size: 18px;
		margin-top: 10px;
		margin-bottom: 10px;
	}
</style>
