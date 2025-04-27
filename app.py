import re
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
time.sleep(3)

loading_screen = pygame.image.load(LOADING_SCREEN)

ENEMYS = os.path.join(ROOT, "Enemys")
CHARACTER = os.path.join(ROOT, "Character")
POKEMON = os.path.join(ROOT, "Pokemon")
HP = os.path.join(ROOT, "HP")
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
time.sleep(3)


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

# 내 포켓몬 체력바
my_hp_img = os.path.join(HP, "my_hp.png")
my_hp = pygame.image.load(my_hp_img)
my_hp_size = my_hp.get_rect().size
my_hp_width = my_hp_size[0]
my_hp_hight = my_hp_size[1]
my_hp_x_pos = 300
my_hp_y_pos = 400

# 상대대 포켓몬 체력바
enemy_hp_img = os.path.join(HP, "enemy_hp.png")
enemy_hp = pygame.image.load(enemy_hp_img)
enemy_hp_size = enemy_hp.get_rect().size
enemy_hp_width = enemy_hp_size[0]
enemy_hp_hight = enemy_hp_size[1]
enemy_hp_x_pos = 50
enemy_hp_y_pos = 50

# FPS
clock = pygame.time.Clock()

# STT
stt = STT()
prompt1 = "가라 지가르데!!"
prompt2 = "가라 이벨타르!!"

# TTS
tts = TTS()

# 이벤트 루프
running = True  # 게임이 진행중인가?
starting = True
battle = False
enemy_attack = False
gpt_response_pending = False
gpt_response_text = ""
battle_started = False
zygarde_hp = 216
yveltal_hp = 126
messages = [
    {
        "role": "system",
        "content": f"""
        너는 포켓몬 배틀 해설자야.
        처음 소환하면 배틀이 시작되는 거고 내가 포켓몬 명령과 관련된 프롬프트를 넣어주면 그때 게임이 시작되며 턴이 진행되는거야.
        처음 포켓몬을 소환하였을 때 상세한 능력치를 전부 말해줄 필요 없이 간략하게 배틀이 시작되었다고만 출력해줘.
        프롬프트 한번에 한턴만 진행되는거니까 턴을 마음대로 진행하지 말고 다음 프롬프트가 들어올 때까지 기다려줘.
        내 포켓몬과 관련된 프롬프트가 들어오면 내 턴에 대한 상황만 간략하게 해설하고 상대의 포켓몬과 관련된 프롬프트가 들어오면 상대 턴에 대한 상황만 간략하게 해설해줘.
        그리고 매 턴마다 공격 데미지가 몇 들어갔는지 알려주고 체력 상황을 알려줘.
        매 턴 상대 포켓몬과 내 포켓몬의 체력은 다음과 같이 표시해줘:
            "상대 포켓몬 이름 HP - {yveltal_hp}"
            "내 포켓몬 이름 HP - {zygarde_hp}"
        그리고 만약 나의 포켓몬 체력이 0 또는 0보다 아래이면 체력 상황을 알려주고 이후 '패배하였습니다.'라는 결과만 출력해줘.
        상대 포켓몬의 체력이 0 또는 0 아래이면 체력 상황을 알려주고 이후 '승리하였습니다.'라는 결과만 출력해줘.
        또한 결과가 나왔다면 이후에는 결과만 출력해줘.
        """,
    }
]
font = pygame.font.SysFont("malgungothic", 13)

while running:
    dt = clock.tick(60)  # 게임화면의 초당 프레임 수를 설정

    screen.blit(background, (0, 0))  # 배경 그리기

    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창 닫기 버튼 누르면 종료
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_SPACE:
                prompt1 = "지가르데 천살!!"  # stt.stt()
                messages.append({"role": "user", "content": prompt1})
                response = client.chat.completions.create(
                    model="gpt-4o", messages=messages
                )
                gpt_response_text = response.choices[0].message.content
                tts.tts(gpt_response_text)
                # print(gpt_response_text)
                messages.append({"role": "user", "content": gpt_response_text})
                match = re.search(r"이벨타르\s*HP\s*-\s*([0-9]+)", gpt_response_text)
                if match:
                    yveltal_hp = int(match.group(1))

                enemy_attack = True

    # y = 430
    # for line in gpt_response_text.split("\n"):
    #     chat_box = font.render(line, True, (0, 0, 0))
    #     screen.blit(chat_box, (350, y))
    #     y += 30

    result_match = re.search(r"승리하였습니다.", gpt_response_text)
    if result_match:
        # tts.tts("상대를 쓰러뜨렸다!")
        print("상대를 쓰러뜨렸다!")
        time.sleep(5)
        pygame.quit()

    if enemy_attack:
        prompt2 = "이벨타르 공격해!!"
        messages.append({"role": "user", "content": prompt2})
        response = client.chat.completions.create(model="gpt-4o", messages=messages)
        gpt_response_text = response.choices[0].message.content
        tts.tts(gpt_response_text)
        # print(gpt_response_text)
        messages.append({"role": "user", "content": gpt_response_text})

        match = re.search(r"지가르데\s*HP\s*-\s*([0-9]+)", gpt_response_text)
        if match:
            zygarde_hp = int(match.group(1))

        enemy_attack = False

    result_match = re.search(r"패배하였습니다.", gpt_response_text)
    if result_match:
        # tts.tts("지가르데가 쓰러졌다! 눈앞이 캄캄 해졌다...")
        print("지가르데가 쓰러졌다! 눈앞이 캄캄 해졌다...")
        time.sleep(5)
        pygame.quit()

    if battle and not gpt_response_pending:
        gpt_response_pending = True
        prompt3 = f"""
        나는 지가르데를 소환했다.
        상대는 이벨타르를 소환.
        지가르데의 능력치
            - HP: {zygarde_hp}
            - 공격: 100
            - 방어: 121
            - 특수 공격: 91
            - 특수 방어: 95
            - 스피드: 85
        이벨타르의 능력치
            - HP: {yveltal_hp}
            - 공격: 131
            - 방어: 95
            - 특수 공격: 131
            - 특수 방어: 98
            - 스피드: 99
        """
        messages.append(
            {
                "role": "user",
                "content": prompt3,
            },
        )
        response = client.chat.completions.create(model="gpt-4o", messages=messages)
        gpt_response_text = response.choices[0].message.content.strip()
        tts.tts(gpt_response_text)
        # print(gpt_response_text)
        messages.append(
            {
                "role": "user",
                "content": gpt_response_text,
            },
        )

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

    if character_x_pos + character_width > 0:
        screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    else:
        screen.blit(my_pokemon, (my_pokemon_x_pos, my_pokemon_y_pos))  # 내 포켓몬
        # 내 포켓몬 체력바
        for i in range(int((zygarde_hp / 216) * 100)):
            screen.blit(my_hp, (my_hp_x_pos + (i * my_hp_width), my_hp_y_pos))

    if enemy_x_pos < screen_width:
        screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 상대 그리기
    else:
        screen.blit(
            enemy_pokemon, (enemy_pokemon_x_pos, enemy_pokemon_y_pos)
        )  # 상대 포켓몬
        # 상대 포켓몬 체력바
        for i in range(int((yveltal_hp / 126) * 100)):
            screen.blit(
                enemy_hp, (enemy_hp_x_pos + (i * enemy_hp_width), enemy_hp_y_pos)
            )

    if (character_x_pos + character_width <= 0) and (enemy_x_pos >= screen_width):
        battle = True

    pygame.display.update()  # 게임화면을 다시 그리기!

    if starting:
        tts = TTS()
        tts.tts("사천왕과 배틀에서 승리하세요!")
        starting = False


# pygame 종료
pygame.quit()
