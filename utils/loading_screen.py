import time
import pygame


def show_loading_screen(screen, font, image_path):
    # 로딩 화면 표시
    try:
        loading_image = pygame.image.load(image_path)
    except pygame.error as e:
        print(f"[오류] 로딩 이미지 불러오기 실패: {e}")
        loading_image = None

    loading_text = font.render("로딩 중...", True, (255, 255, 255))
    screen.fill((0, 0, 0))

    # 이미지가 있으면 중앙에 표시
    if loading_image:
        img_rect = loading_image.get_rect(
            center=(screen.get_width() // 2, screen.get_height() // 2 - 50)
        )
        screen.blit(loading_image, img_rect)

    # 텍스트는 이미지 아래에 표시
    text_rect = loading_text.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 50)
    )
    screen.blit(loading_text, text_rect)

    pygame.display.update()
