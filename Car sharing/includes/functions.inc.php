<?php



use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;


require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/SMTP.php';


// funkce, která kontroluje, jestli není prázdné pole v signup fomuláři
function emptyInputSignup($name, $email, $username, $pwd, $pwdRepeat) {
    $result;
    if (empty($name) || empty($email) || empty($username) || empty($pwd) || empty ($pwdRepeat)) {
        $result = true;
    }
    else {
        $result = false;
    }
    return $result;

}
// funkce, která kontroluje, jestli nejsou v uživatelském jméně zakázané znaky
function invalidUid($username) {
    $result;
    if (!preg_match("/^[a-zA-Z0-9]*$/", $username)) {
        $result = true;
    }
    else {
        $result = false;
    }
    return $result;
} 
// funkce, která kontroluje, jestli je email v databázi
function invalidEmail($email) {
    $result;
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $result = true;
    }
    else {
        $result = false;
    }
    return $result;
}
// funkce, která kontroluje, jestli je pwd stejné jako pwdRepeat
function pwdMatch($pwd, $pwdRepeat) {
    $result;
    if ($pwd !== $pwdRepeat) {
        $result = true;
    }
    else {
        $result = false;
    }
    return $result;
}
// funkce, která kontroluje, jestli je email nebo uživatelské jméno zaregistrované v databázi
function uidExists($conn, $username, $email) {
    $sql = "SELECT * FROM users WHERE usersUid = ? OR usersEmail = ?;";
    $stmt = mysqli_stmt_init($conn);
    if (!mysqli_stmt_prepare($stmt, $sql)) {
        header("location: ../signup.php?error=uživateslkéJménoNeboEmailNenalezeno");
        exit();
    }
    mysqli_stmt_bind_param($stmt, "ss", $username, $email);
    mysqli_stmt_execute($stmt);

    $resultData = mysqli_stmt_get_result($stmt);
    if ($row = mysqli_fetch_assoc($resultData)) {
        return $row;
    }
    else {
        $result = false;
        return $result;
    }
    mysqli_stmt_close("stmt");
}

// funkce, která vytvoří profil uživatele
function createUser($conn, $name, $email, $username, $pwd) {
   
    $sql = "INSERT INTO users (usersName, usersEmail, usersUid, usersPwd) VALUES (?,?,?,?);";
    $stmt = mysqli_stmt_init($conn);
    if (!mysqli_stmt_prepare($stmt, $sql)) {
        header("location: ../signup.php?error=údajJeŠpatně");
        exit();
    }
    $hashedPwd = password_hash($pwd, PASSWORD_DEFAULT);


    mysqli_stmt_bind_param($stmt, "ssss", $name, $email, $username, $hashedPwd);
    mysqli_stmt_execute($stmt);
    mysqli_stmt_close("stmt");
    header("location: ../verifi.php?email_sent");
    exit();
}

// prázdné pole v login.php
function emptyInputLogin($username, $pwd) {
    $result;
    if (empty($username) || empty($pwd)) {
        $result = true;
    }
    else {
        $result = false;
    }
    return $result;
}
// funkce, která přihlásí uživatele
function loginUser($conn, $username, $pwd) {
    $uidExists = uidExists($conn, $username, $username);

    if ($uidExists === false) {
        header("location: ../login.php?error=špatnéPřihlašovacíÚdaje");
        exit();
    }

    $pwdHashed = $uidExists["usersPwd"];
    $checkPwd = password_verify($pwd, $pwdHashed);

    if ($checkPwd === false) {
        header("location: ../login.php?error=špatnépřihlašovacíÚdáje");
        exit();
    }
    else if ($checkPwd === true) {
        session_start();
        $_SESSION["userid"] = $uidExists["usersId"];
        $_SESSION["useruid"] = $uidExists["usersUid"];
        header("location: ../vyberskol.php");
        exit();   
    }
}





// fukce, která pošle ověřovací email na zadanou addresu 

function Send_Email($email, $username, $conn) {
    $mail = new PHPMailer(true);

try {
 
                  
    $mail->isSMTP();
    
    
    
    
   
    $mail->SMTPAuth = true;                                          
    $mail->Host       = 'smtp.gmail.com';                                                        
    $mail->Username   = 'tt549473@gmail.com';                    
    $mail->Password   = 'baydddwctscokoer';
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS;  
    //$mail->SMTPDebug = SMTP::DEBUG_SERVER;
    $mail->Port = 465;
   
    
       
    
  
    $mail->setFrom('tt549473@gmail.com');

    $mail->addAddress($email);             

    $code = random_int(100000, 999999);
    $mail->isHTML(true);                                 
    $mail->Subject = 'no reply';
    $mail->Body    = 'Here is the verification code '.$code.'.';
   

    $mail->send();
    
    echo "Email sent";
    

} catch (Exception $e) {
    echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
}
}

//! oveření prázdných polí
function EmptyCode($verifi) {
    $result;
    if (empty($verifi)) {
        $result = true;
    }
    else {
        $result = false;
    }
    return $result;
}

//! ověření linku z emailu

    function VerifiCode($verifi) {
    
    $result;
    if ($code == $verifi){ 
        $result = false;

       
    }
    else {
        $result = true;
        
    }
    return $result;
}
















?>