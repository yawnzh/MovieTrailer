import media,fresh_tomatoes
#create 3 instances of Movie class for 3 movies 
movies=[]
m1=media.Movie("Monkey King: Hero is back","http://i3.sinaimg.cn/ent/2015/0209/U12106P28DT20150209114918.jpg","https://www.youtube.com/watch?v=YmIbnfh-2DA")
m2=media.Movie("ANT-MAN","http://ia.media-imdb.com/images/M/MV5BMjM2NTQ5Mzc2M15BMl5BanBnXkFtZTgwNTcxMDI2NTE@._V1_SX640_SY720_.jpg","https://www.youtube.com/watch?v=pWdKf3MneyI")
m3=media.Movie("Minions","http://img.loveitsomuch.com/uploads/201501/28/20/2015%20minions%20stuart%20kevin%20bob%20movie%20poster%20illumination%20presents%20-%20minions%20poster%20minions%20wallpaper-f65785.jpg","https://www.youtube.com/watch?v=ZiakC19KpRA")
movies.append(m1)
movies.append(m2)
movies.append(m3)
#call the open_movies_page() function to create html file and open it in a browser.
fresh_tomatoes.open_movies_page(movies)
