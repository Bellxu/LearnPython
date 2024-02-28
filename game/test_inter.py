import pygame
import sys

# 初始化Pygame
pygame.init()

# 设置屏幕尺寸
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置游戏标题
pygame.display.set_caption("Move Object Example")

# 定义一个矩形对象
rect = pygame.Rect(100, 100, 50, 50)

# 设置移动间隔时间（毫秒）
move_interval = 1000

# 游戏主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 获取当前时间（毫秒）
    current_time = pygame.time.get_ticks()

    # 判断是否到达移动时间
    if current_time % move_interval< pygame.time.get_ticks() - rect.x:
        rect.x += 20

    # 绘制背景
    screen.fill((255, 255, 255))

    # 绘制矩形对象
    pygame.draw.rect(screen, (0, 0, 255), rect)

    # 更新屏幕显示
    pygame.display.update()

    # 控制帧率
    pygame.time.Clock().tick(60)