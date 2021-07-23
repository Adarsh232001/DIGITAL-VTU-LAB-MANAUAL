/* 6. Write a PHP program to keep track of the number of visitors visiting the web page and to display
this count of visitors, with proper headings.  */

<?php
	echo "<h1> REFRESH PAGE </h1>" ;
	$file = 'count.txt' ;
	$c = file_get_contents($file) ;
	file_put_contents($file, $c+1);
	echo "The number of users visited : ".$c ;
?>


//count.txt 
8