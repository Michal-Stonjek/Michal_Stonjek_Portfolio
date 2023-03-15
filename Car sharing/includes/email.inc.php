<?php










if (isset($_POST["send"])) {

$send_to = $_POST["sendto"];
$subject = $_POST["subject"];
$message = $_POST["message"];


require_once "dbh.inc.php";
require_once "functions.inc.php";
            // prázdné pole
if (emptyInputMessage($send_to, $subject, $message) !== false) {
    header("location: ../index.php?error=PrázdnéPoleVyplňVšechnaPole!");
    exit();
    
}
       

if (invalidSend_to($send_to) !== false) {
    header("location: ../index.php?error=NeexistujícíEmail");
    exit();
}

Send_Email($send_to, $subject, $message);







}

else {
header("location: ../index.php");
exit();
}

