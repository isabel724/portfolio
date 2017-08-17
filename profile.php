<?php
$output = array();
$output['right'] = array();
$output['main'] = array();

foreach ($profile as $type => $data) {
  if ($type == 'user_picture' 
   || $type == 'locations' 
   || $type == 'summary') {
    $output['right'][] = $data;
  } else {
    $output['main'][] = $data;
  }
}
?>

<?php // OUTPUT ----------------------------- ?>

<div class='profile'>
<table style='margin:0; padding:0; float:right; width:328px' width='328'>
  <tr>
    <td style='padding:0 0 0 25px'>
    <?php foreach($output['right'] as $data) { echo $data; } ?>
    </td>
  </tr>
  <tr>
    <td style='padding-left:30px'>
    </td>
  </tr>
</table>

<?php foreach($output['main'] as $data) { echo $data; } ?>
