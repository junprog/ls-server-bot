# インストールした discord.py を読み込む
import discord
import random

TOKEN = "" # ここにアクセストークンを記述(str)

# 接続に必要なオブジェクトを生成
client = discord.Client()

sanhok_list = ['ふぐかMongnaiどっち選ぶ？', 'Tat mok', 'Bhanとその周りの集落でリユニオン作戦！', 'Tambangとか物資薄いしBootcampでいいよ',
               'Quarry', 'Cave', 'イケメンならCamp Alpha、違かったらHa Tinh', 'Na kham', 'Docks', 'Camp Bravo', 'Khao', 'Ruins', 
               'こっきくんはこっきビーチで(Ban Tai)、ほかはCamp Charlie', 'Lakawiとか物資薄いしParadise Resortでいいよ', 'Ha Tinh',
               'さんめで(Sahmee)', 'Camp Charlie', 'Kam pong', 'Bootcamp', 'Paradise Resort', 'Pai Nan']

erangel_list = ['Zharki', 'Severny', 'Yasnaya Polyana', 'Kameshki', 'Georgopol', 'Pochinki', 'Rozhok', 'School or 6連マンション',
                'Lipovka', 'Mansion', 'Prison', 'Mylta', 'Mylta power', 'Primorsk', 'Novorepnoye', 'Military Base']

miramar_list = ['Alcantara(左上)', 'La Cobreria(左上)', 'El Pozo', 'Monte Nuevo', 'Valle del Mar(左下)', '左下の島', 'Chumacera', 'Los Leones',
                'Pecado', 'San Martin', 'Minas Generales', 'Impara', 'Torre Ahumada(右上)', 'Cruz del Valle(右上)', 'El Azahar', 'Campo Militar',
                'Tierra Bronca', 'Puerto Paraiso']

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print(client.user.name)
    #print(client.user.id)
    print('ログインしましたぁ～')
    print('------')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 返信処理
    if message.content == '/sanhok':
        word = str(random.choices(sanhok_list, k=1, weights=[0.3, 1, 0.3, 2, 1, 1, 2, 0.6, 1, 1, 3, 1, 5, 5, 5, 3, 5, 4, 3, 5, 4]))
        await message.channel.send(word.strip("[""]""'"))

    if message.content == '/erangel':
        word = str(random.choices(erangel_list, k=1, weights=[1, 5, 5, 1, 5, 4, 5, 5, 3, 2, 2, 5, 3, 5, 4, 4]))
        await message.channel.send(word.strip("[""]""'"))

    if message.content == '/miramar':
        word = str(random.choices(miramar_list, k=1, weights=[0.5, 1, 3, 3, 1, 0.5, 4, 5, 2, 4, 1, 4, 1, 2, 3, 1, 2, 1]))
        await message.channel.send(word.strip("[""]""'"))

    if message.content == 'どもでーす':
        m = message.author.name + "さん、どもでーす"
        await message.channel.send(m)
        
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
