<?php
  $supported_langs = array('en', 'ru');
  $lang = 'en';


  // determine lang based on HTTP ACCEPT LANGUAGE
  if (!empty($_SERVER['HTTP_ACCEPT_LANGUAGE'])) {
    $substr = substr($_SERVER['HTTP_ACCEPT_LANGUAGE'], 0, 2);
    if (in_array($substr, $supported_langs)) {
      $lang = $substr;
    }
    if (in_array($substr, array("be", "kk", "uk"))) {
      $lang = "ru";
    }
  }
  

  // determine lang based on user preference
  if (!empty($_GET['lang']) && in_array($_GET['lang'], $supported_langs)) {
    $lang = $_GET['lang'];
  }


  $TXT['name'] = array(
    'en' => 'Roman Vorobyov',
    'ru' => 'Роман Воробьёв');
  $TXT['title'] = $TXT['name'];
  $TXT['tagline'] = array(
    'en' => 'Web Developer, MSc Student',
    'ru' => 'Веб-Разработчик, Магистрант');
  $TXT['email_title'] = array(
      'en' => 'Web Developer, MSc Student',
      'ru' => 'Веб-Разработчик, Магистрант');
  $TXT['meta_description'] = array(
    'en' => 'Personal Businesscard-Website of Roman Vorobyov',
    'ru' => 'Личный Сайт-Визитка Романа Воробьёва');
  $TXT['meta_keywords'] = array(
    'en' => 'Roman Alexeyevich Vorobyov',
    'ru' => 'Роман Алексеевич Воробьёв');
  $TXT['meta_author'] = $TXT['name'];
  $TXT['quote'] = array(
    'en' => 'Work for something because it is good, not just because it stands a chance to succeed',
    'ru' => 'Надо работать во благо, а не потому, что это может привести к успеху');
  $TXT['quote_author'] = array(
      'en' => 'Václav Havel',
      'ru' => 'Вацлав Гавел');
  $TXT['quote_author_link'] = array(
      'en' => 'http://en.wikipedia.org/wiki/V%C3%A1clav_Havel',
      'ru' => 'http://ru.wikipedia.org/wiki/%D0%93%D0%B0%D0%B2%D0%B5%D0%BB,_%D0%92%D0%B0%D1%86%D0%BB%D0%B0%D0%B2');
  
  
  
  if ($lang == 'en') {
    $css_active_en = " active";
  } elseif ($lang == 'ru') {
    $css_active_ru = " active";
  }
?>




<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="<?php echo $lang; ?>" lang="<?php echo $lang; ?>">
<head>
  <!-- Template design by <a href="http://andreasviklund.com/">Andreas Viklund</a> -->
  <meta name="google-site-verification" content="4me7F3vkawQDYk8A2_hdNZuXRDxgQeYJuX7nONjsQZ0" />
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <meta name="description" content="<?php echo $TXT['meta_description'][$lang]; ?>" />
  <meta name="keywords" content="<?php echo $TXT['meta_keywords'][$lang]; ?>" />
  <meta name="author" content="<?php echo $TXT['author'][$lang]; ?>" />
  <link rel="icon" href="img/favicon.ico" />
  <link rel="stylesheet" type="text/css" href="main.css" media="all" />
  <title><?php echo $TXT['title'][$lang]; ?></title>

  <script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-41765277-1']);
    _gaq.push(['_trackPageview']);
    (function() {
      var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
      ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
      var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
  </script>
</head>

<body>

<div id="wrap">
  <div id="logo"><img src="img/logo.jpg" /></div>
	<div id="content">
		<h1><a href=""><?php echo $TXT['name'][$lang]; ?></a></h1>
		<h2 class="tagline"><?php echo $TXT['tagline'][$lang]; ?></h2>	
		<dl>
			<dt><img class='icon' src='img/contact.gif' /></dt>
			<dd><a href="mailto:ravoro@gmail.com">ravoro@gmail.com</a></dd>
			<dt><img class='icon' src='img/social.gif' /></dt>
			<dd><a href="http://romanvorobyov.com">romanvorobyov.com</a></dd>
		</dl>
		<p class='quote'>"<?php echo $TXT['quote'][$lang]; ?>"<span class='quote-author'>-&nbsp;<a href="<?php echo $TXT['quote_author_link'][$lang]; ?>"><?php echo $TXT['quote_author'][$lang]; ?></a></span></p>
	</div>
</div>
<!--	
<div id="triples">
	<div class="t1">
		<h2>Products</h2>
		<p>Additional text goes here.</p>
	</div>
	
	<div class="t2">
		<h2>Partners</h2>
		<p>Additional text goes here.</p>
	</div>
	
	<div class="t3">
		<h2>More information</h2>
		<p>Additional text goes here.</p>
	</div>
</div>
-->
<div id="footer">
	<p>
    <a href='?lang=en'><img class='flag <?php echo $css_active_en; ?>' src='img/en.png' title='English' /></a>
    <a href='?lang=ru'><img class='flag <?php echo $css_active_ru; ?>' src='img/ru.png' title='Русский' /></a>
    <span class='copyright'>&copy; <?php echo date("Y"); ?>  <a href=""><?php echo $TXT['name'][$lang]; ?></a></span>
  </p>
</div>
</body>
</html>
