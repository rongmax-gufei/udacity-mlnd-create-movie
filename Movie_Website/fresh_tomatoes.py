# -*- coding：utf-8 -*-

import webbrowser
import os
import re

# page head contains js && styles
html_page_head = """
<head> 
    <meta charset="utf-8"> 
    <title>Fresh Tomatoes!</title> 

    <!-- Bootstrap 3 --> 
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css"> 
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css"> 
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script> 
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script> 
    <style type="text/css" media="screen"> 
        body { 
            padding-top: 80px; 
        } 
        #trailer .modal-dialog { 
            margin-top: 200px; 
            width: 640px; 
            height: 480px; 
        } 
        .hanging-close { 
            position: absolute; 
            top: -12px; 
            right: -12px; 
            z-index: 9001; 
        } 
        #trailer-video { 
            width: 100%; 
            height: 100%; 
        } 
        .movie-title { 
            margin-bottom: 20px; 
            padding-top: 20px; 
        } 
        .movie-title:hover { 
            background-color: #EEE; 
            cursor: pointer; 
        } 
        .scale-media { 
            padding-bottom: 56.25%; 
            position: relative; 
        } 
        .scale-media iframe { 
            border: none; 
            height: 100%; 
            position: absolute; 
            width: 100%; 
            left: 0; 
            top: 0; 
            background-color: white; 
        } 
    </style> 
    <script type="text/javascript" charset="utf-8"> 
        
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) { 
            $("#trailer-video-container").empty(); 
        }); 
        
        $(document).on('click', '.movie-title', function (event) { 
            var trailerSrc = $(this).attr('data_youtube_src') 
            var sourceUrl = trailerSrc + '?autoplay=1&html5=1'; 
            $("#trailer-video-container").empty().append($("<iframe></iframe>", { 
              'id': 'trailer-video', 
              'type': 'text-html', 
              'src': sourceUrl, 
              'frameborder': 0 
            })); 
        }); 
        
        $(document).ready(function () { 
          $('.movie-title').hide().first().show("fast", function showNext() { 
            $(this).next("div").show("fast", showNext); 
          }); 
        }); 
    </script> 
</head> 
"""

# html page
html_page_content = """
<!DOCTYPE html> 
<html lang="en"> 
  <body> 
    <div class="modal" id="trailer"> 
      <div class="modal-dialog"> 
        <div class="modal-content"> 
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true"> 
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/> 
          </a> 
          <div class="scale-media" id="trailer-video-container"> 
          </div> 
        </div> 
      </div> 
    </div> 

    <div class="container"> 
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation"> 
        <div class="container"> 
          <div class="navbar-header"> 
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a> 
          </div> 
        </div> 
      </div> 
    </div> 
    <div class="container"> 
      {movie_container} 
    </div> 
  </body> 
</html> 
"""

# single movie page template
html_single_movie_content = """ 
<div class="col-md-6 col-lg-4 movie-title text-center" data_youtube_src="{youtube_src}" data-toggle="modal" data-target="#trailer" > 
    <img src="{movie_image_url}" width="336" height="188"> 
    <h2>{movie_name}</h2> 
</div> 
"""


def get_youtube_id(movie):
    play_url = movie.movie_play_url
    # match movie id from youtube url
    id_match = re.search(r'(?<=v=)[^&#]+', play_url)
    id_match = id_match or re.search(r'(?<=be/)[^&#]+', play_url)
    youtube_id = id_match.group(0) if id_match else None
    return youtube_id


def generate_movie_content(movies):
    content = ''
    for movie in movies:
        youtube_url = 'http://youtube.com/embed/' + get_youtube_id(movie)
        content += html_single_movie_content.format(movie_name=movie.movie_name, movie_image_url=movie.movie_image_url, youtube_src=youtube_url)
    return content


def open_movies_page(movies):
    # create html page
    output_file = open('fresh_tomatoes.html', 'w')

    rendered_content = html_page_content.format(movie_container=generate_movie_content(movies))

    output_file.write(html_page_head + rendered_content)
    output_file.close()

    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)