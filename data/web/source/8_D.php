/*d. Addition of two matrices.*/

<html>
    <body>
        <?php
echo "<b>The First matrix is given below:-</b>"."<br>";
$a=array(array());// First two dimensional array declaration
$b=array(array());//Second two dimensional array declaration
$c=array(array());//Third two dimensional array declaration
$rows=4;
$cols=4;
$m=1;
$n=1;
for($i=0;$i<$rows;$i=$i+1)
{
    for($j=0;$j<$cols;$j=$j+1)
    {
        $a[$i][$j]=$m;
        echo $a[$i][$j]." ";
        $m=$m+1;
    }
    echo "<br>";
}
echo "<b>The second matrix is given below:-</b><br>";
for($i=0;$i<$rows;$i=$i+1)
{
    for($j=0;$j<$cols;$j=$j+1)
    {
        $b[$i][$j]=$n;
        echo $b[$i][$j]." ";
        $n=$n*1;
    }
    echo "<br>";
}
echo "<b>The Final matrix is given below:-</b>"."<br>";
for($i=0;$i<$rows;$i=$i+1)
{
    for($j=0;$j<$cols;$j=$j+1)
    {
        $c[$i][$j]=$a[$i][$j]+$b[$i][$j]; 
        echo $c[$i][$j]." ";
    }
    echo "<br>";
}
        ?>
    </body>
</html>