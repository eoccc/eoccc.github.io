# Servers

Servers are a large part of Mindustry in that they offer the ability to play the game with other people. There are two main types of servers; dedicated servers and local LAN servers.

## Dedicated Servers

Dedicated servers are standalone, headless versions of the game that are focused only on providing a means for people to play Multiplayer. They are usually run on a computer as a separate program rather than in-game, and are operated from the terminal. These are usually stronger than a local LAN server as they have more resources available to them to support more than two or three players, and can be run 24/7. They are also more versatile and powerful in that they have many commands to provide the administrator with more control over it, and they can easily be modded to fit the administrator's needs.

You can connect to one using the "Join Game" button under the "Play" menu. Unlike local LAN servers, you will have to enter the host's IP address and port. Also unlike local LAN servers, once you add a server, it will automatically show up on your server list when you open it, and the game will automatically check the server's status.

To establish a dedicated server, a dedicated Linux or Windows machine is **highly** recommended.

- If you haven't already, install Java.

- Download the desired server release from [itch.io](https://anuke.itch.io/mindustry) or [Github releases](https://github.com/Anuken/Mindustry/releases). The filename should be `server.jar` or `server-release.jar`, although if you are on Windows it may only show as `server` or `server-release`.

- Move the server file to your desired folder. It is recommended to place it in a new directory on your desktop.

- Open a new terminal window(CMD if you are on windows). Use the command "[cd](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands/)" to navigate into the directory you placed the server file in, ex `cd Desktop` then `cd Server`. Run `java -jar [server].jar`, replacing [server] with the name of your server file.

- Your server should start. Type `help` for a list of all console commands. If you get a message similar to "Unable to access file server.jar" you are likely in the wrong directory.

- Start hosting a map with the command `host  [mode]`.

- If you are using Windows to run your server, use your favorite search engine to look up how to add rules to your Windows Firewall, as it blocks the necessary port most of the time. Make sure to allow **port 6567 TCP and UDP**.

- To close the server, either close the terminal window or press Ctrl+C on the terminal window.

Unless you have already enabled port forwarding, your dedicated server can only be connected to by clients within your local network. If you want to make your server globally available, read below.

### What is an IP and how do I find out what mine is?

In simplified terms, an IP address is a number that identifies your computer on the internet. You can connect to someone's Mindustry server if you know their IP address. There are two types; a **public** and a **local** address.

- For a **local IP**, when for example you would like to play with a friend on the same network as yours, each device has its own way of showing it. You can Google how to do it for your device, e.g. "find local ip on Mac".

- For a **public IP**, you can simply Google "what is my ip".

### Running A Dedicated Server At Home

Most of the time, this is what you should remember; **never share your public IP with the public if you're hosting from your home, unless you acknowledge the implications of doing so!** Your public IP is tied to your household, and if it falls into the wrong hands, and when put into the wrong hands, can open up your network to vulnerabilities and dangers. **Exercise caution, do your research, and use a VPN or webhost if possible.**

It is also recommended and that you use a domain name or DNS service to mask your IP for public servers for ease of use, or even better, use a cloud service e.g. Amazon AWS or a dedicated server/VM from a hosting provider such as Linode or DigitalOcean, which is much safer. **Do your research**, and determine which option best fits your needs.

- Find the make/model of your router. This is usually on a sticker on the bottom or back of the router.

- Use your favorite search engine to search "port forward ASUS RT-ACRH17" and use the guide to foward **port 6567 TCP and UDP**. These instructions are different for every router, so be sure to read your guide thoroughly!

- You can use a service such as [You Get Signal](https://www.yougetsignal.com/tools/open-ports/) to check if you have done your portforwarding correctly.

## Local LAN & Steam Servers

A local LAN or Steam server is a server that is built into the game, and can be started using the "Host Multiplayer Game" button in the in-game menu. It is meant to be simple and straightforward, for sessions between a few players under a LAN network (aka in your household's WiFi network). It is not really meant for several players, as it takes more and more resources from your device to be able to use it that way; for that you will need a dedicated server mentioned above. It can only run when the game is open, and is immediately terminated when it is closed.

You can connect to one using the "Join Game" button under the "Play" menu. Unlike dedicated servers, your device will automatically find the host device and it will ususally appear in the server list without you having to enter the host's IP address in.

## Dedicated Server Commands

- `help [command]`: *Display the command list, or get help for a specific command.*

- `version`: *Displays server version info.*

- `exit`: *Exit the server application.*

- `stop`: *Stop hosting the server.*

- `host [mapname] [mode]`: *Open the server. Will default to survival and a random map if not specified.*

- `maps [all/custom/default]`: *Display available maps. Displays only custom maps by default.*

- `reloadassets`: *Reload all content/patch asset files from disk.*

- `reloadmaps`: *Reload all maps from disk.*

- `status`: *Display server status.*

- `mods`: *Display all loaded mods.*

- `mod `: *Display information about a loaded plugin.*

- `js `: *Run arbitrary Javascript.*

- `say `: *Send a message to all players.*

- `pause `: *Pause or unpause the game.*

- `rules [remove/add] [name] [value...]`: *List, remove or add global rules. These will apply regardless of map.*

- `dumpsettings`: *Print every settings value. Useful for debugging.*

- `fillitems [team]`: *Fill the core with items.*

- `playerlimit [off/somenumber]`: *Set the server player limit.*

- `config [name] [value...]`: *Configure server settings.*

- `subnet-ban [add/remove] [address]`: *Ban a subnet. This simply rejects all connections with IPs starting with some string.*

- `name-ban [add/remove/clear] [regex]`: *Ban a name by case-insensitive regex.*

- `whitelist [add/remove] [ID]`: *Add/remove players from the whitelist using their ID.*

- `shuffle [none/all/custom/builtin]`: *Set map shuffling mode.*

- `nextmap `: *Set the next map to be played after a game-over. Overrides shuffling.*

- `kick `: *Kick a person by name.*

- `ban  `: *Ban a person.*

- `bans`: *List all banned IPs and IDs.*

- `unban `: *Completely unban a person by IP or ID.*

- `pardon `: *Pardons a votekicked player by ID and allows them to join again.*

- `admin  `: *Make an online user admin*

- `admins`: *List all admins.*

- `players`: *List all players currently in game.*

- `runwave`: *Trigger the next wave.*

- `loadautosave`: *Loads the last auto-save.*

- `load `: *Load a save from a slot.*

- `save  [embedAssets]`: *Save game state to a slot.*

- `saves`: *List all saves in the save directory.*

- `gameover`: *Force a game over.*

- `info `: *Find player info(s). Can optionally check for all names or IPs a player has had.*

- `search `: *Search players who have used part of a name.*

- `gc`: *Trigger a garbage collection. Testing only.*

- `yes`: *Run the last suggested incorrect command.*

- `dos-ban [add/remove] [ip]`: *Add or remove a DOS ban.*

## Dedicated Server Configuration Options

- `name`: *The server name as displayed on clients.*

- `desc`: *The server description, displayed under the name. Max 100 characters.*

- `port`: *The port to host on.*

- `autoUpdate`: *Whether to auto-update and exit when a new bleeding-edge update arrives.*

- `showConnectMessages`: *Whether to display connect/disconnect messages.*

- `enableVotekick`: *Whether votekick is enabled.*

- `startCommands`: *Commands run at startup. This should be a comma-separated list.*

- `logging`: *Whether to log everything to files.*

- `strict`: *Whether strict mode is on - corrects positions and prevents duplicate UUIDs.*

- `antiSpam`: *Whether spammers are automatically kicked and rate-limited.*

- `interactRateWindow`: *Block interaction rate limit window, in seconds.*

- `interactRateLimit`: *Block interaction rate limit.*

- `interactRateKick`: *How many times a player must interact inside the window to get kicked.*

- `messageRateLimit`: *Message rate limit in seconds. 0 to disable.*

- `messageSpamKick`: *How many times a player must send a message before the cooldown to get kicked. 0 to disable.*

- `packetSpamLimit`: *Limit for packet count sent within 3sec that will lead to a blacklist + kick.*

- `uuidChangeLimit`: *Limit for how many UUID changes an IP can send in the time frame specified by uuidChangeTimePeriod before it gets banned.*

- `uuidChangeTimePeriod`: *Time window for the uuidChangeLimit config, in hours.*

- `chatSpamLimit`: *Limit for chat packet count sent within 2sec that will lead to a blacklist + kick. Not the same as a rate limit.*

- `socketInput`: *Allows a local application to control this server through a local TCP socket.*

- `socketInputPort`: *The port for socket input.*

- `socketInputAddress`: *The bind address for socket input.*

- `allowCustomClients`: *Whether custom clients are allowed to connect.*

- `whitelist`: *Whether the whitelist is used.*

- `motd`: *The message displayed to people on connection.*

- `autosave`: *Whether the periodically save the map when playing.*

- `autosaveAmount`: *The maximum amount of autosaves. Older ones get replaced.*

- `autosaveSpacing`: *Spacing between autosaves in seconds.*

- `debug`: *Enable debug logging.*

- `snapshotInterval`: *Client entity snapshot interval in ms.*

- `autoPause`: *Whether the game should pause when nobody is online.*

- `roundExtraTime`: *Time before loading a new map after the gameover, in seconds.*

- `maxLogLength`: *The Maximum log file size, in bytes.*

- `logCommands`: *Whether player commands should be logged.*
