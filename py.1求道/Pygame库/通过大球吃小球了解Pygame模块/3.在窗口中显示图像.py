import pygame


def main():

    pygame.init()
    top_window = pygame.display.set_mode((1250, 700))#QwQ:建议不要超过1250X700
    pygame.display.set_caption('图像显示')
    top_window.fill((255, 255, 255))

    #通过指定的文件名加载图像
    png_image = pygame.image.load('/py.0初出凡尘/12.文件/copy_xp.png')
    #修改传入图像的大小
                                             # QwQ:需要修改的图像,(新的宽度,新的高度)
    png_image_trans = pygame.transform.smoothscale(png_image, (650, 450))
    #在窗口上渲染图像
               #QwQ:图像对象       图像左上角位于屏幕上的位置(坐标)
    top_window.blit(png_image_trans, (50, 80))
    #刷新屏幕
    pygame.display.flip()  #QwQ:切记,在所有渲染操作结束后一定要刷新屏幕.不必每个渲染操作后都跟一遍刷新.

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()