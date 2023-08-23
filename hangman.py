import pygame
import math
import random

# setup display
pygame.init()  #Pygame oyun geliştirme kütüphanesini kullanmaya başlamadan önce gerekli olan başlatma işlemini gerçekleştirir.
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))  # we define the dimensions
pygame.display.set_caption("Hangman Game!")






#load images
images = []
for i in range(7):
  image = pygame.image.load("hangman" + str(i) + ".png")
  images.append(image)

#button variables
RADIUS = 20
GAP = 15  #daireler arasındaki boşluk
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2) 
starty = 400
A = 65
for i in range(26):
  x = startx + GAP * 2 + ((RADIUS * 2 + GAP)* (i % 13)) #her 13 harfin sonunda konumun bir sonraki sıraya geçmesini sağlar.
  y = starty + ((i // 13) * (GAP + RADIUS * 2))  # // integer division
  letters.append([x, y, chr(A + i),True]) #chr(A + i): Bu, geçerli iterasyona (i) karşılık gelen harf karakterini oluşturur. Değişken A, 'A' karakterinin ASCII değeridir ve üzerine i eklemek geçerli harfin ASCII değerini verir.


#fonts
LETTER_FONT = pygame.font.SysFont('comicsans',40 )
WORD_FONT =  pygame.font.SysFont('comicsans',60 )
TITLE_FONT = pygame.font.SysFont('comicsans',70)


# game variables
hangman_status = 0
words = ["IDE","PYTHON","PYGAME","REPLIT"]

word = random.choice(words)
guessed = []


#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# setup game loop
FPS = 60  #FPS ölçümü, 1 saniyede ekrana aktarılan kare sayısını ifade eder.

clock = pygame.time.Clock()
run = True


def draw():
  win.fill(WHITE)
        # oyun ekranını beyaz renkle doldurarak her döngü turunda önceki karelerin üzerine yeni bir kare çizilmesi sağlanıyor. win burada oyun ekranını temsil ediyor.
  #draw title
  text = TITLE_FONT.render("DEVELOPER HANGMAN",1,BLACK)
  win.blit(text,(WIDTH/2 - text.get_width()/2,20))
  # draw word
  display_word = ""
  for letter in word:
    if letter in guessed:
      display_word += letter + " "
    else:
      display_word += "_ "
    
  text = WORD_FONT.render(display_word,1,BLACK)
  win.blit(text,(400,200))


  
  #draw buttons
  for letter in letters:
    x, y, ltr, visible= letter
    if visible:
      pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3) #harfi temsil eden daire çizer
      text = LETTER_FONT.render(ltr,1,BLACK) #harfi temsil eden texti oluşturur render() fonksiyonu:örsel nesnelerin veya metinlerin bir yüzeye çizilmesi için kullanılır 1 metin kalınlığını belirler.
      win.blit(text,(x-text.get_width()/2,y-text.get_height()/2)) # Harf metni, dairenin merkezine hizalanacak şekilde ekrana yerleştirilir. blit fonksiyonu, metni belirtilen koordinatlara yerleştirir. Metnin ortalanması için x ve y koordinatları ayarlanırken metin genişliği ve yüksekliği de dikkate alınır.


      
    
    
  win.blit(images[hangman_status], (150, 100))  #oyun ekranına belirli bir koordinata ((150, 100)) belirli bir görüntüyü çizmeyi sağlar. Burada images listesi içindeki hangman_status indeksine karşılık gelen görüntüyü ekrana çiziyor
  pygame.display.update()  #değişiklikleri ekranda güncellemek için pygame'in display modülünün update fonksiyonu çağrılıyor. Bu işlem, yeni kareleri görüntülemek için ekrana çizilen değişiklikleri işler.
draw()

def display_message(message):
  pygame.time.delay(1000)
  win.fill(WHITE)
  text = WORD_FONT.render(message,1,BLACK)
  win.blit(text,(WIDTH/2 -text.get_width()/2, HEIGHT/2 - text.get_height()/2))
  pygame.display.update()
  pygame.time.delay(3000) # 3 seconds boyunca nu yazıyı gösterecek (3000miliseconds)
  

while run:
  clock.tick(FPS)  #clock nesnesinin tick metodu çağrılarak oyun döngüsünün belirlenen FPS hızında çalışmasını sağlanıyor. Bu, oyunun her döngüsünde belirtilen FPS hızında çalışacağı anlamına gelir.
  


  for event in pygame.event.get():
    if event.type == pygame.QUIT:  # oyun penceresinin X düğmesine basıldığında oyunun kapatılmasını sağlar.
      run = False

    if event.type == pygame.MOUSEBUTTONDOWN:
      m_x,m_y  = pygame.mouse.get_pos()
      #mouse'un XY koordinatlarını alıyor
      # (0,0) noktası top-left hand cornerda
      for letter in letters:
        x,y,ltr,visible = letter
        if visible:
          dis = math.sqrt((x - m_x)**2+(y-m_y)**2)
          if dis<RADIUS: #Eğer hesaplanan uzaklık (dis) yarıçaptan (RADIUS) daha küçükse, yani fare imleci harf dairelerinden birine girmişse
            letter[3] = False
            guessed.append(ltr)
            if ltr not in word:
              hangman_status +=1

      won = True
      for letter in word:
        if letter not in guessed:
          won = False
          break
        
      if won:
        display_message("YOU WON !")
        break

      if hangman_status == 6:
        display_message("YOU LOST !")
        break
       
         
    draw()      
          
       
          
        
          


      


      
     
  
     

pygame.quit()
