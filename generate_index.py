#!/usr/bin/env python

import os



page_head = """
<!DOCTYPE html>
<!--[if lt IE 7 ]><html class="ie ie6" lang="en"> <![endif]-->
  <!--[if IE 7 ]><html class="ie ie7" lang="en"> <![endif]-->
    <!--[if IE 8 ]><html class="ie ie8" lang="en"> <![endif]-->
      <!--[if (gte IE 9)|!(IE)]><!--><html lang="en"> <!--<![endif]-->
        <head>

          <!-- Basic Page Needs
          ================================================== -->
          <meta charset="utf-8">
          <title>Page Title</title>

          <!-- Mobile Specific Metas
          ================================================== -->
          <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

          <!-- CSS
          ================================================== -->
          <link rel="stylesheet" href="stylesheets/base.css">
          <link rel="stylesheet" href="stylesheets/skeleton.css">
          <link rel="stylesheet" href="stylesheets/layout.css">

          <!--[if lt IE 9]>
          <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
          <![endif]-->

          <!-- Favicons
          ================================================== -->
          <link rel="shortcut icon" href="images/favicon.ico">
          <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
          <link rel="apple-touch-icon" sizes="72x72" href="images/apple-touch-icon-72x72.png">
          <link rel="apple-touch-icon" sizes="114x114" href="images/apple-touch-icon-114x114.png">

        </head>
        <body>



          <!-- Primary Page Layout
          ================================================== -->
        <div class="container">
        <div class="sixteen columns">
"""
print page_head

for filename in os.listdir('.'):
  basename = os.path.splitext(filename)[0]
  if os.path.isfile(filename):
    print '<a href="%s" class="button">%s</a><br />' %(filename,basename)

print "</div></div></body></html>"
