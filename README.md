# GOOD Formatter for Ambr

Python script that converts GOOD formated JSONs exported from different programs to GOOD formated JSON that Ambr is expecting.

It only supports Genshin Impact materials for now.

JSON exported from said programs are expected to contain at least of of the following item types:
- Character Development Items
- Materials

## Instructions
### Editing convertAmbr.py
1) Scan your materials using your desired program. I recommend [Inventory_Kamera](https://github.com/Andrewthe13th/Inventory_Kamera/)
2) Move the file to the directory where you extacted convertAmbr.py
3) Open **convertAmbr.py** on your text editor of preference
4) Change **YOUR_FILE_NAME_HERE.json** to the filename of your resulted exported GOOD formatted JSON
5) **Save** the file

### Usage

1) Either double click **convertAmbr.py** or open it on Python's IDLE, then selet Run > Run Module
2) The script will request that you input your amount of Enhancement Ore (Weapon Leveling Material)
3) Once you have entered the requested values, a new file should be created on that same directory. Defaulted to **updated_ambrTemplate.json**
4) Import the file into Ambr
