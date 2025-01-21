import qrcode as qr 
img = qr.make("https://www.youtube.com/watch?v=s2lX0cBlJ1Y&list=RDs2lX0cBlJ1Y&index=1&pp=8AUB")
img.save("song_youtube.png")