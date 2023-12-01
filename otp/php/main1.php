<?php
$string = "RUSDI";

$asciiValues = [];
for ($i = 0; $i < strlen($string); $i++) {
    $asciiValues[] = ord($string[$i]);
}

foreach ($asciiValues as $value) {
    echo $value . " ";
}
?>