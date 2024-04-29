import transformers
import pretty_midi
import argparse
import video_to_audio_to_text_converter as converter

parser = argparse.ArgumentParser()
parser.add_argument("--n_labels", type=int, choices=(7, 28), default=28,
    help="Number of labels to output, 7 or 28.")
parser.add_argument("--midi_file_path", type=str,
    help="Path to the MIDI file")
parser.add_argument("--audio_text_file_path", type=str,
    help="Path to the audio_text file")
parser.add_argument("--audio_file_path", type=str,
    help="Path to the audio file")
parser.add_argument("--video_file_path", type=str,
    help="Path to the video file")
parser.add_argument("--lyrics", type=str,
    help="Song lyrics, must be in quotes")
args = parser.parse_args()

assert args.midi_file_path != None or args.audio_text_file_path != None or args.audio_file_path != None or args.video_file_path != None or args.lyrics != None, \
    "Either MIDI file path or audio_text_file_path or audio or video or lyrics must be provided."

assert not (args.midi_file_path != None and args.audio_text_file_path != None and args.audio_file_path != None and args.video_file_path != None and args.lyrics != None), \
    "Cannot provide MORE THAN ONE LYRICS_ARGS."
    # "Cannot provide BOTH MIDI file path and lyrics."

model_dir = f'models/labels{args.n_labels}'
tokenizer = transformers.AutoTokenizer.from_pretrained(model_dir)
model = transformers.AutoModelForSequenceClassification.from_pretrained(model_dir)
pipeline = transformers.pipeline("text-classification", model=model, tokenizer=tokenizer, top_k=None)

# python main.py --midi_file_path "JohnLennon_Imagine.mid" 
# python main.py --n_labels 7 --midi_file_path "JohnLennon_Imagine.mid"
if args.midi_file_path != None:
    mid = pretty_midi.PrettyMIDI(args.midi_file_path)
    lyrics = "".join([lyric.text for lyric in mid.lyrics])\

# python main.py --audio_text_file_path "transcription.txt"  
# python main.py --n_labels 7 --audio_text_file_path "transcription.txt"  

elif args.audio_text_file_path != None:
    with open(args.audio_text_file_path, 'r') as file:
        lyrics = file.read()

# python main.py --audio_file_path "audio_songs\Unstoppable_small.mp3"
# python main.py --audio_file_path "see_you_again.mp3"
# python main.py --n_labels 7 --audio_file_path "see_you_again.mp3"

elif args.audio_file_path != None:
    converter.audio_to_text(args.audio_file_path)
    with open('transcription.txt', 'r') as file:
        lyrics = file.read()

# python main.py --video_file_path "video_songs\see_you_again.mp4"
# python main.py --video_file_path "see_you_again.mp4"
# python main.py --n_labels 7 --video_file_path "see_you_again.mp4"

elif args.video_file_path != None:
    converter.video_to_audio_to_text(args.video_file_path)
    with open('transcription.txt', 'r') as file:
        lyrics = file.read()
else:
    lyrics = args.lyrics

'''
python main.py --lyrics "I'm scared, of the mountain           
Of the river, of the fire
Of the sound of lightning in the sky
Those sounds make me wanna cry"
'''

emotions = pipeline(lyrics, truncation=True)[0]

[print(f'{emotion["label"]:15s}: {emotion["score"]:.4f}') for emotion in emotions]
lyrics = lyrics.replace("\r", "\n")
print("\nLyrics:")
print(lyrics)

