<?php
include_once 'header.php';
?>
<head>

<style>
    .forms {
        margin-top: 5% !important;
    }
</style>

</head>
<main>
<div class="flex">
    <h3 class="nadpis">Log in</h3>
</div>

<!---  //?    Login formulář      -->

<section class="flex" >
<form  class="forms " action="includes/login.inc.php" method='post'>
<input class="forms " type="text" name="uid" placeholder="Uživatelské jméno nebo Email">
<input class="forms " type="password" name="pwd" placeholder="Heslo">
<div class="flex">
<button type="submit" name="submit" class="btn btn-danger forms bottom flex">Log in</button>
</div>

</form>



</section>



</main>
 <?php include_once 'footer.php'; ?>