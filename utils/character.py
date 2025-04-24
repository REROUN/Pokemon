import os
import sys
import openai
import requests
from PIL import Image
from io import BytesIO
from glob import glob
from dotenv import load_dotenv


def create_enemy_image(ENEMYS, Elite_Four, Hidden_Elite, version):
    data = glob(os.path.join(ENEMYS, "*.png"))
    if not (data):
        load_dotenv()

        api_key = os.getenv("OPENAI_API_KEY")

        client = openai.Client(api_key=api_key)

        for elite in Elite_Four.keys():
            prompt = f"""
            포켓몬스터 {version}버전 게임에 나오는 사천왕 중 {elite}라는 캐릭터를
            다른 부가적인 것 없이 캐릭터만 있으면서 전신이 다 나와있는 배경 없는 도트 이미지로 
            생성해줘
            """

            response = client.images.generate(
                model="dall-e-3", prompt=prompt, n=1, size="1024x1024"
            )

            image_url = response.data[0].url
            img = Image.open(BytesIO(requests.get(image_url).content))
            img_resized = img.resize((250, 250), Image.NEAREST)
            img_resized.save(os.path.join(ENEMYS, f"{elite}.png"))

        prompt = f"""
        포켓몬스터 {version}버전 게임에 나오는 {list(Hidden_Elite.keys())[0]}라는 캐릭터를 원작과 다르게 변경하여 다른 부가적인 것 없이 캐릭터만 있으면서 전신이 다 나와있는 배경 없는 도트 이미지로 생성해줘
        """

        response = client.images.generate(
            model="dall-e-3", prompt=prompt, n=1, size="1024x1024"
        )

        image_url = response.data[0].url
        img = Image.open(BytesIO(requests.get(image_url).content))
        img_resized = img.resize((250, 250), Image.NEAREST)
        img_resized.save(os.path.join(ENEMYS, f"{list(Hidden_Elite.keys())[0]}.png"))


def create_character_image(CHARACTER, prompt):
    data = glob(os.path.join(CHARACTER, "*.png"))
    if not (data):
        load_dotenv()

        api_key = os.getenv("OPENAI_API_KEY")

        client = openai.Client(api_key=api_key)

        prompt = f"""{prompt} 성격을 가지고 뒤돌아서 허리까지만 나오는 도트로된 사람 이미지를 배경 없이 생성해줘"""

        response = client.images.generate(
            model="dall-e-3", prompt=prompt, n=1, size="1024x1024"
        )

        image_url = response.data[0].url
        img = Image.open(BytesIO(requests.get(image_url).content))
        img_resized = img.resize((250, 250), Image.NEAREST)
        img_resized.save(os.path.join(CHARACTER, "Me.png"))


def create_pokemon_image(POKEMON, Elite_Four, Hidden_Elite, My_Pokemon):
    data = glob(os.path.join(POKEMON, "*.png"))
    if not (data):
        load_dotenv()

        api_key = os.getenv("OPENAI_API_KEY")

        client = openai.Client(api_key=api_key)

        for pokemon in set(sum(list(Elite_Four.values()), [])):
            prompt = f"""포켓몬스터에 나오는 {pokemon}을 도트 이미지로 생성해줘. 단, 배경이 없어야하고 포켓몬스터 이외에 다른건 아무것도 그리지 말아줘"""

            response = client.images.generate(
                model="dall-e-3", prompt=prompt, n=1, size="1024x1024"
            )

            image_url = response.data[0].url
            img = Image.open(BytesIO(requests.get(image_url).content))
            img_resized = img.resize((250, 250), Image.NEAREST)
            img_resized.save(os.path.join(POKEMON, f"{pokemon}.png"))

        for pokemon in set(sum(list(Hidden_Elite.values()), [])):
            prompt = f"""포켓몬스터에 나오는 {pokemon}을 도트 이미지로 생성해줘. 단, 배경이 없어야하고 포켓몬스터 이외에 다른건 아무것도 그리지 말아줘"""

            response = client.images.generate(
                model="dall-e-3", prompt=prompt, n=1, size="1024x1024"
            )

            image_url = response.data[0].url
            img = Image.open(BytesIO(requests.get(image_url).content))
            img_resized = img.resize((250, 250), Image.NEAREST)
            img_resized.save(os.path.join(POKEMON, f"{pokemon}.png"))

        for pokemon in list(My_Pokemon):
            prompt = f"""포켓몬스터에 나오는 {pokemon}을 뒤돌아 있는 모습에 도트 이미지로 생성해줘. 단, 배경이 없어야하고 포켓몬스터 이외에 다른건 아무것도 그리지 말아줘"""

            response = client.images.generate(
                model="dall-e-3", prompt=prompt, n=1, size="1024x1024"
            )

            image_url = response.data[0].url
            img = Image.open(BytesIO(requests.get(image_url).content))
            img_resized = img.resize((250, 250), Image.NEAREST)
            img_resized.save(os.path.join(POKEMON, f"{pokemon}.png"))
