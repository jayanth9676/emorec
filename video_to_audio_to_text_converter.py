import whisper
import moviepy.editor as mp
# from pydub import AudioSegment
# import speech_recognition as sr
# import os

def audio_to_text(audio_file):
	model = whisper.load_model("base")
	# result = model.transcribe("output.mp3")
	result = model.transcribe(audio_file)

	with open("transcription.txt", "w") as f:
		f.write(result["text"])


def video_to_audio_to_text(video_file):
    # video = mp.VideoFileClip("see-you-again.mp4")
    video = mp.VideoFileClip(video_file)
    video.audio.write_audiofile("output_video_to_audio.mp3")
    # video.audio.write_audiofile("output_video_to_audio.wav")


    # video.audio.write_audiofile("output.mp3")
    # audio = AudioSegment.from_file("output.mp3", format="mp3")
    # audio.export("output.wav", format="wav")
    # audio = AudioSegment.from_file("output.wav", format="wav")
    # audio = audio.set_channels(1)
    # audio.export("output.wav", format="wav")

    audio_to_text("output_video_to_audio.mp3")
    # audio_to_text("output_video_to_audio.wav")