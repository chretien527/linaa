<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form method="post" action="#">
        <label>the a input <input type="number" name="a"></label>
        <label>the b input <input type="number" name="b"></label>
        <label>the c input <input type="number" name="c"></label>
        <button type="submit"> calculate</button>
    </form>
    <?php
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $a = (float) $_POST['a'];
        $b = (float) $_POST['b'];
        $c = (float) $_POST['c'];
        $delta = $b² - 4 * $a * $c;

        echo "the delta of your equation is:" . $delta;
        if ($delta > 0) {
            $x1 = (-$b + sqrt($delta)) / (2 * $a);
            $x2 = (-$b - sqrt($delta)) / (2 * $b);
            echo " the value of first x is:" . $x1;
            echo "the value of the second x is:" . $x2;
        } elseif ($delta = 0) {
            $x1 = (-$b + sqrt($delta)) / (2 * $a);
            $x2 = (-$b - sqrt($delta)) / (2 * $b);
            echo " the value of first x is:" . $x1;
            echo " the value of the second x is:" . $x2;
        } else {
            echo "error";
        }
    }
    ?>
</body>

</html>