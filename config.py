#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiAFKBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiAFKBot/blob/master/LICENSE >
#
# All rights reserved.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Database to save your chats and stats... Get MongoDB:-  https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb#4.-youll-see-a-deploy-cloud-database-option.-please-select-shared-hosting-under-free-plan-here
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb://arya:arya@ac-4zotjcs-shard-00-00.77ytvjf.mongodb.net:27017,ac-4zotjcs-shard-00-01.77ytvjf.mongodb.net:27017,ac-4zotjcs-shard-00-02.77ytvjf.mongodb.net:27017/?ssl=true&replicaSet=atlas-9nxz2h-shard-0&authSource=admin&retryWrites=true&w=majority")

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("SUDO_USER", "").split())
)  # Input type must be interger
