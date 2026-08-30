# Task 07 - Berry Broker Discord Bot

Berry Broker is a small One Piece themed economy bot I made using Python and discord.py.

The idea is simple, every member in the server is treated like a pirate. Everyone starts with some Berries and then they can earn more, trade with others, buy items, raid other users and try to get into the Worst Generation leaderboard.

I used SQLite for storing all the data, so the balances and inventory will still be there even if the bot is restarted.

---

## Commands

### `!ping`

Just checks if the bot is alive.

```text
!ping
```

### `!bounty`

Shows your wallet, bank and total Berries.

```text
!bounty
```

### `!setsail`

Gives you a daily Berry reward.

You can only use it once every 24 hours.

```text
!setsail
```

### `!trade`

Used to send Berries to another user.

```text
!trade @user 500
```

The bot also checks if you have enough Berries, if the amount is valid, and if you are not trying to trade with yourself or a bot.

### `!shop`

Shows all the items which can be bought.

```text
!shop
```

Each item has a price and an effect.

### `!buy`

Used to buy an item from the shop.

```text
!buy sword
```

The money is removed from the wallet and the item is stored in the database.

### `!inventory`

Shows all the items you currently own.

```text
!inventory
```

If you have bought the same item more than once, the quantity will also be shown.

### `!worstgeneration`

Shows the top 5 richest users in the server.

```text
!worstgeneration
```

The ranking is based on total money:

```text
wallet + bank
```

### `!raid`

Try to raid another user and steal some Berries.

```text
!raid @user
```

The raid is chance based, so sometimes you win and sometimes you fail.

---

## Database

I used Python's built in `sqlite3` module.

The database file is:

```text
berry_broker.db
```

There are mainly two tables right now.

### Users table

This stores stuff like:

- Discord user id
- wallet balance
- bank balance
- last time the user claimed `!setsail`

Every new user starts with:

```text
Wallet: 1000 Berries
Bank: 0 Berries
```

### Inventory table

This stores the items bought by each user.

It keeps things like:

- user id
- item name
- item status

---

## File Structure

```text
Task-07/
│
├── bot.py
├── database.py
├── items.py
├── requirements.txt
├── README.md
│
└── cogs/
    ├── __init__.py
    ├── general.py
    ├── economy.py
    └── shop.py
```

I split the code into different files because keeping everything inside one `bot.py` would get messy pretty fast.

### `bot.py`

This is the main file. It starts the bot and loads the other command files.

### `database.py`

All the SQLite related work is here, like checking balance, adding users, buying items, trading and getting leaderboard data.

### `items.py`

This contains the shop items, their prices and their effects.

### `cogs/general.py`

Contains simple commands like:

```text
!ping
```

### `cogs/economy.py`

Contains the economy commands:

```text
!bounty
!setsail
!trade
!worstgeneration
!raid
```

### `cogs/shop.py`

Contains the shop related commands:

```text
!shop
!buy
!inventory
```

---

## How to Run

Go inside the Task-07 folder.

```bash
cd Task-07
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Create a `.env` file and put your Discord bot token inside it:

```text
DISCORD_TOKEN=your_discord_bot_token
```

Then run the bot:

```bash
python3 bot.py
```

If everything is fine, something like this should come in the terminal:

```text
Berry Broker is online as Berry Broker
```

---

## Screenshots

I will add screenshots of the working commands here.

### Ping

```markdown
![Ping Command](screenshots/ping.png)
```

### Bounty and Setsail

```markdown
![Economy Commands](screenshots/economy.png)
```

### Shop and Inventory

```markdown
![Shop and Inventory](screenshots/shop.png)
```

### Raid and Leaderboard

```markdown
![Raid and Leaderboard](screenshots/raid.png)
```

---

## Note

The bot token is stored in `.env`, so it should not be uploaded to GitHub.

I also ignored these files/folders:

```text
.env
venv/
__pycache__/
berry_broker.db
```

This avoids uploading the token, local virtual environment and local database.
