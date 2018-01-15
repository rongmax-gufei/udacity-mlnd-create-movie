# -*- coding:utf-8 -*-


class Movie():
    """movie实体类"""
    def __init__(self, movie_name, movie_image_url, movie_play_url):
        """
            movie_name：电影名称
            movie_poster_url：电影海报链接
            movie_play_url：电影播放youtube地址
        """
        self.movie_name = movie_name
        self.movie_image_url = movie_image_url
        self.movie_play_url = movie_play_url

    def __str__(self):
        return '电影名:%s \n电影海报：%s \n播放地址： %s' % (self.movie_name, self.movie_image_url, self.movie_play_url)