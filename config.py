tgChannel = "-1001256512153"  # link to the channel in telegram
                     # or channel ID (for example: tgChannel = -1234567890987)
                     # (you can get channel ID here t.me/username_to_id_bot)
                     # you must add bot to this channel as an administrator
                     # don't forget to add bot to this channel as an administrator!
tgBotToken = "1868310671:AAEdyGU5-HfF2oPB7yTyCPEIEaZgEThLERc"  # your bot's token from t.me/BotFather
vkToken = "ef3dec346ac8d3bf090670aa78da8ead4393d75f466d2d5f19f2b7957e7dd9e15cb5ad8cadd3f85142120"  # your token from https://github.com/alcortazzo/vktgbot/wiki/How-to-get-personal-access-token
vkDomain = "ageofmagicgame"  # domain of vk channel (vk.com/>>>>aaaaaaaa<<<<)

tgLogChannel = ""  # link to another channel in telegram if you want to get bot's log message
                        # you can use the same bot as for the main task
                        # don't forget to add bot to this channel as an administrator!
tgBotForLogToken = ""   # set token here if you want vktgbot to use another bot for logging
                        # leave the variable empty if you want use first bot (tgBotToken) for logging 
                        # don't forget to add this bot to tgLogChannel as administrator 

reqVer = 5.131       # version of VK API (https://vk.com/dev/versions). used for wall.get method
reqCount = 1         # number of posts to send to telegram (2 - 100)
reqFilter = "owner"  # Filter to apply:
                     # "owner" — posts by the wall owner;
                     # "others" — posts by someone else;
                     # "all" — posts by the wall owner and others
                     # "postponed" — timed posts (only available for calls with an access_token)
                     # "suggests" — suggested posts on a community wall

singleStart = False  # if True bot will stop after  first pass through the loop 
timeSleep = 60 * 20  # waiting time between cycle passes
isPinned = False
skipAdsPosts = True  # set True if you want to skip sponsored posts
skipPostsWithCopyright = False

WHITELIST = []  # Words whitelist. Bot will repost posts only containing words in whitelist. Useful for hashtags
BLACKLIST = []  # Words blacklist. If a post contains a blacklisted word, the post will be skipped
# Example
# WHITELIST = ["#music", "new"]
# BLACKLIST = ["rap", "dubstep"]
# This configuration will keep posts only with music hashtag and word "new" excluding posts with words "rap" and "dubstep"

proxyEnable = False     # Set True if telegram is not available in your country
proxyLogin = "bot"      # Login for Socks5 proxy
proxyPass = "12345"     # Password for Socks5 proxy
proxyIp = "myproxy.com" # Socks5 proxy ip
proxyPort = "1234"      # Socks5 proxy port

logFolderName = "logs"  # name of the folder in which the log files will be stored
logFileName = "dev.log"
