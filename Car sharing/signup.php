<?php
include_once "header.php";
?>
<head>

<style>
    .forms {
        margin-top: 5% !important;
    }
</style>

</head>
<main>
<div class="flex nav">
    <h1 class="nadpis"> Sign up </h1>
</div>
</main>                                             <!--//? blue login and signup database-->
<section class="flex" >                          
        <form class="forms" action="includes/signup.inc.php" method="post" >
            <input type="text" class="forms" name="name" placeholder="Celé jméno" >    <!--//?  jméno -->
            <input type="text" class="forms" name="uid" placeholder="Uživatelské jméno" >    <!--//? uživatelské jméno -->
            <input class = "forms" name = "email"  placeholder ="Email" type="text"> <!--//?<!-- email -->
            <input class = "forms" name = "pwd"  placeholder ="Heslo" type="password">   <!--//?<!-- heslo -->
            <input class = "forms"  name = "pwdrepeat"  placeholder ="Heslo znovu" type="password">  <!--//?<!-- heslo znovu -->
            <div class="flex">
            <button type="submit" name="submit" class="btn btn-danger flex forms bottom">Sign up</button>    <!--//?<!-- tlačítko -->
            </div>
            
           

        </form>


</section>
 <?php include_once 'footer.php'; ?>

