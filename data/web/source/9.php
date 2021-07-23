/*9. Write a PHP program named states.py that declares a variable states with value "Mississippi
Alabama Texas Massachusetts Kansas". write a PHP program that does the following:
a. Search for a word in variable states that ends in xas. Store this word in element 0 of a list
named statesList.
b. Search for a word in states that begins with k and ends in s. Perform a case-insensitive
comparison. [Note: Passing re.Ias a second parameter to method compile performs a
case-insensitive comparison.] Store this word in element1 of statesList.
c. Search for a word in states that begins with M and ends in s. Store this word in
element 2 of the list.
d. Search for a word in states that ends in a. Store this word in element 3 of the list. */


<html>
<body>
	<?php 
		$states = "Mississippi Alabama Texas Massachusetts Kansas";
		$b = explode(' ',$states);
		echo "<br>ORIGINAL ARRAY :<br>"; 
		foreach ( $b as $i => $value )
			echo "states[$i] = $value<br>";
		foreach ($b as $c) 
		{
			$n = strlen($c);
			if($c[$n-1]=='s' && $c[$n-2]=='a' && $c[$n-3]=='x')	$d[0] = $c;
			if($c[0]=='K' && $c[$n-1]=='s')	$d[1] = $c;
			if($c[0]=='M' && $c[$n-1]=='s')	$d[2] = $c;
			if($c[$n-1]=='a') $d[3] = $c;
		}
		echo "<br>RESULTANT ARRAY :<br>"; 
		for($i=0; $i < count($d); $i++)
			echo "statesList[$i] = $d[$i]<br>";
	?>
</body>
</html>