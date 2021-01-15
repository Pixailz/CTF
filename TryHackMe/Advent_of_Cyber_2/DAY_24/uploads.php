<!DOCTYPE html>
<html lang=en>
	<head>
		<title>Aperture Clear?</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="icon" type="image/png" href="favicon.png">
		<link rel="stylesheet" type="text/css" href="assets/css/CourierPrime.css">
		<link rel="stylesheet" type="text/css" href="assets/css/uploads.css">
		<script src="assets/js/filter.js"></script>
		<script src="assets/js/upload.js"></script>
	</head>
	<body>
		<input id="uploadInput" type=file accept=".png,.jpg,.jpeg">
		<div id="arrow">
			<table border=0 cellspacing=0 cellpadding=0>
				<tbody>
					<tr>
						<td id="leftMost"><img src="assets/imgs/shapes/left-most.png"></td>
						<td id="leftMostAngled"><img src="assets/imgs/shapes/left-most-angled.png"></td>
						<td id="middleBar">
							<img src="assets/imgs/shapes/middle-bar.png">
							<div class="resMsg" id="resMsg">&nbsp;</div>
						</td>
						<td id="rightAngled"><img src="assets/imgs/shapes/right-angled.png"></td>
						<td id="uploadBtn" class="uploadBtn"><img id="uploadImg" src="assets/imgs/upload-button.png"></td>
					</tr>
				</tbody>
			</table>
		</div>
		<!--Mobile-->
		<img class="uploadBtn" id="mobUploadBtn" src="assets/imgs/upload-button.png">
		<p class="resMsg" id="mobResMsg">&nbsp;</p>
	</body>
</html>
