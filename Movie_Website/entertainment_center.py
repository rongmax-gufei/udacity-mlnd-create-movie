# -*- coding:utf-8 -*-

import media
import fresh_tomatoes

# 初始化model数据
movieOne = media.Movie("Star Wars Battlefront II", "https://i.ytimg.com/vi/WypeQtYC3Ms/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIZCGAE=&rs=AOn4CLDO0EXdWiHVheduqbfizpQaN6nEmw", "https://youtu.be/WypeQtYC3Ms")
movieTwo = media.Movie("Logan", "https://i.ytimg.com/vi/p0Xlr3La_6I/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIZCGAE=&rs=AOn4CLDtokXAqjWUDZmA3jClTR2eRY07gw", "https://youtu.be/zW-wrIlpv7E")
movieThree = media.Movie("injustice god among us", "https://i.ytimg.com/vi/KTJ9MOumqxk/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIZCGAE=&rs=AOn4CLAOb8zzQPtUHirCwYgPYuoSu2vR1A", "https://youtu.be/KTJ9MOumqxk")

# print(movieOne)
# print(movieTwo)
# print(movieThree)

# 将model数据加进数组
movies = [movieOne, movieTwo, movieThree]

# 执行页面生成函数
fresh_tomatoes.open_movies_page(movies)
