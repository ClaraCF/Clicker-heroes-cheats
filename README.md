# Clicker Heroes 1 Cheats
Clicker Heroes 1 comes with an export feature which provides the player with a base64 encoded save\.  
This one can be abused to tweak its values and grant the player an advantage\.  
This repo has a python script that facilitates the auditing process of this game, taking the user's base64 encoded save file, modifying it at will and generating a new file which the player can then import to their game\.  
  
![Have a nice day ♥](https://img.shields.io/static/v1?label=Hey~&message=Have%20A%20Nice%20Day%20♥&color=blueviolet) &nbsp; ![GitHub last commit](https://img.shields.io/github/last-commit/ClaraCF/clicker-heroes-cheats?color=ff7fff) &nbsp; ![GitHub](https://img.shields.io/github/license/ClaraCF/clicker-heroes-cheats)<br><br>  
  
## Disclaimer
My intentions do not lie upon destroying or causing harm of any kind to the studio who developed the game, Playsaurus.  
Several other tools have been deployed and are scattered all over the web already.  
The topic about hacking has already been talked about numerous times on their [community](https://www.reddit.com/r/ClickerHeroes/)\.  
The devs themselves released a statement addressing the situation on their [blog](https://www.clickerheroes2.com/paytowin.php) in a post on why Clicker Heroes 2 (their new game which you should definitely [check out](https://www.clickerheroes2.com)) saying that:  
> Games are inherently addictive [...]. We found that some number of players spent many thousands of dollars on rubies.  
We really don't like making money off players who are in denial of their addiction, and that's what a large part of free-to-play gaming is all about.  
[...]  
That said, we're not going to change how we monetize Clicker Heroes 1. It would destroy our studio if we did. 

So just to reiterate, my intentions do not lie upon harming, but rather learning, as I am a cybersecurity student looking for a deeper understanding of machines and improving my coding skills in the process.<br><br>  
  
## Requirements
The only used modules are argparse, base64 and zlib, which are already included in [The Python Standard Library](https://docs.python.org/3/library)\.  
See [argparse](https://docs.python.org/3/library/#:~:text=argparse), [base64](https://docs.python.org/3/library/#:~:text=base64) and [zlib](https://docs.python.org/3/library/#:~:text=zlib)\.  
This means that an installation process is not necessary.<br><br>  
    
## Usage
The player is required to give as input a base64 encoded save file and can choose from the available options. The file extension is irrelevant as long as the file contains base64.  
It is not obligatory to use all flags, they're all optional. You can see some examples on how to use this tool in the [examples section](#examples)\.  
Upon specifying a flag, the user can then set the amount of said value.  
Also, the program comes with a help menu:
```
usage: main.py [-h] [-g gold amount] [-r rubies amount] [-s souls amount] [-o filename] [--stdin] save

positional arguments:
  save              The path to your exported Base64 game save file

optional arguments:
  -h, --help        show this help message and exit
  -g gold amount    specifies a new amount of gold
  -r rubies amount  specifies a new amount of rubies
  -s souls amount   specifies a new amount of hero souls
  -o filename       Output result to a file instead of the screen
  --stdin           Takes base64 input from stdin instead of a file
```
There are 2 ways of providing input, either specifying the filename containing the base64 (default option) or directly pasting it in the command if the `--stdin` flag is used.
There are also 2 ways of displaying output, either printing it to the screen (default option) or writing it to a file if the `-o` flag is used.<br><br>  
  
## Examples
 * Miscelaneous & Quick Reference
    * Check help menu
      * `python main.py -h`
      * `python main.py --help`
      <br>
      
    * Add gold, rubies and souls reading export from file and print to screen
      * `python main.py -g GOLD -r RUBIES -s SOULS <filename>`
      <br>
      
    * Add gold, rubies and souls reading export from file and writing output to a file
      * `python main.py -g GOLD -r RUBIES -s SOULS <input filename> -o <output filename>`
      <br>
      
    * Add gold, rubies and souls reading from STDIN and printing the result to the screen
      * `python main.py -g GOLD -r RUBIES -s SOULS --stdin <your very long base64>`
      <br>
      
    * Add gold, rubies and souls reading from STDIN and writing the result to a file
      * `python main.py -g GOLD -r RUBIES -s SOULS --stdin <your very long base64> -o <output filename>`
      <br>
      
As stated before, flags are optional, which means you are not forced to use them all. You can make combinations, or even use them alone:  
  * Add only gold
      * `python main.py -g GOLD mySave.b64`
      <br>
    
  * Add only rubies
      * `python main.py -r RUBIES mySave.b64`
      <br>
      
  * Add only hero souls
      * `python main.py -s SOULS mySave.b64`
      <br>
      
  * Add gold and rubies
      * `python main.py -g GOLD -r RUBIES --stdin SWYgeW91J3JlIHJlYWRpbmcgdGhpcywgaGF2ZSBhIG5pY2UgZGF5IDwzCg==`
      <br>

And so on and so forth.  
It's also worth noticing that **order is completely irrelevant**\. <br><br>  
  
## Contributing
This project is open to pull requests. They're greatly appreciated 💜.  
For suggestions on changes or additions, please open an issue describing with as much detail your thoughts.  
Same thing goes with bugs and major mistakes (Thanks~). <br><br>


## License
[MIT](https://choosealicense.com/licenses/mit/)
