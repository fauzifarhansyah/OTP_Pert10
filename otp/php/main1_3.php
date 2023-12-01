<?php
function convertstringkeascii($string) {
    $hasilascii = [];
    $hasilbiner = [];
    for ($i = 0; $i < strlen($string); $i++) {
        $hasilascii[] = ord(string[$i]);
    }
    foreach ($hasilascii as $value) {
        $hasilbiner[] = decbin($value);
    }
    return $hasilbiner;
}
$inputString = "RUSDI";
$binaryResult = convertstringkeascii($inputString);
echo "String" . $inputrString . "\n";
echo "Biner: " . implode(" ", $binaryResult);
?>