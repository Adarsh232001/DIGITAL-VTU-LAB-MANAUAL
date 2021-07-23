/*7. Write a PHP program to display a digital clock which displays the current time of the
server.  */


NOTE: IGNORE "(DOUBLE QUOTE) IN THE BELOW PROGRAM AS THE SOFTWARE USES QTextBrowser(which is a html compiler)
"
<!DOCTYPE html>
<html lang="en">

<head>
	<title>Digital clock</title>
	<meta http-equiv="refresh" content="1" />
	<style>
		p {
			color: yellow;
			font-size: 90px;
			position: absolute;
			top: 40%;
			left: 50%;
			transform: translate(-50%, -50%);
		}

		body {
			background-color: maroon;
		}
	</style>
	<p>
		<?php echo date(" h: i : s A");?>
	</p>
</head>

</html>
"
NOTE: IGNORE "(DOUBLE QUOTE) IN THE BELOW PROGRAM AS THE SOFTWARE USES QTextBrowser(which is a html compiler)