[9:14 PM] import serial
import pygame
import random
ser = serial.Serial("COM5", 9600, timeout=0.01)
pygame.init()
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Shooter Game")
clock = pygame.time.Clock()
x, y = 400, 500
size = 40
color = (0, 255, 0)
bullets = []
enemies = []
score = 0
game_over = False
jx, jy, btn = 512, 512, 1
smoothed_dx = 0
smoothing_factor = 0.2
def map_range(v, a1, a2, b1, b2):
    return (v - a1) * (b2 - b1) / (a2 - a1) + b1
def restart():
    global x, y, bullets, enemies, score, game_over
    x, y = 400, 500
    bullets = []
    enemies = []
    score = 0
    game_over = False
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_r:
                restart()
    if game_over:
        win.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 60)
        t = font.render("GAME OVER", True, (255, 0, 0))
        s = font.render(f"Score: {score}", True, (255, 255, 255))
        r = font.render("Press R to Restart", True, (200, 200, 200))
        win.blit(t, (250, 200))
        win.blit(s, (300, 280))
        win.blit(r, (210, 350))
        pygame.display.update()
        clock.tick(60)
        continue
    try:
        while ser.in_waiting:
            line = ser.readline().decode(errors='ignore').strip()
            if line:
                try:
                    jx, jy, btn = map(int, line.split(","))
                except:
                    pass
    except:
        pass
    target_dx = map_range(jx, 0, 1023, -10, 10)
    smoothed_dx += (target_dx - smoothed_dx) * smoothing_factor
    x += smoothed_dx
    x = max(0, min(800 - size, x))
    if btn == 0:
        bullets.append([x + size // 2, y])
    for b in bullets:
        b[1] -= 10
    bullets = [b for b in bullets if b[1] > 0]
    if random.random() < 0.03:
        enemies.append([random.randint(0, 760), -20])
    for en in enemies:
        en[1] += 3
        if en[1] > 600:
            game_over = True
    new_enemies = []
    for en in enemies:
        hit = False
        for b in bullets:
            if b[0] > en[0] and b[0] < en[0] + 40 and b[1] < en[1] + 40 and b[1] > en[1]:
                bullets.remove(b)
                score += 1
                hit = True
                break
        if not hit:
            new_enemies.append(en)
    enemies = new_enemies
    win.fill((0, 0, 0))
    pygame.draw.rect(win, color, (x, y, size, size))
    for b in bullets:
        pygame.draw.rect(win, (255, 255, 0), (b[0], b[1], 5, 10))
    for en in enemies:
        pygame.draw.rect(win, (255, 0, 0), (en[0], en[1], 40, 40))
    font = pygame.font.SysFont(None, 40)
    s = font.render(f"Score: {score}", True, (255, 255, 255))
    win.blit(s, (10, 10))
    pygame.display.update()
    clock.tick(60)
pygame.quit()