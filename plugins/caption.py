from pyrogram import Client,filters
ccaption = """\n\n<b><i>⚜️ To Join Click here
⭐️ @honeybeemovies
⭐️ @AmazonPrime_Orginal ✅
⭐️ @honeybeemoviesgroup 
⭐️ @MalluFlix 🧲

    🅷🅾️🅽🅴🆈 🅱️🅴🅴 🅼🅾️🆅🅸🅴🆂 </b></i>"""

ccaption2 = """\n<b><i>⚜️ Join    @h4hbm</b></i>"""

@Client.on_message(filters.group, group=1)
async def caption2(client, message):
    grp=message.chat.id
    if grp==-1001574333947:
        ogcap=message.caption
        if ogcap==None:
            newcap=ccaption
        else:
            newcap="<b><i>"+str(ogcap)+"</b></i>"+ccaption
        await message.copy(message.chat.id, caption=newcap)
    else:
        ogcap=message.caption
        if ogcap==None:
            newcap="."+ccaption2
        else:
            newcap="<b><i>"+str(ogcap)+"\n</b></i>"+ccaption2
        await message.copy(message.chat.id, caption=newcap)
