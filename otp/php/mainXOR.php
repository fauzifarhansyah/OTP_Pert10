<?php
function xorBiner($biner1, $biner2) {
    $desimal1 = bindec($biner1);
    $desimal2 = bindec($biner2);
    $hasilXOR = $desimal1 ^ $desimal2;
    return decbin($hasilXOR);
}
$biner1 = "1010011";
$biner2 = "1000011";

$hasil =xorBIner($biner1, $biner2);

echo "XOR dari $biner1 dan $biner2 adalah $hasil";
?>