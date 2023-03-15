
<?php 
    include_once "nav.php";
?>

<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/škola.css">
    <title>Car share</title>
</head>
<body>
    <div class="wrapper">
        <form id="form">
            <div class="inputBox">
                <label for="name">Jméno:</label>
                <br>
                <input type="text" id="name" placeholder="Zadej své jméno" required>
            </div>
            <div class="inputBox">
                <label for="msg">Zpráva:</label>
                <br>
                <textarea id="msg" placeholder="Nezapoměn, že zpráva musí obsahovat: místo, datum, domluvený čas a hlavně mobilní telefon!" required></textarea>
            </div>
            <button id="btn" class="btn">Poslat</button>
        </form>
        <hr>
        <div class="content" id="content">
            
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>

    <script>
        $(document).ready(function(){
            function loadData(){
                $.ajax({
                    url: 'select-data.php',
                    type: 'POST',
                    success: function(data){
                        $("#content").html(data);
                    }
                });
            }

            loadData();

            $("#btn").on("click", function(e){
                e.preventDefault();
                var name = $("#name").val();
                var msg = $("#msg").val();

                $.ajax({
                    url: 'insert-data.php',
                    type: 'POST',
                    data: {name: name, msg: msg},
                    success: function(data){
                        if (data == 1) {
                            loadData();
                            alert('Comment Submitted Successfully.');
                            $("#form").trigger("reset");
                        }else {
                            alert("Comment Can't Submit.");
                        }
                    }
                });
            });
        });
    </script>
</body>
</html>