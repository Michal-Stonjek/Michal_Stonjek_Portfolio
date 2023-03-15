<?php

if (isset($_POST["submit"])) {             //definice proměnných

    $name = $_POST["name"];   
    $email = $_POST["email"];
    $username = $_POST["uid"];
    $pwd = $_POST["pwd"];
    $pwdRepeat = $_POST["pwdrepeat"];

    require_once "dbh.inc.php";
    require_once "functions.inc.php";
   
    
                //error prázdné pole
    if (emptyInputSignup($name, $email, $username, $pwd, $pwdRepeat) !== false) {
        header("location: ../signup.php?error=prázdnéPole");
        exit();
    }               //error neplatné uživatelské jméno
    if (invalidUid($username) !== false) {
        header("location: ../signup.php?error=NeplatnéuživatelskéJméno");
        exit();
    }
                    //error neplatná email
    if (invalidEmail($email) !== false ) {
        header("location: ../signup.php?error=NeplatnýEmail");
        exit();
    }               // neplatné heslo
    if (pwdMatch($pwd, $pwdRepeat) !== false ) {
        header("location: ../signup.php?error=neplatnéHeslo");
        exit();
    }                       // uživatelské jménu už existuje
    if (uidExists($conn, $username, $email) !== false ) {
        header("location: ../signup.php?error=UživatelskéJménoUžExistuje");
        exit();
    }

    // vytvoření uživatele
    Send_Email($email, $username, $conn);
    createUser($conn, $name, $email, $username, $pwd);
    
 

}

else {
    header("location: ../signup.php");
    exit();
}