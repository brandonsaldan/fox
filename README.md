# KitsuneDiscord

A social media username scraper made for use as a Discord bot.

**Installation on Windows and macOS**
--------------

1. Download this project as a .zip
2. Unzip to a directory of your choice
3. Install requirements with `pip3 install -r requirements.txt`
4. Get bot token from Discord
5. Replace bot.run with your token
6. `cd` to the directory you installed Kitsune to
7. run `python KitsuneDiscord.py`

**Usage**
--------------

KitsuneDiscord's default prefix is `%`. The correct syntax is `%kitsune (social media) (username)`

If done correctly, KitsuneDiscord will instantly check if the provided username is taken.

On certain social medias, for example, Instagram, if a user gets banned or deactivates their account, the username they had will still show up as available, but will not be able to be set as a username.

I am not responsible for any damage or unwanted consequences this application may cause. By using this application you assume complete responsibility.

**Batch Usage**
--------------

To use KitsuneDiscord's batch function, first, create a .txt containing the usernames you wish to check for. Make sure to only put one username per line. Doing anything else may result in the bot not working as intended.

Send the .txt file through Discord. Right click the download button and click `Copy Link`.

Now you are able to run `%batch (social media) (link you just copied)`

If done correctly, KitsuneDiscord will automatically go through the list and check if each username is available. This command is handy if you want to check a larger number of usernames but don't want to check them each individually using `%kitsune`.

**KitsuneDiscord currently supports:**
--------------

- Instagram

- Twitter

- Reddit

- SoundCloud

**Credits**
--------------

4201337

exofeel

clemente

padraig

brandonsaldan
