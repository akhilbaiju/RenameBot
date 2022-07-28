from pyrogram import Client,filters
ccaption = """\n\n<b><i>⚜️ To Join Click here
⭐️ @honeybeemovies
⭐️ @AmazonPrime_Orginal ✅
⭐️ @honeybeemoviesgroup 
⭐️ @MalluFlix 🧲

    🅷🅾️🅽🅴🆈 🅱️🅴🅴 🅼🅾️🆅🅸🅴🆂 </b></i>"""

ccaption2 = """\n<b><i>⚜️ Join    @h4hbm</b></i>"""

@Client.on_message(filters.group([-1001644864422]), group=1)
async def caption2(client, message):
    ogcap=message.caption
    if ogcap==None:
        newcap=ccaption2
    else:
        newcap="<b><i>"+str(ogcap)+"</b></i>"+ccaption2
    await message.copy(message.chat.id, caption=newcap)
    
@Client.on_message(filters.group, group=1)
async def caption2(client, message):
    ogcap=message.caption
    if ogcap==None:
        newcap=ccaption
    else:
        newcap="<b><i>"+str(ogcap)+"</b></i>"+ccaption
    await message.copy(message.chat.id, caption=newcap)
