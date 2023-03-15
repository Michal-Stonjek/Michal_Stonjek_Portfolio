<?php
    $servername = "localhost";
    $username = "root";
    $password = "";
    $database = "phplogin-system";

    $conn = mysqli_connect($servername, $username, $password, $database);

    if (!$conn) {
        echo "Connection Failed.";
    }
?>