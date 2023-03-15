<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car sharing</title>
    <link rel="stylesheet" href="styles1.css" type="text/css">
    <link rel="stylesheet" href="basic.css" type="text/css">
    <link rel="stylesheet" type="text/css" href="nav.css">
    <link rel="stylesheet" href="basic-setup.css" type="text/css">
    <link rel="shortcut icon" href="favicon.png" type="image/x-icon">
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<style>
        .odstavec{
            margin-top: 2rem;
            margin-bottom: 2rem;
            font-size: 25px;
            color: var(--secondary-color);
        }
        .verifi {
            margin-left: 1.5rem;
        }
</style>


</head>
<body>
        <h1 class="flex nadpis">Zadejte heslo z emailu</h1>
        <p class="flex odstavec">Na email jsme Vám odeslali ověřovací kód</p>
    <div class="flex">
    <form class="forms" action="includes/verifi.inc.php" method="post" class = "forms">
            <input type="number" name="code-user" class="flex forms" >
            <button type="submit" name="submit" class="btn btn-danger forms bottom flex verifi">Verifi</button>

        </form>
    </div>
        <
         <?php include_once 'footer.php'; ?>
</body>
</html>

