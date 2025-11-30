<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form method="POST" action="#">
        <label for="first_number">input the first number<input type="number" id="first_number" name="num1"></label><br>
        <label for="second_number">input the second number<input type="number" id="second_number"
                name="num2"></label><br>
        <button> calculate</button>
    </form>
    <?php
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $num1 = (int) $_POST['num1'];
        $num2 = (int) $_POST['num2'];
        if ($num1 % 2 == 0 && $num2 % 2 == 0) {
            $sum = $num1 + $num2;
            echo "the sum of the number you've input is:" . $sum;
        } elseif ($num1 % 2 != 0 && $num2 % 2 != 0) {
            $product = $num1 * $num2;
            echo "the product of the number you've input is:" . $product;
        } else {
            echo "One number is even and the other is odd. Please try again.";
        }
    }
    ?>
</body>

</html>