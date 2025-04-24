import os
import sys
import time
import pygame
import openai
import random
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = openai.Client(api_key=api_key)

# 아래 import 오류나지 않게 하기
FILE = Path(__file__).resolve()  # 현재 python 파일의 절대경로
ROOT = FILE.parents[0]  # 현재 python 파일의 이전 경로
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # PATH에 ROOT 추가가
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # 상대경로로 변경경

from utils.STT import STT
from utils.TTS import TTS
from utils.character import (
    create_enemy_image,
    create_character_image,
    create_pokemon_image,
)
from utils.loading_screen import show_loading_screen

MAPS = os.path.join(ROOT, "Maps")
BACKGROUND = os.path.join(MAPS, "background.png")
LOADING_SCREEN = os.path.join(MAPS, "loading_screen.png")

# 기본 초기화
pygame.init()

# 화면 크기 설정
scale = 4
screen_width = 160 * scale  # 가로 크기
screen_height = 144 * scale  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("포켓몬 - 4천왕을 이겨라!!")  # 게임 이름

# 캐릭터 생성
Elite_Four = {
    "일목": ["네이티오", "루주라", "야도란", "나시", "네이티오"],
    "독수": ["아리아도스", "도나리", "쏘콘", "질뻐기", "크로뱃"],
    "시바": ["카포에라", "시라소몬", "홍수몬", "롱스톤", "괴력몬"],
    "카렌": ["블래키", "라플레시아", "니로우", "팬텀", "헬가"],
}

Hidden_Elite = {"목호": ["갸라도스", "망나뇽", "리자몽", "프테라", "망나뇽", "망나뇽"]}

# 폰트
font = pygame.font.SysFont("malgungothic", 48)

# 로딩 화면 보여주기
show_loading_screen(screen, font, LOADING_SCREEN)

loading_screen = pygame.image.load(LOADING_SCREEN)

ENEMYS = os.path.join(ROOT, "Enemys")
CHARACTER = os.path.join(ROOT, "Character")
POKEMON = os.path.join(ROOT, "Pokemon")
# if not (os.path.isdir(ENEMYS)):
#     os.mkdir(ENEMYS)

#     # 캐릭터 이미지 생성
#     create_enemy_image(ENEMYS, Elite_Four, Hidden_Elite, version="골드")
#     # time.sleep(3)
# else:
#     # 캐릭터 이미지 생성성
#     create_enemy_image(ENEMYS, Elite_Four, Hidden_Elite, version="골드")
#     # time.sleep(3)

# if not (os.path.isdir(CHARACTER)):
#     os.mkdir(CHARACTER)

#     tts = TTS()
#     tts.tts("MBTI를 말해주세요!")

#     screen.fill((50, 150, 50))
#     game_ready = font.render("MBTI를 말해주세요!", True, (255, 255, 255))
#     game_ready_rect = game_ready.get_rect(
#         center=(screen.get_width() // 2, screen.get_height() // 2 + 50)
#     )
#     screen.blit(loading_screen, (0, 0))
#     screen.blit(game_ready, game_ready_rect)
#     pygame.display.update()

#     stt = STT()
#     prompt = stt.stt()

#     # 캐릭터 이미지 생성
#     create_character_image(CHARACTER, prompt)
#     # time.sleep(3)

#     pokemon_prompt = f"{prompt}와 어울리는 포켓몬 이름만줘 다른 대답 필요없어"

#     response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[{"role": "user", "content": pokemon_prompt}],
#         max_tokens=250,
#     )

#     pokemons = response.choices[0].message.content.strip().split("\n")

# else:
#     tts = TTS()
#     tts.tts("MBTI를 말해주세요!")

#     screen.fill((50, 150, 50))
#     game_ready = font.render("MBTI를 말해주세요!", True, (255, 255, 255))
#     game_ready_rect = game_ready.get_rect(
#         center=(screen.get_width() // 2, screen.get_height() // 2 + 50)
#     )
#     screen.blit(loading_screen, (0, 0))
#     screen.blit(game_ready, game_ready_rect)
#     pygame.display.update()

#     stt = STT()
#     prompt = stt.stt()

#     # 캐릭터 이미지 생성성
#     create_character_image(CHARACTER, prompt)
#     # time.sleep(3)

#     pokemon_prompt = f"{prompt}와 어울리는 포켓몬 이름만 작성해줘 다른 대답 필요없어"

#     response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[{"role": "user", "content": pokemon_prompt}],
#         max_tokens=250,
#     )

#     pokemons = response.choices[0].message.content.strip().split("\n")

# if not (os.path.isdir(POKEMON)):
#     os.mkdir(POKEMON)

#     create_pokemon_image(POKEMON, Elite_Four, Hidden_Elite, pokemons)
#     # time.sleep(3)
# else:
#     # 캐릭터 이미지 생성성
#     create_pokemon_image(POKEMON, Elite_Four, Hidden_Elite, pokemons)
#     # time.sleep(3)


# 게임 메인 화면 진입
screen.fill((50, 150, 50))
game_ready = font.render("게임 시작!", True, (255, 255, 255))
screen.blit(loading_screen, (0, 0))
screen.blit(game_ready, (220, 220))
pygame.display.update()
# time.sleep(3)


# 배경 이미지 불러오기
background = pygame.image.load(BACKGROUND)

# 내 캐릭터 이미지 불러오기
character_img = os.path.join(CHARACTER, "Me.png")
character = pygame.image.load(character_img)
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]  # 캐릭터의 가로 크기
character_hight = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = 0  # 화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
character_y_pos = (
    screen_height - character_hight
)  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로)

# 내 포켓몬 이미지 불러오기
my_pokemon_img = os.path.join(POKEMON, "Zygarde.png")
my_pokemon = pygame.image.load(my_pokemon_img)
my_pokemon_size = my_pokemon.get_rect().size  # 이미지의 크기를 구해옴
my_pokemon_width = my_pokemon_size[0]  # 캐릭터의 가로 크기
my_pokemon_hight = my_pokemon_size[1]  # 캐릭터의 세로 크기
my_pokemon_x_pos = 0  # 화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
my_pokemon_y_pos = (
    screen_height - my_pokemon_hight
)  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로)

# 적 캐릭터 이미지 불러오기
enemy_name = random.choice(list(Elite_Four.keys()))
enemy_img = os.path.join(ENEMYS, f"{enemy_name}.png")
enemy = pygame.image.load(enemy_img)
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구해옴
enemy_width = enemy_size[0]  # 캐릭터의 가로 크기
enemy_hight = enemy_size[1]  # 캐릭터의 세로 크기
enemy_x_pos = (
    screen_width - enemy_width
)  # 화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
enemy_y_pos = 0  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로)

# 적 포켓몬 이미지 불러오기기
enemy_pokemon_img = os.path.join(POKEMON, "Yveltal.png")
enemy_pokemon = pygame.image.load(enemy_pokemon_img)
enemy_pokemon_size = enemy_pokemon.get_rect().size  # 이미지의 크기를 구해옴
enemy_pokemon_width = enemy_pokemon_size[0]  # 캐릭터의 가로 크기
enemy_pokemon_hight = enemy_pokemon_size[1]  # 캐릭터의 세로 크기
enemy_pokemon_x_pos = (
    screen_width - enemy_pokemon_width
)  # 화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
enemy_pokemon_y_pos = 0  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로)

# FPS
clock = pygame.time.Clock()

# 이벤트 루프
running = True  # 게임이 진행중인가?
starting = True
while running:
    dt = clock.tick(60)  # 게임화면의 초당 프레임 수를 설정

    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창 닫기 버튼 누르면 종료
            running = False  # 게임이 진행중이 아님

    if character_x_pos + character_width > 0:
        character_x_pos -= 5

    if enemy_x_pos < screen_width:
        enemy_x_pos += 5

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    screen.blit(background, (0, 0))  # 배경 그리기

    if character_x_pos + character_width > 0:
        screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    else:
        screen.blit(my_pokemon, (my_pokemon_x_pos, my_pokemon_y_pos))

    if enemy_x_pos < screen_width:
        screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기
    else:
        screen.blit(enemy_pokemon, (enemy_pokemon_x_pos, enemy_pokemon_y_pos))

    pygame.display.update()  # 게임화면을 다시 그리기!

    if starting:
        tts = TTS()
        tts.tts("사천왕과 배틀에서 승리하세요!")
        starting = False

# pygame 종료
pygame.quit()
