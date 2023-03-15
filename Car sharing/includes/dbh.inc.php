<?php
// Nastavení databáze
$serverName = "localhost";
$dBUserName = "root";
$dBPassword = "";
$dBName = "phplogin-system";

$conn = mysqli_connect($serverName, $dBUserName, $dBPassword, $dBName);

if (!$conn) {
    die("Připojení selhalo:" . mysqli_connect_error());
}







