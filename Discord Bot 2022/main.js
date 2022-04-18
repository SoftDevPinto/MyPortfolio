const Discord = require('discord.js')

const client = new Discord.Client({ 
    intents: [
        "GUILDS", 
        "GUILD_MESSAGES"
    ] 
})

client.on("ready", () => {
    console.log("Garrys online fuckers")
})

client.on("messegeCreate", (message) => {
    if (message.content == "hi"){
        message.reply("hello world!")
    }
})


client.login("OTY1NTY2NzkzMDM0ODkxMzU2.Yl1EJg.RWgpNB4eoyXW_seyuQw8n9ExajM");
