<?php
// Allow from any origin
    if (isset($_SERVER['HTTP_ORIGIN'])) {
        // Decide if the origin in $_SERVER['HTTP_ORIGIN'] is one
        // you want to allow, and if so:
        header("Access-Control-Allow-Origin: {$_SERVER['HTTP_ORIGIN']}");
        header('Access-Control-Allow-Credentials: true');
        header('Access-Control-Max-Age: 86400');    // cache for 1 day
    }
    
    // Access-Control headers are received during OPTIONS requests
    if ($_SERVER['REQUEST_METHOD'] == 'OPTIONS') {
        
        if (isset($_SERVER['HTTP_ACCESS_CONTROL_REQUEST_METHOD']))
            // may also be using PUT, PATCH, HEAD etc
            header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
        
        if (isset($_SERVER['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']))
            header("Access-Control-Allow-Headers: {$_SERVER['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']}");
    
        exit(0);
    }

if(isset($_GET['add'])) {
    $x = $_GET['x'];
    $y = $_GET['y'];
    $color = $_GET['color'];
    $array = unserialize(file_get_contents('game_data.bin'));
    $array[$x][$y] = $color;
    file_put_contents('game_data.bin', serialize($array));
    echo "Done";
} 
if(isset($_GET['get'])) {
    $array = unserialize(file_get_contents('game_data.bin'));
    foreach($array as $sub) {
        foreach($sub as $item) {
            echo $item." ";
        }
        echo "/";
    }
}
if(isset($_GET['reset'])) {
    $line = ["white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white"];
    $array = [$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line,$line];
    foreach($array as $sub) {
        foreach($sub as $item) {
            echo $item." ";
        }
        echo "/";
    }
    file_put_contents('game_data.bin', serialize($array));
}
?>
