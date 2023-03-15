<?php
session_start();
?>


<!DOCTYPE html>
<html lang="cs">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CarShare</title>
    <link rel="stylesheet" href="styles1.css" type="text/css">
    <link rel="stylesheet" href="basic.css" type="text/css">
    <link rel="stylesheet" href="basic-setup.css" type="text/css">
    <link rel="shortcut icon" href="favicon.svg" type="image/x-icon">
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

</head>
<body>
    <header>
        <div class="pozadí"></div>
        <nav class="nav">
            <ul class="">
                

                <a class="main-link btn" href="index.php">Domů</a>
                <a class="main-link btn" href="about-us.php">O nás</a>
                <a class="main-link btn" href="kontakt.php">Kontakt</a>

         
                <?php




        if (isset($_SESSION["useruid"])) {
            echo "<a  class='secondary-link btn btn-primary' href='includes/logout.inc.php'>Log out</a> ";
            echo '
                <h1 class="nadpis flex škola-nadpis">Zadejte svou školu</h1>

               <div class="dropdown dd">
  <button class="btn btn-primary dropdown-toggle butt" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Vyberte svou školu
  </button>
  <div class="dropdown-menu menu-drop" aria-labelledby="dropdownMenuButton">
    <a class="dropdown-item" href="školy/škola1.php">Škola1</a>
    <a class="dropdown-item" href="školy/škola2.php">Škola2</a>
    <a class="dropdown-item" href="školy/škola3.php">Škola3</a>
  </div>
</div>

                
            
            
            ';
        }
        else {
            echo "<a   class='secondary-link btn btn-primary' href='signup.php'>Sign up</a>";
            echo '<a   class="secondary-link btn btn-primary" href="login.php">Log in</a>
            <h1 class="flex nadpis">Vítejte na Car Share</h1>
            <h2 class="flex nadpis2">Pro další akci se přihlašte / zaregistrujte</h2>
                    ';
            
        }

        

        

                ?>
          </ul>
        </nav>

                                                    
         



    </header>

   
    
        
        












  
</body>


</html>