from pyrogram import Client,filters
ccaption = """\n\n<b><i>⚜️ To Join Click here
⭐️ @honeybeemovies
⭐️ @AmazonPrime_Orginal ✅
⭐️ @honeybeemoviesgroup 
⭐️ @MalluFlix 🧲

    🅷🅾️🅽🅴🆈 🅱️🅴🅴 🅼🅾️🆅🅸🅴🆂 </b></i>"""

@Client.on_message(filters.group, group=1)
async def caption2(client, message):
    ogcap=message.caption
    if ogcap==None:
        newcap=ccaption
    else:
        newcap="<b><i>"+str(ogcap)+"</b></i>"+ccaption
    await message.copy(message.chat.id, caption=newcap)
