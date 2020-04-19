# runeterra_audio
Turn your favorite runeterra decks into audio files!

PRE-REQUESITES

In order to use this succesfully you will need a few things. 
1. Python 3.7 (probably works on older versions of 3.x)
2. ffmpeg (https://www.ffmpeg.org/)
  https://www.youtube.com/watch?v=SW-iKrT_nJs
  
3. An AWS account (Free but you need a credit card on file with Amazon).
  Create AWS account - https://www.youtube.com/watch?v=XhW17g73fvY
4. AWS credentails set as default.
  Install AWS CLI - https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html
  Set default credentails
  create key / secret key - https://www.youtube.com/watch?v=HCl2_FzMxAg
  Set access keys - https://youtu.be/bT19B3IBWHE?t=101
  

How to use:
Now that you're done with all the setup, this should be a breeze to use. 

Currently there are 4 things you can do:

##JSON TO TEXT FILES##

blitzcrank.card_grab(path_to_file=str, path_to_save=str)

  You give it a path to the RIOT games runeterra.json file (Download from here https://dd.b.pvp.net/latest/set1-lite-en_us.zip)
  It will save a text file for each card in the game, into the "path_to_save"
  
  Example text file:
  
    Name. Garen.
    Region. Demacia.
    Cost. 5.
    Attack. 5.
    Health. 5. 
    Keywords.
      1. Regeneration.
      Level up criteria. I've struck twice..
    Associated card 1. Name. Garen.
    Cost. 5.
    Description. Round Start: Rally..
    Attack. 6.
    Health. 6. 
    Keywords.
    1. Regeneration.
    Associated card 2. Name. Garen's Judgment.
    Cost. 8.
    Description. A battling ally strikes all battling enemies.

    Shuffle a Garen into your deck..
    Spell Speed. Fast.
  
Each text file is ran through AWS Polly text to speech. It will save them as OGG files, and then WAV files. The great thing about this setup is you dont need to use blitzcrank to grab the text files. You can create them all yourself if youwant, but the naming scheme must be the same for each text file.

##TEXT FILES TO AUDIO FILES##

sona.text_to_audio(TEXT_PATH, OGG_PATH, WAV_PATH)

You give it a PATH to all the text files, it will run them through AWS Poll and save them to paths of your choice.

##DECKS TO AUDIO##

heimerdinger.deck_code_to_audio(deck_code, "Bannermen", WAV_PATH, SAVE_PATH, 2 )

Give it a RIOT games deck code, a name of your output file, path to your WAV files made by sona. Path to save your file too, and how long you want some silence inbetween each card read.

heimerdinger.regions_to_audio(WAV_PATH, SAVE_PATH, 2)

Give it a path to your WAV files made by sona, and a save loction, and how much silence you want inbetween the cards.

The output will be an mp3 file for each Region in the game!
