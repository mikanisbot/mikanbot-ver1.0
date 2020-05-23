from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

若干のバグは残ってるけどいいよね
その時直せば
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']



@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_message(message):
    if message.author.bot:
        # もし、送信者がbotなら無視する
        return
    GLOBAL_CH_NAME = "Mikanglobal" # グローバルチャットのチャンネル名

    if message.channel.name == GLOBAL_CH_NAME:
        # hoge-globalの名前をもつチャンネルに投稿されたので、メッセージを転送する

        await message.delete() # 元のメッセージは削除しておく

        channels = client.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
        # channelsはbotの取得できるチャンネルのイテレーター
        # global_channelsは hoge-global の名前を持つチャンネルのリスト

        embed = discord.Embed(title=GLOBAL_CH_NAME,
            description=message.content, color=0x00bfff)

        embed.set_author(name=message.author.display_name, 
            icon_url=message.author.avatar_url_as(format="png"))
        embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
            icon_url=message.guild.icon_url_as(format="png"))
        # Embedインスタンスを生成、投稿者、投稿場所などの設定

        for channel in global_channels:
            # メッセージを埋め込み形式で転送
            await channel.send(embed=embed)
@bot.event
async def on_ready():
    # discordのあれ
    prefix = "(サポートサーバー GdfkgGF8をプレイ中)"
    await commands.change_presence(activity=discord.Game(name=f"(Python)ヘルプは『{prefix}.help』だ"))
    # discordのあれ
    
    @bot.command(name="ログアウト")
@commands.is_owner()
async def restart(ctx):
    if ctx.message.author.id ==713583564138217514 :  # このidのとこは自身のIDに変更してね
        await ctx.send(embed=discord.Embed(title="シャットダウン！", description="終了する！(Python版)", color=color))
        await bot.logout()
    else:
        color = random.randint(0x000000, 0xffffff)
        await ctx.send(embed=discord.Embed(title="違う！", description="お前……。", color=color))
bot.run(token)
 
