from pygame import mixer
import pygame
pygame.mixer.init()
pygame.mixer.music.load("sound/X Ray Vision - Slynk.wav")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)


#로딩완료
loading=mixer.Sound("sound/loading.wav")
loading.set_volume(0.4)
#폭발
deadso1=mixer.Sound("sound/explosion01.wav")
deadso1.set_volume(0.45)
deadso2=mixer.Sound("sound/explosion02.wav")
deadso2.set_volume(0.45)
deadso3=mixer.Sound("sound/explosion03.wav")
deadso3.set_volume(0.45)
deadso4=mixer.Sound("sound/explosion04.wav")
deadso4.set_volume(0.45)
#미사일
missile=mixer.Sound("sound/missile.wav")
#먹는소리
eat1=mixer.Sound("sound/eat1.wav")
eat2=mixer.Sound("sound/eat2.wav")
eat3=mixer.Sound("sound/eat3.wav")
eat4=mixer.Sound("sound/eat4.wav")
#축하소리
cheer1=mixer.Sound("sound/people-stadium-cheer1.wav")
cheer2=mixer.Sound("sound/people-stadium-cheer2.wav")
#실패
fail=mixer.Sound("sound/fail.wav")
fail.set_volume(0.4)

endingsound=mixer.Sound("sound/Smile - Slynk.wav")
endingsound.set_volume(0.2)

locksound=mixer.Sound("sound/lock.wav")

success=mixer.Sound("sound/success.wav")
success.set_volume(0.1)