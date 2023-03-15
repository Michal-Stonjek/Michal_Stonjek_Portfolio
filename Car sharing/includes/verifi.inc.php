<?php
if (isset($_POST["submit"])) {             //definice proměnných
    
    $verifi = $_POST["code-user"]; 

    require_once "dbh.inc.php";
    require_once "functions.inc.php";

    if (EmptyCode($verifi) !== false) {
        header("location: ../verifi.php?wrong");
        exit();
    }
    
    if (VerifiCode($verifi) !== true) {
        echo ("koko");
        header("location: ../verifi.php?wrong");
        exit();
    } 
    else{
         header("location: ../index.php?succes");
        exit();
    }
     
        
             
}
else {
        echo("bad");
        exit();
    }