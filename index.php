<!DOCTYPE html>
<html>
    <head>
        <title>Cours PHP & MySQL</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="cours.css">
    </head>
    
    <body>
        <h1>Titre principal</h1>

       <?php       
          // chemin d'acc\u00e8s \u00e0 votre fichier JSON
          $file = 'ethsolde.json'; 
          // mettre le contenu du fichier dans une variable
          $data = file_get_contents($file); 
          // d\u00e9coder le flux JSON
          $obj = json_decode($data); 
          // acc\u00e9der \u00e0 l'\u00e9l\u00e9ment appropri\u00e9
          echo $obj[0]->balance;
        ?>
        <progress id="barre" value="<?php echo $obj[0]->balance; ?>" max="10$

        <p>Un paragraphe</p>

    </body>
</html>
