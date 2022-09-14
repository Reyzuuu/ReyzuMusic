HELP_1 = """✅**<u>Admin Commands :</u>**

**c** stands for channel play.

/pause or /cpause - Jeda musik yang diputar.
/resume or /cresume - Lanjutkan musik yang dijeda.
/mute or /cmute - Bisukan musik yang diputar.
/unmute or /cunmute - Suarakan musik yang dibisukan.
/skip or /cskip - Lewati musik yang sedang diputar.
/stop or /cstop - Hentikan pemutaran musik.
/shuffle or /cshuffle - Secara acak mengacak daftar putar yang antri.
/seek or /cseek - Teruskan mencari musik sesuai durasi.
/seekback or /cseekback - Kembali mencari musik sesuai durasi.
/restart - Mulai ulang bot untuk grup Anda.


✅<u>**Specific Skip :**</u>
/skip or /cskip [Nomor (contoh : 3)] 
    - Melewati musik ke nomor antrian yang ditentukan. Contoh : /skip 3 akan melewatkan musik ke musik antrian ketiga dan akan mengabaikan musik 1 dan 2 dalam antrian.

✅<u>**Loop Play :**</u>
/loop or /cloop [enable/disable] or [Angka antara 1-10] 
    - Saat diaktifkan, bot memutar musik yang sedang diputar menjadi 1-10 kali pada obrolan suara.

✅<u>**Auth Users :**</u>
Pengguna Auth dapat menggunakan perintah admin tanpa hak admin di obrolan Anda.

/auth [Username] - Tambahkan pengguna ke daftar AUTH grup.
/unauth [Username] - Hapus pengguna dari daftar AUTH grup.
/authusers - Periksa daftar AUTH grup."""


HELP_2 = """✅<u>**Play Commands :**</u>

Perintah yang tersedia = play , vplay , cplay

Perintah ForcePlay = playforce , vplayforce , cplayforce

**c** singkatan dari pemutaran saluran.
**v** singkatan dari pemutaran video.
**force** singkatan dari force play.

/play or /vplay or /cplay  - Bot akan mulai memainkan kueri yang Anda berikan di obrolan suara atau Streaming tautan langsung di obrolan suara.

/playforce or /vplayforce or /cplayforce -  **Force Play** menghentikan trek yang sedang diputar pada obrolan suara dan mulai memutar trek yang dicari secara instan tanpa mengganggu/mengosongkan antrean.
/channelplay [Chat username or id] or [Disable] - Hubungkan channel ke grup dan streaming musik di obrolan suara channel dari grup Anda.


✅**<u>Bot's Server Playlists :</u>**
/playlist  - Periksa Daftar Putar tersimpan Anda di server.
/deleteplaylist - Delete any saved music in your playlist
/play  - Start playing Your Saved Playlist from Servers."""


HELP_3 = """✅<u>**Bot Commands:**</u>

/stats - Get Top 10 Tracks Global Stats, Top 10 Users of bot, Top 10 Chats on bot, Top 10 Played in a chat etc etc.

/sudolist - Check Sudo Users of Reyzu Music Bot

/lyrics [Music Name] - Searches Lyrics for the particular Music on web.

/song [Track Name] or [YT Link] - Download any track from youtube in mp3 or mp4 formats.

/player -  Get a interactive Playing Panel.

**c** stands for channel play.

/queue or /cqueue- Check Queue List of Music."""

HELP_4 = """✅<u>**Extra  Commands:**</u>
/start - Start the Music Bot.
/help  - Get Commands Helper Menu with detailed explanations of commands.
/ping- Ping the Bot and check Ram, Cpu etc stats of Bot.

✅<u>**Group Settings:**</u>
/settings - Get a complete group's settings with inline buttons

🔗 **Options in Settings:**

1️⃣ You can set **Audio Quality** you want to stream on voice chat.

2️⃣ You can set **Video Quality** you want to stream on voice chat.

3️⃣ **Auth Users**:- You can change admin commands mode from here to everyone or admins only. If everyone, anyone present in you group will be able to use admin commands(like /skip, /stop etc)

4️⃣ **Clean Mode:** When enabled deletes the bot's messages after 5 mins from your group to make sure your chat remains clean and good.

5️⃣ **Command Clean** : When activated, Bot will delete its executed commands (/play, /pause, /shuffle, /stop etc) immediately.

6️⃣ **Play Settings:**

/playmode - Get a complete play settings panel with buttons where you can set your group's play settings. 

<u>Options in playmode:</u>

1️⃣ **Search Mode** [Direct or Inline] - Changes your search mode while you give /play mode. 

2️⃣ **Admin Commands** [Everyone or Admins] - If everyone, anyone present in you group will be able to use admin commands(like /skip, /stop etc)

3️⃣ **Play Type** [Everyone or Admins] - If admins, only admins present in group can play music on voice chat."""

HELP_5 = """🔰**<u>ADD & REMOVE SUDO USERS :</u>**
/addsudo [Username or Reply to a user]
/delsudo [Username or Reply to a user]

🛃**<u>HEROKU:</u>**
/usage - Dyno Usage.

🌐**<u>CONFIG VARS:</u>**
/get_var - Get a config var from Heroku or .env.
/del_var - Delete any var on Heroku or .env.
/set_var [Var Name] [Value] - Set a Var or Update a Var on heroku or .env. Seperate Var and its Value with a space.

🤖**<u>BOT COMMANDS:</u>**
/reboot - Reboot your Bot. 
/update - Update Bot.
/speedtest - Check server speeds
/maintenance [enable / disable] 
/logger [enable / disable] - Bot logs the searched queries in logger group.
/get_log [Number of Lines] - Get log of your bot from heroku or vps. Works for both.
/autoend [enable|disable] - Enable Auto stream end after 3 mins if no one is listening.

📈**<u>STATS COMMANDS:</u>**
/activevoice - Check active voice chats on bot.
/activevideo - Check active video calls on bot.
/stats - Check Bots Stats

⚠️**<u>BLACKLIST CHAT FUNCTION:</u>**
/blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
/whitelistchat [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot
/blacklistedchat - Check all blacklisted chats.

👤**<u>BLOCKED FUNCTION:</u>**
/block [Username or Reply to a user] - Prevents a user from using bot commands.
/unblock [Username or Reply to a user] - Remove a user from Bot's Blocked List.
/blockedusers - Check blocked Users Lists

👤**<u>GBAN FUNCTION:</u>**
/gban [Username or Reply to a user] - Gban a user from bot's served chat and stop him from using your bot.
/ungban [Username or Reply to a user] - Remove a user from Bot's gbanned List and allow him for using your bot
/gbannedusers - Check Gbanned Users Lists

🎥**<u>VIDEOCALLS FUNCTION:</u>**
/set_video_limit [Number of Chats] - Set a maximum Number of Chats allowed for Video Calls at a time. Default to 3 chats.
/videomode [download|m3u8] - If download mode is enabled, Bot will download videos instead of playing them in M3u8 form. ByDefault to M3u8. You can use download mode when any query doesnt plays in m3u8 mode.

⚡️**<u>PRIVATE BOT FUNCTION:</u>**
/authorize [CHAT_ID] - Allow a chat for using your bot.
/unauthorize [CHAT_ID] - Disallow a chat from using your bot.
/authorized - Check all allowed chats of your bot.

🌐**<u>BROADCAST FUNCTION:</u>**
/broadcast [Message or Reply to a Message] - Broadcast any message to Bot's Served Chats.

<u>options for broadcast:</u>
**-pin** : This will pin your message 
**-pinloud** : This will pin your message with loud notification
**-user** : This will broadcast your message to the users who have started your bot.
**-assistant** : This will broadcast your message from assistant account of your bot.
**-nobot** : This will force your bot to not broadcast message

**Example:** `/broadcast -user -assistant -pin Hello Testing`

"""
