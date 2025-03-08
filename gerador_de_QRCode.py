import segno
seuLink = "https://exemplo.com"
corDoQR = "#191919"
corDoFundo = "#f4a100"
img = segno.make(seuLink)
img.save('img.png', dark=corDoQR , light=corDoFundo, scale=5)
