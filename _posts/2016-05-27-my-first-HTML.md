---
layout: post
title:  "Learning HTML"
date:   2016-05-27 12:25
tags:
    - HTML
---

This is the first html file I have written.

{% highlight html %}
<!DOCTYPE html>
<html>
    <head>
        <title>My first HTML</title>
        <meta charset="UTF-8">
    </head>
    
    <body style="background-color:lightgrey;">
        <h1 style="color:red;">This is a red heading</h1>
        <hr>
        
        <p title="About Yu Shu">
            Frederick Smiles.
            I am Yu Shu.
        </p>
        <p style="font-family:verdana;font-size:300%;text-align:center;">
            This <br> paragraph
            contains a lot of lines
            in the source code,
            but the browser
            ignores it.
        </p>
        <!-- this is a comment -->
        <p>Here is a quote from WWF's website:</p>
        <blockquote cite="http://www.worldwildlife.org/who/index.html">
        For 50 years, WWF has been protecting the future of nature.
        The world's leading conservation organization,
        WWF works in 100 countries and is supported by
        1.2 million members in the United States and
        close to 5 million globally.
        </blockquote>
        
        <h2>Unordered List with Default Bullets</h2>
        
        <ul>
        <li>Coffee</li>
        <li>Tea</li>
        <li>Milk</li>
        </ul>
        <p>I have a date on <time datetime="2008-02-14 20:00">Valentines day</time>.</p>
    </body>
</html>
{% endhighlight %}
