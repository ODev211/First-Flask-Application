HTML Document Structure
<!DOCTYPE html>: Declares the document type as HTML5.

<html lang="en">: The root element of the HTML document, specifying the language as English.

Head Section
<head>: Contains metadata and links to external resources.

<title>Home</title>: Specifies the title of the web page, shown in the browser tab.

<meta charset="utf-8">: Sets the character encoding to UTF-8, supporting a wide range of characters.

<meta name="viewport" content="width=device-width, initial-scale=1">: Ensures the page is responsive and scales appropriately on different devices.

Stylesheets and Scripts
<!-- Link to the main stylesheet -->: Comments are ignored by browsers and are for developers' reference.

<link rel="stylesheet" href="../static/css/style.css">: Links to the main CSS file for styling the page.

<!-- Link to the navbar stylesheet -->

<link rel="stylesheet" href="../static/css/navbar.css">: Links to the CSS file for styling the navbar.

<!-- Link to the footer stylesheet -->

<link rel="stylesheet" href="../static/css/footer.css">: Links to the CSS file for styling the footer.

<!-- Link to Bootstrap CSS for additional styling and responsiveness -->

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">: Links to the Bootstrap CSS library for additional styling and responsiveness.

<!-- jQuery library -->

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>: Links to the jQuery library for JavaScript functionality.

<!-- Bootstrap JavaScript for interactive components -->

<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>: Links to the Bootstrap JavaScript library for interactive components.

Body Section
<body>: Contains the content of the web page.

<!-- Navbar section -->: Indicates the start of the navigation bar section.

<nav class="navbar navbar-inverse">: Creates an inverse-style navbar using Bootstrap classes.

<div class="container-fluid">: A container for the navbar elements.

<div class="navbar-header">: The header section of the navbar.

<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">: A button for toggling the navbar menu on mobile devices.

<span class="icon-bar"></span>: Three bars indicating the menu button.

<a class="navbar-brand" href="/">HEALTH</a>: A brand link for the navbar.

<div class="collapse navbar-collapse" id="myNavbar">: A collapsible container for navbar links.

<ul class="nav navbar-nav">: An unordered list for left-aligned navbar links.

<li class="active"><a href="/">Home</a></li>: An active link to the home page.

<li><a href="/airquality">AQI</a></li>: A link to the air quality page.

<li><a href="/forecast">Forecast</a></li>: A link to the forecast page.

<li><a href="/riskassessment">Risks</a></li>: A link to the risk assessment page.

<li><a href="/access">Accessibility</a></li>: A link to the accessibility page.

<ul class="nav navbar-nav navbar-right">: An unordered list for right-aligned navbar links.

{% if session.user_id %}: A conditional statement checking if the user is logged in.

<li><a href="/profile"><span class="glyphicon glyphicon-user"></span> Profile</a></li>: A link to the profile page with a user icon.

<li><a href="/logout"><span class="glyphicon glyphicon-log-out"></span> Logout</a></li>: A logout link with a logout icon.

{% else %}: The else condition if the user is not logged in.

<li><a href="login"><span class="glyphicon glyphicon-log-in"></span> Login</a></li>: A login link with a login icon.

<li><a href="register"><span class="glyphicon glyphicon-user"></span> Register</a></li>: A registration link with a user icon.

{% endif %}: Ends the conditional statement.

Main Content
<!-- Rest of the body content goes here -->

<div class="container-fluid text-center">: A container for the main content, centered.

<div class="row content">: A row for the content.

<div class="col-sm-12 text-left">: A column for the content, left-aligned.

{% with messages = get_flashed_messages(with_categories=true) %}: A block to display flashed messages.

{% if messages %}: Checks if there are any messages.

<div class="alert alert-success">: A container for success messages.

{% for category, message in messages %}: Loops through each message.

<p>{{ message }}</p>: Displays each message.

{% endfor %}

{% endif %}

{% endwith %}

<h1>Welcome to Health and Advice</h1>: A heading for the welcome message.

<p>Your go-to platform for health-related insights and resources.</p>: A paragraph for the introductory text.

Footer Section
<footer class="container-fluid text-center">: A container for the footer, centered.

<p>Health Advice</p>: A paragraph for the footer text.

<div class="footer-links">: A container for the footer links.

<a href="/privacyandcookies">Privacy Policy</a> |: A link to the privacy policy.

<a href="/terms">Terms and Conditions</a> |: A link to the terms and conditions.

<a href="/contact-us">Contact Us</a>: A link to the contact page.