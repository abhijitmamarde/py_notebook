import requests
from bs4 import BeautifulSoup

# r = requests.get("http://www.python.org/")
text = '''

<!doctype html>
<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
<!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->
<!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->
<!--[if gt IE 8]><!--><html class="no-js" lang="en" dir="ltr">  <!--<![endif]-->

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">

    <meta name="application-name" content="Python.org">
    <meta name="msapplication-tooltip" content="The official home of the Python Programming Language">
    <meta name="apple-mobile-web-app-title" content="Python.org">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="HandheldFriendly" content="True">
    <meta name="format-detection" content="telephone=no">
    <meta http-equiv="cleartype" content="on">
    <meta http-equiv="imagetoolbar" content="false">

    <script src="/static/js/libs/modernizr.js"></script>

    <link href="/static/stylesheets/style.css" rel="stylesheet" type="text/css" title="default" />
    <link href="/static/stylesheets/mq.css" rel="stylesheet" type="text/css" media="not print, braille, embossed, speech, tty" />


    <!--[if (lte IE 8)&(!IEMobile)]>
    <link href="/static/stylesheets/no-mq.css" rel="stylesheet" type="text/css" media="screen" />


    <![endif]-->


    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/static/apple-touch-icon-144x144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/static/apple-touch-icon-114x114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/static/apple-touch-icon-72x72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="/static/apple-touch-icon-precomposed.png">
    <link rel="apple-touch-icon" href="/static/apple-touch-icon-precomposed.png">


    <meta name="msapplication-TileImage" content="/static/metro-icon-144x144-precomposed.png"><!-- white shape -->
    <meta name="msapplication-TileColor" content="#3673a5"><!-- python blue -->
    <meta name="msapplication-navbutton-color" content="#3673a5">

    <title>Welcome to Python.org</title>

    <meta name="description" content="The official home of the Python Programming Language">
    <meta name="keywords" content="Python programming language object oriented web free open source software license documentation download community">


    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Python.org">
    <meta property="og:title" content="Welcome to Python.org">
    <meta property="og:description" content="The official home of the Python Programming Language">

    <meta property="og:image" content="https://www.python.org/static/opengraph-icon-200x200.png">
    <meta property="og:image:secure_url" content="https://www.python.org/static/opengraph-icon-200x200.png">

    <meta property="og:url" content="https://www.python.org/">

    <link rel="author" href="/static/humans.txt">




    <script type="application/ld+json">
     {
       "@context": "http://schema.org",
       "@type": "WebSite",
       "url": "https://www.python.org/",
       "potentialAction": {
         "@type": "SearchAction",
         "target": "https://www.python.org/search/?q={search_term_string}",
         "query-input": "required name=search_term_string"
       }
     }
    </script>


    <script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-39055973-1']);
    _gaq.push(['_trackPageview']);

    (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
    </script>

</head>

<body class="python home" id="homepage">

    <div id="touchnav-wrapper">

        <div id="nojs" class="do-not-print">
            <p><strong>Notice:</strong> While Javascript is not essential for this website, your interaction with the content will be limited. Please turn Javascript on for the full experience. </p>
        </div>

        <!--[if lt IE 8]>
        <div id="oldie-warning" class="do-not-print">
            <p><strong>Notice:</strong> Your browser is <em>ancient</em> and <a href="http://www.ie6countdown.com/">Microsoft agrees</a>. <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience a better web.</p>
        </div>
        <![endif]-->

        <!-- Sister Site Links -->
        <div id="top" class="top-bar do-not-print">

            <nav class="meta-navigation container" role="navigation">


                <div class="skip-link screen-reader-text">
                    <a href="#content" title="Skip to content">Skip to content</a>
                </div>


                <a id="close-python-network" class="jump-link" href="#python-network" aria-hidden="true">
                    <span aria-hidden="true" class="icon-arrow-down"><span>&#9660;</span></span> Close
                </a>



<ul class="menu" role="tree">

    <li class="python-meta current_item selectedcurrent_branch selected">
        <a href="/" title="The Python Programming Language" class="current_item selectedcurrent_branch selected">Python</a>
    </li>

    <li class="psf-meta ">
        <a href="/psf-landing/" title="The Python Software Foundation" >PSF</a>
    </li>

    <li class="docs-meta ">
        <a href="https://docs.python.org" title="Python Documentation" >Docs</a>
    </li>

    <li class="pypi-meta ">
        <a href="https://pypi.python.org/" title="Python Package Index" >PyPI</a>
    </li>

    <li class="jobs-meta ">
        <a href="/jobs/" title="Python Job Board" >Jobs</a>
    </li>

    <li class="shop-meta ">
        <a href="/community/" title="Python Community" >Community</a>
    </li>

</ul>


                <a id="python-network" class="jump-link" href="#top" aria-hidden="true">
                    <span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> The Python Network
                </a>

            </nav>

        </div>

        <!-- Header elements -->
        <header class="main-header" role="banner">
            <div class="container">

                <h1 class="site-headline">
                    <a href="/"><img class="python-logo" src="/static/img/python-logo.png" alt="python&trade;"></a>
                </h1>

                <div class="options-bar do-not-print">


                    <a id="site-map-link" class="jump-to-menu" href="#site-map"><span class="menu-icon">&equiv;</span> Menu</a><form class="search-the-site" action="/search/" method="get">
                        <fieldset title="Search Python.org">

                            <span aria-hidden="true" class="icon-search"></span>

                            <label class="screen-reader-text" for="id-search-field">Search This Site</label>
                            <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">

                            <button type="submit" name="submit" id="submit" class="search-button" title="Submit this Search" tabindex="3">
                                GO
                            </button>


                            <!--[if IE]><input type="text" style="display: none;" disabled="disabled" size="1" tabindex="4"><![endif]-->

                        </fieldset>
                    </form><span class="breaker"></span><div class="adjust-font-size" aria-hidden="true">
                        <ul class="navigation menu" aria-label="Adjust Text Size on Page">
                            <li class="tier-1 last" aria-haspopup="true">
                                <a href="#" class="action-trigger"><strong><small>A</small> A</strong></a>
                                <ul class="subnav menu">
                                    <li class="tier-2 element-1" role="treeitem"><a class="text-shrink" title="Make Text Smaller" href="javascript:;">Smaller</a></li>
                                    <li class="tier-2 element-2" role="treeitem"><a class="text-grow" title="Make Text Larger" href="javascript:;">Larger</a></li>
                                    <li class="tier-2 element-3" role="treeitem"><a class="text-reset" title="Reset any font size changes I have made" href="javascript:;">Reset</a></li>
                                </ul>
                            </li>
                        </ul>
                    </div><div class="winkwink-nudgenudge">
                        <ul class="navigation menu" aria-label="Social Media Navigation">
                            <li class="tier-1 last" aria-haspopup="true">
                                <a href="#" class="action-trigger">Socialize</a>
                                <ul class="subnav menu">
                                    <li class="tier-2 element-1" role="treeitem"><a href="http://plus.google.com/+Python"><span aria-hidden="true" class="icon-google-plus"></span>Google+</a></li>
                                    <li class="tier-2 element-2" role="treeitem"><a href="http://www.facebook.com/pythonlang?fref=ts"><span aria-hidden="true" class="icon-facebook"></span>Facebook</a></li>
                                    <li class="tier-2 element-3" role="treeitem"><a href="http://twitter.com/ThePSF"><span aria-hidden="true" class="icon-twitter"></span>Twitter</a></li>
                                    <li class="tier-2 element-4" role="treeitem"><a href="/community/irc/"><span aria-hidden="true" class="icon-freenode"></span>Chat on IRC</a></li>
                                </ul>
                            </li>
                        </ul>
                    </div><div class="account-signin">
                        <ul class="navigation menu" aria-label="Social Media Navigation">
                            <li class="tier-1 last" aria-haspopup="true">

                                <a href="/accounts/login/" title="Sign Up or Sign In to Python.org">Sign In</a>
                                <ul class="subnav menu">
                                    <li class="tier-2 element-1" role="treeitem"><a href="/accounts/signup/">Sign Up / Register</a></li>
                                    <li class="tier-2 element-2" role="treeitem"><a href="/accounts/login/">Sign In</a></li>
                                </ul>

                            </li>
                        </ul>
                    </div>

                </div><!-- end options-bar -->

                <nav id="mainnav" class="python-navigation main-navigation do-not-print" role="navigation">


<ul class="navigation menu" role="menubar" aria-label="Main Navigation">



    <li id="about" class="tier-1 element-1  " aria-haspopup="true">
        <a href="/about/" title="" class="">About</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>

</ul>


    </li>



    <li id="downloads" class="tier-1 element-2  " aria-haspopup="true">
        <a href="/downloads/" title="" class="">Downloads</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/mac-osx/" title="">Mac OS X</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>

</ul>


    </li>



    <li id="documentation" class="tier-1 element-3  " aria-haspopup="true">
        <a href="/doc/" title="" class="">Documentation</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner&#39;s Guide</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="https://docs.python.org/devguide/" title="">Developer&#39;s Guide</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="http://python.org/dev/peps/" title="">PEP Index</a></li>

        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>

</ul>


    </li>



    <li id="community" class="tier-1 element-4  " aria-haspopup="true">
        <a href="/community/" title="" class="">Community</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>

        <li class="tier-2 element-8" role="treeitem"><a href="/community/merchandise/" title="">Merchandise</a></li>

        <li class="tier-2 element-9" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>

</ul>


    </li>



    <li id="success-stories" class="tier-1 element-5  " aria-haspopup="true">
        <a href="/about/success/" title="success-stories" class="">Success Stories</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/about/success/#arts" title="">Arts</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/about/success/#business" title="">Business</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/about/success/#education" title="">Education</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/about/success/#engineering" title="">Engineering</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="/about/success/#government" title="">Government</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="/about/success/#scientific" title="">Scientific</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="/about/success/#software-development" title="">Software Development</a></li>

</ul>


    </li>



    <li id="news" class="tier-1 element-6  " aria-haspopup="true">
        <a href="/blogs/" title="News from around the Python world" class="">News</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">Community News</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon News</a></li>

</ul>


    </li>



    <li id="events" class="tier-1 element-7  " aria-haspopup="true">
        <a href="/events/" title="" class="">Events</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events" title="">Python Events</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>

</ul>


    </li>





</ul>


                </nav>

                <div class="header-banner "> <!-- for optional "do-not-print" class -->

        <div id="dive-into-python" class="flex-slideshow slideshow">

            <ul class="launch-shell menu" id="launch-shell">
                <li>
                    <a class="button prompt" id="start-shell" data-shell-container="#dive-into-python" href="/shell/">&gt;_
                        <span class="message">Launch Interactive Shell</span>
                    </a>
                </li>
            </ul>

            <ul class="slides menu">

                <li>
                    <div class="slide-code"><pre><code><span class="comment"># Python 3: Fibonacci series up to n</span>
>>> def fib(n):
>>>     a, b = 0, 1
>>>     while a &lt; n:
>>>         print(a, end=' ')
>>>         a, b = b, a+b
>>>     print()
>>> fib(1000)
<span class="output">0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987</span></code></pre></div>
                    <div class="slide-copy"><h1>Functions Defined</h1>
<p>The core of extensible programming is defining functions. Python allows mandatory and optional arguments, keyword arguments, and even arbitrary argument lists. <a href="//docs.python.org/3/tutorial/controlflow.html#defining-functions">More about defining functions in Python&nbsp;3</a></p></div>
                </li>

                <li>
                    <div class="slide-code"><pre><code><span class="comment"># Python 3: List comprehensions</span>
>>> fruits = ['Banana', 'Apple', 'Lime']
>>> loud_fruits = [fruit.upper() for fruit in fruits]
>>> print(loud_fruits)
<span class="output">['BANANA', 'APPLE', 'LIME']</span>

<span class="comment"># List and the enumerate function</span>
>>> list(enumerate(fruits))
<span class="output">[(0, 'Banana'), (1, 'Apple'), (2, 'Lime')]</span></code></pre></div>
                    <div class="slide-copy"><h1>Compound Data Types</h1>
<p>Lists (known as arrays in other languages) are one of the compound data types that Python understands. Lists can be indexed, sliced and manipulated with other built-in functions. <a href="//docs.python.org/3/tutorial/introduction.html#lists">More about lists in Python&nbsp;3</a></p></div>
                </li>

                <li>
                    <div class="slide-code"><pre><code><span class="comment"># Python 3: Simple arithmetic</span>
>>> 1 / 2
<span class="output">0.5</span>
>>> 2 ** 3
<span class="output">8</span>
>>> 17 / 3  <span class="comment"># classic division returns a float</span>
<span class="output">5.666666666666667</span>
>>> 17 // 3  <span class="comment"># floor division</span>
<span class="output">5</span></code></pre></div>
                    <div class="slide-copy"><h1>Intuitive Interpretation</h1>
<p>Calculations are simple with Python, and expression syntax is straightforward: the operators <code>+</code>, <code>-</code>, <code>*</code> and <code>/</code> work as expected; parentheses <code>()</code> can be used for grouping. <a href="http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator">More about simple math functions in Python&nbsp;3</a>.</p></div>
                </li>

                <li>
                    <div class="slide-code"><pre><code><span class="comment"># Python 3: Simple output (with Unicode)</span>
>>> print("Hello, I'm Python!")
<span class="output">Hello, I'm Python!</span>

<span class="comment"># Input, assignment</span>
>>> name = input('What is your name?\n')
>>> print('Hi, %s.' % name)
<span class="output">What is your name?
Python
Hi, Python.</span></code></pre></div>
                    <div class="slide-copy"><h1>Quick &amp; Easy to Learn</h1>
<p>Experienced programmers in any other language can pick up Python very quickly, and beginners find the clean syntax and indentation structure easy to learn. <a href="//docs.python.org/3/tutorial/">Whet your appetite</a> with our Python&nbsp;3 overview.</p>
                   </div>
                </li>

                <li>
                    <div class="slide-code"><pre><code><span class="comment"># For loop on a list</span>
>>> numbers = [2, 4, 6, 8]
>>> product = 1
>>> for number in numbers:
...    product = product * number
...
>>> print('The product is:', product)
<span class="output">The product is: 384</span></code></pre></div>
                    <div class="slide-copy"><h1>All the Flow You&rsquo;d Expect</h1>
<p>Python knows the usual control flow statements that other languages speak &mdash; <code>if</code>, <code>for</code>, <code>while</code> and <code>range</code> &mdash; with some of its own twists, of course. <a href="//docs.python.org/3/tutorial/controlflow.html">More control flow tools in Python&nbsp;3</a></p></div>
                </li>

            </ul>
        </div>


                </div>


        <div class="introduction">
            <p>Python is a programming language that lets you work quickly <span class="breaker"></span>and integrate systems more effectively. <a class="readmore" href="/doc/">Learn More</a></p>
        </div>


             </div><!-- end .container -->
        </header>

        <div id="content" class="content-wrapper">
            <!-- Main Content Column -->
            <div class="container">

                <section class="main-content " role="main">








                <div class="row">

                    <div class="small-widget get-started-widget">
                        <h2 class="widget-title"><span aria-hidden="true" class="icon-get-started"></span>Get Started</h2>
<p>Whether you're new to programming or an experienced developer, it's easy to learn and use Python.</p>
<p><a href="/about/gettingstarted/">Start with our Beginner&rsquo;s Guide</a></p>
                    </div>

                    <div class="small-widget download-widget">
                        <h2 class="widget-title"><span aria-hidden="true" class="icon-download"></span>Download</h2>
<p>Python source code and installers are available for download for all versions! Not sure which version to use? <a href="https://wiki.python.org/moin/Python2orPython3">Check here</a>.</p>
<p>Latest: <a href="/downloads/release/python-361/">Python 3.6.1</a> - <a href="/downloads/release/python-2713/">Python 2.7.13</a></p>
                    </div>

                    <div class="small-widget documentation-widget">
                        <h2 class="widget-title"><span aria-hidden="true" class="icon-documentation"></span>Docs</h2>
<p>Documentation for Python's standard library, along with tutorials and guides, are available online.</p>
<p><a href="https://docs.python.org">docs.python.org</a></p>
                    </div>

                    <div class="small-widget jobs-widget last">
                        <h2 class="widget-title"><span aria-hidden="true" class="icon-jobs"></span>Jobs</h2>
<p>Looking for work or have a Python related position that you're trying to hire for? Our <strong>relaunched community-run job board</strong> is the place to go.</p>
<p><a href="//jobs.python.org">jobs.python.org</a></p>
                    </div>

                </div>

                <div class="list-widgets row">

                    <div class="medium-widget blog-widget">

                        <div class="shrubbery">

                            <h2 class="widget-title"><span aria-hidden="true" class="icon-news"></span>Latest News</h2>
                            <p class="give-me-more"><a href="http://blog.python.org" title="More News">More</a></p>

                            <ul class="menu">


                                <li>
<time datetime="2017-03-22T03:13:00.000002+00:00"><span class="say-no-more">2017-</span>03-22</time>
 <a href="http://feedproxy.google.com/~r/PythonInsider/~3/C-xfWJKP0-A/python-361-is-now-available.html">Python 3.6.1 is now available. &nbsp; Python 3.6.1 is the ...</a></li>

                                <li>
<time datetime="2017-03-05T12:11:00.000006+00:00"><span class="say-no-more">2017-</span>03-05</time>
 <a href="http://feedproxy.google.com/~r/PythonInsider/~3/w2AW2NRSOEM/python-361rc1-is-now-available-for.html">Python 3.6.1rc1 is now available. &nbsp; Python 3.6.1rc1 is the ...</a></li>

                                <li>
<time datetime="2017-01-17T08:40:00.000001+00:00"><span class="say-no-more">2017-</span>01-17</time>
 <a href="http://feedproxy.google.com/~r/PythonInsider/~3/NeIHRAidlpc/python-353-and-346-are-now-available.html">Python 3.5.3 and Python 3.4.6 are now available for download. ...</a></li>

                                <li>
<time datetime="2017-01-03T02:24:00.000001+00:00"><span class="say-no-more">2017-</span>01-03</time>
 <a href="http://feedproxy.google.com/~r/PythonInsider/~3/UoiMThSwgQM/python-353rc1-and-python-346rc1-are-now.html">Python 3.5.3rc1 and Python 3.4.6rc1 are now available for download. ...</a></li>

                                <li>
<time datetime="2016-12-23T10:11:00.000004+00:00"><span class="say-no-more">2016-</span>12-23</time>
 <a href="http://feedproxy.google.com/~r/PythonInsider/~3/4gOtq8ChYHk/python-360-is-now-available.html">Python 3.6.0 is now available! &nbsp; Python 3.6.0 is the ...</a></li>

                            </ul>
                        </div><!-- end .shrubbery -->

                    </div>

                    <div class="medium-widget event-widget last">

                        <div class="shrubbery">

                            <h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events</h2>
                            <p class="give-me-more"><a href="/events/calendars/" title="More Events">More</a></p>

                            <ul class="menu">



                                <li>
<time datetime="2017-06-06T00:00:00+00:00"><span class="say-no-more">2017-</span>06-06</time>
 <a href="/events/python-events/523/">PyCon Taiwan 2017</a></li>



                                <li>
<time datetime="2017-06-09T00:00:00+00:00"><span class="say-no-more">2017-</span>06-09</time>
 <a href="/events/python-events/513/">PyCon CZ 2017</a></li>



                                <li>
<time datetime="2017-06-10T00:00:00+00:00"><span class="say-no-more">2017-</span>06-10</time>
 <a href="/events/python-events/531/">PythonDay Mexico</a></li>



                                <li>
<time datetime="2017-06-12T00:00:00+00:00"><span class="say-no-more">2017-</span>06-12</time>
 <a href="/events/python-events/527/">PyCon Israel 2017</a></li>



                                <li>
<time datetime="2017-06-12T00:00:00+00:00"><span class="say-no-more">2017-</span>06-12</time>
 <a href="/events/python-events/509/">PyParis 2017</a></li>


                            </ul>
                        </div>

                    </div>

                </div>

                <div class="row">

                    <div class="medium-widget success-stories-widget">


                        <div class="shrubbery">


                            <h2 class="widget-title"><span aria-hidden="true" class="icon-success-stories"></span>Success Stories</h2>
                            <p class="give-me-more"><a href="/success-stories/" title="More Success Stories">More</a></p>


                            <div class="success-story-item" data-weight="25" id="success-story-2" style="display: none;">

                            <blockquote>
                                <a href="/success-stories/industrial-light-magic-runs-python/">ILM runs a batch processing environment capable of modeling, rendering and compositing tens of thousands of motion picture frames per day. Thousands of machines running Linux, IRIX, Compaq Tru64, OS X, Solaris, and Windows join together to provide a production pipeline used by ~800 users daily. Speed of development is key, and Python was a faster way to code (and re-code) the programs that control this production pipeline.</a>
                            </blockquote>

                            <table cellpadding="0" cellspacing="0" border="0" width="100%" class="quote-from">
                                <tbody>
                                    <tr>

                                        <td><p><a href="/success-stories/industrial-light-magic-runs-python/">Industrial Light &amp; Magic Runs on Python</a> <em>by Tim Fortenberry</em></p></td>
                                    </tr>
                                </tbody>
                            </table>
                            </div>


                        </div><!-- end .shrubbery -->

                    </div>

                    <div class="medium-widget applications-widget last">
                        <div class="shrubbery">
                            <h2 class="widget-title"><span aria-hidden="true" class="icon-python"></span>Use Python for&hellip;</h2>
<p class="give-me-more"><a href="/about/apps" title="More Applications">More</a></p>

<ul class="menu">
    <li><b>Web Development</b>:
        <span class="tag-wrapper"><a class="tag" href="http://www.djangoproject.com/">Django</a>, <a class="tag" href="http://www.pylonsproject.org/">Pyramid</a>, <a class="tag" href="http://bottlepy.org">Bottle</a>, <a class="tag" href="http://tornadoweb.org">Tornado</a>, <a href="http://flask.pocoo.org/" class="tag">Flask</a>, <a class="tag" href="http://www.web2py.com/">web2py</a></span></li>
    <li><b>GUI Development</b>:
        <span class="tag-wrapper"><a class="tag" href="http://wiki.python.org/moin/TkInter">tkInter</a>, <a class="tag" href="https://wiki.gnome.org/Projects/PyGObject">PyGObject</a>, <a class="tag" href="http://www.riverbankcomputing.co.uk/software/pyqt/intro">PyQt</a>, <a class="tag" href="https://wiki.qt.io/PySide">PySide</a>, <a class="tag" href="https://kivy.org/">Kivy</a>, <a class="tag" href="http://www.wxpython.org/">wxPython</a></span></li>
    <li><b>Scientific and Numeric</b>:
        <span class="tag-wrapper">
<a class="tag" href="http://www.scipy.org">SciPy</a>, <a class="tag" href="http://pandas.pydata.org/">Pandas</a>, <a href="http://ipython.org" class="tag">IPython</a></span></li>
    <li><b>Software Development</b>:
        <span class="tag-wrapper"><a class="tag" href="http://buildbot.net/">Buildbot</a>, <a class="tag" href="http://trac.edgewall.org/">Trac</a>, <a class="tag" href="http://roundup.sourceforge.net/">Roundup</a></span></li>
    <li><b>System Administration</b>:
        <span class="tag-wrapper"><a class="tag" href="http://www.ansible.com">Ansible</a>, <a class="tag" href="http://www.saltstack.com">Salt</a>, <a class="tag" href="https://www.openstack.org">OpenStack</a></span></li>
</ul>

                        </div><!-- end .shrubbery -->
                    </div>

                </div>


                <div class="pep-widget">

                    <h2 class="widget-title">
                        <span class="prompt">&gt;&gt;&gt;</span> <a href="/dev/peps/">Python Enhancement Proposals<span class="say-no-more"> (PEPs)</span></a>: The future of Python<span class="say-no-more"> is discussed here.</span>
                        <a aria-hidden="true" class="rss-link" href="/dev/peps/peps.rss"><span class="icon-feed"></span> RSS</a>
                    </h2>




                </div>

                                <div class="psf-widget">

                    <div class="python-logo"></div>

                    <h2 class="widget-title">
    <span class="prompt">&gt;&gt;&gt;</span> <a href="/psf/">Python Software Foundation</a>
</h2>
<p>The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. <a class="readmore" href="/psf/">Learn more</a> </p>
<p class="click-these">
    <a class="button" href="/users/membership/">Become a Member</a>
    <a class="button" href="/psf/donations/">Donate to the PSF</a>
</p>
                </div>




                </section>








            </div><!-- end .container -->
        </div><!-- end #content .content-wrapper -->

        <!-- Footer and social media list -->
        <footer id="site-map" class="main-footer" role="contentinfo">
            <div class="main-footer-links">
                <div class="container">


                    <a id="back-to-top-1" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> Back to Top</a>



<ul class="sitemap navigation menu do-not-print" role="tree" id="container">

    <li class="tier-1 element-1">
        <a href="/about/" >About</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>

</ul>


    </li>

    <li class="tier-1 element-2">
        <a href="/downloads/" >Downloads</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/mac-osx/" title="">Mac OS X</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>

</ul>


    </li>

    <li class="tier-1 element-3">
        <a href="/doc/" >Documentation</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner&#39;s Guide</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="https://docs.python.org/devguide/" title="">Developer&#39;s Guide</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="http://python.org/dev/peps/" title="">PEP Index</a></li>

        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>

</ul>


    </li>

    <li class="tier-1 element-4">
        <a href="/community/" >Community</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>

        <li class="tier-2 element-8" role="treeitem"><a href="/community/merchandise/" title="">Merchandise</a></li>

        <li class="tier-2 element-9" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>

</ul>


    </li>

    <li class="tier-1 element-5">
        <a href="/about/success/" title="success-stories">Success Stories</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/about/success/#arts" title="">Arts</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/about/success/#business" title="">Business</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/about/success/#education" title="">Education</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/about/success/#engineering" title="">Engineering</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="/about/success/#government" title="">Government</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="/about/success/#scientific" title="">Scientific</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="/about/success/#software-development" title="">Software Development</a></li>

</ul>


    </li>

    <li class="tier-1 element-6">
        <a href="/blogs/" title="News from around the Python world">News</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">Community News</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon News</a></li>

</ul>


    </li>

    <li class="tier-1 element-7">
        <a href="/events/" >Events</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events" title="">Python Events</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>

</ul>


    </li>

    <li class="tier-1 element-8">
        <a href="/dev/" >Contributing</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="http://docs.python.org/devguide/" title="">Developer&#39;s Guide</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="https://bugs.python.org/" title="">Issue Tracker</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="https://mail.python.org/mailman/listinfo/python-dev" title="">python-dev list</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/dev/core-mentorship/" title="">Core Mentorship</a></li>

</ul>


    </li>

</ul>


                    <a id="back-to-top-2" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> Back to Top</a>


                </div><!-- end .container -->
            </div> <!-- end .main-footer-links -->

            <div class="site-base">
                <div class="container">

                    <ul class="footer-links navigation menu do-not-print" role="tree">
                        <li class="tier-1 element-1"><a href="/about/help/">Help &amp; <span class="say-no-more">General</span> Contact</a></li>
                        <li class="tier-1 element-2"><a href="/community/diversity/">Diversity <span class="say-no-more">Initiatives</span></a></li>
                        <li class="tier-1 element-3"><a href="https://github.com/python/pythondotorg/issues">Submit Website Bug</a></li>
                        <li class="tier-1 element-4">
                            <a href="https://status.python.org/">Status <span class="python-status-indicator-default" id="python-status-indicator"></span></a>
                        </li>
                    </ul>

                    <div class="copyright">
                        <p><small>
                            <span class="pre">Copyright &copy;2001-2017.</span>
                            &nbsp;<span class="pre"><a href="/psf-landing/">Python Software Foundation</a></span>
                            &nbsp;<span class="pre"><a href="/about/legal/">Legal Statements</a></span>
                            &nbsp;<span class="pre"><a href="/privacy/">Privacy Policy</a></span>
                        </small></p>
                    </div>

                </div><!-- end .container -->
            </div><!-- end .site-base -->

        </footer>

    </div><!-- end #touchnav-wrapper -->


    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="/static/js/libs/jquery-1.8.2.min.js"><\/script>')</script>

    <script src="/static/js/libs/masonry.pkgd.min.js"></script>

    <script type="text/javascript" src="/static/js/main-min.js" charset="utf-8"></script>


    <!--[if lte IE 7]>
    <script type="text/javascript" src="/static/js/plugins/IE8-min.js" charset="utf-8"></script>


    <![endif]-->

    <!--[if lte IE 8]>
    <script type="text/javascript" src="/static/js/plugins/getComputedStyle-min.js" charset="utf-8"></script>


    <![endif]-->






</body>
</html>
'''
soup = BeautifulSoup(text, 'html.parser')

for div in soup.find_all('div'):
    for a in div.find_all('a'):
        print(a)