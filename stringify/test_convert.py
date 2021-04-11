from pydub import AudioSegment

filename = "Mark"

def convert_mp3_to_wav(filename):
    """ converts mp3 file to wav soundfile """
    
    sound = AudioSegment.from_mp3(f'{filename}.mp3')
    sound.export(f"{filename}.wav", format="wav")
    return

convert_mp3_to_wav(filename)