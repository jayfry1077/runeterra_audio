from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import pydub
import sys
import subprocess
from tempfile import gettempdir


def text_to_audio(path_to_text=str, OGG_PATH=str, WAV_PATH=str, voice_id='Salli'):
    '''
    path_to_text: Specify the location of your text files. Text files must contain cardCode followed by a space in the name
    \nOGG_PATH: Specify the location you want to save the audio output.
    \nvoice_id: Default is Salli. Options are. 
        Salli, Joanna, Ivy, Kendra, Kimberly, Matthew, Justin, Joey
    \nprofile used for aws is 'default'
    '''

    if not os.path.isdir(OGG_PATH):
        print('Creating Path {}'.format(OGG_PATH))
        os.mkdir(OGG_PATH)
    
    if not os.path.isdir(WAV_PATH):
        print('Creating Path {}'.format(WAV_PATH))
        os.mkdir(WAV_PATH)
        
    # Create a client using the credentials and region defined in the [adminuser]
    # section of the AWS credentials file (~/.aws/credentials).
    session = Session(profile_name="default")
    polly = session.client("polly")
 

    for file in os.listdir(path_to_text):
        with open((path_to_text + file), 'r') as f:

            try:
                # Request speech synthesis
                response = polly.synthesize_speech(Text=f.read(), OutputFormat="ogg_vorbis",
                                                VoiceId="Salli")
                f = open(OGG_PATH + file[:-4] + ".ogg", "wb")
                f.write(response['AudioStream'].read())
                f.close

                wav_file_name = file.split(" ")[0]
                sound = pydub.AudioSegment.from_ogg(OGG_PATH + file[:-4] + ".ogg")
                sound.export(WAV_PATH + wav_file_name + ".wav", format='wav')
                print('Wrote {} to disk.'.format(file[7:-4]))
            
            except (BotoCoreError, ClientError) as error:
                # The service returned an error, exit gracefully
                print(error)
                sys.exit(-1)


    
