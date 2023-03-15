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
    <link rel="shortcut icon" href="favicon.png" type="image/x-icon">
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
                

                
            
            
            ';
        }
        else {
            echo "<a   class='secondary-link btn btn-primary' href='signup.php'>Sign up</a>";
            echo '<a   class="secondary-link btn btn-primary" href="login.php">Log in</a>
            
                    ';
            
        }

        

        

                ?>
          </ul>
        </nav>

                                                    
         



    </header>

    <main >
        <h1 class="flex nadpis ">Kontakt</h1>
<div class="flex paragraf">

<div class="card text-bg-primary mb-3 " style="max-width: 18rem;">
  <div class="card-header">Header</div>
  <div class="card-body">
    <p class="card-text">Integer vulputate sem a nibh rutrum consequat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos hymenaeos. Curabitur bibendum justo non orci. Nulla non arcu lacinia neque faucibus fringilla. Maecenas ipsum velit, consectetuer eu lobortis ut, dictum at dui.
         Aliquam ante. Morbi leo mi, nonummy eget tristique non, rhoncus non leo. Duis viverra diam non justo.</p>
  </div>
</div>

<div class="flex">
<div class="card text-bg-danger mb-3" style="max-width: 18rem;">
  <div class="card-header ">Header</div>
  <div class="card-body">
    <p class="card-text "> Integer vulputate sem a nibh rutrum consequat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos hymenaeos. Curabitur bibendum justo non orci. Nulla non arcu lacinia neque faucibus fringilla. Maecenas ipsum velit, consectetuer eu lobortis ut, dictum at dui.
         Aliquam ante. Morbi leo mi, nonummy eget tristique non, rhoncus non leo. Duis viverra diam non justo.</p>
  </div>
</div>


    </main>

    <?php include_once 'footer.php'; ?>