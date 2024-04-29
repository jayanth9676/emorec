# EMOREC: Emotion Recognition on Song Lyrics using Transformer-based Model Distilbert

## Introduction
EMOREC (Emotion Recognition on Song Lyrics using Transformer-based Model Distilbert) is a project aimed at classifying the emotional content of songs based on their lyrics or MIDI representations. Leveraging Natural Language Processing (NLP) techniques and models like DistilBERT, EMOREC offers a nuanced understanding of emotions expressed in song lyrics.

## Project Overview
The project involves developing NLP models trained on emotion-labeled datasets like GoEmotions. These models are then used to classify emotions in song lyrics extracted from various sources, including MIDI files, audio files, and video files.


## Emotion classification of MIDI lyrics

(Also check out <https://github.com/serkansulun/midi-emotion> for another, more accurate MIDI dataset with continuous-valued valence-arousal labels.)

To only download the datasets, with pairs of MIDI file names and predicted emotions from the lyrics, you can right-click and choose "Save Link As...", using the links below:

[7-labels](https://raw.githubusercontent.com/emotionalmusic/lyricsemotions/master/datasets/7labels.csv)

[28-labels](https://raw.githubusercontent.com/emotionalmusic/lyricsemotions/master/datasets/28labels.csv)

[Download](https://drive.google.com/drive/folders/1k9qAEUMjbUlgBLshTUn-_5-EZiPt-q7J?usp=sharing) the models and place inside the `models` folder. 

Required Python packages: transformers, pretty_midi

## Running the Project

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/jayanth9676/lyricsemotions.git
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Main Script:**

	***28 Labels (Default):***

	`python main.py --midi_file_path "John Lennon - Imagine.mid"`

	or

	`python main.py --lyrics "I hope some day you'll join us. And the world will be as one"`

	or

	`python main.py --audio_text_file_path "transcription.txt"`

	or

	`python main.py --audio_file_path "audio_songs\Unstoppable_small.mp3"`

	or

	`python main.py --video_file_path "video_songs\see-you-again.mp4"`


	***7 Labels:***

	`python main.py --n_labels 7 --midi_file_path "John Lennon - Imagine.mid"`

	or

	`python main.py --n_labels 7 --lyrics "I hope some day you'll join us. And the world will be as one"`

	or

	`python main.py --n_labels 7 --audio_text_file_path "transcription.txt"`

	or

	`python main.py --n_labels 7 --audio_file_path "audio_songs\Unstoppable_small.mp3"`

	or

	`python main.py --n_labels 7 --video_file_path "video_songs\see-you-again.mp4"`

## Model Development
EMOREC utilizes DistilBERT, a transformer-based model, for emotion classification. The model is trained on emotion-labeled datasets to predict emotions from song lyrics.

## OpenAI Whisper Integration
OpenAI Whisper is integrated into the project for converting audio songs to text. This allows for the extraction of lyrics from audio files, which are then used for emotion classification.

## Tools and Libraries
- Transformers library for DistilBERT model implementation
- Pretty MIDI for MIDI file processing
- OpenAI Whisper for audio-to-text conversion
- MoviePy for video-to-audio conversion

## Applications and Use Cases
- Real-Time Emotion Recognition
- Multimodal Emotion Analysis
- Personalized Music Generation
- Cross-Cultural Emotion Analysis
- Emotion-Aware Interactive Systems
- Long-Term Emotional Effects of Music
- Emotion-Based Content Creation

## Conclusion
EMOREC offers a comprehensive approach to emotion recognition in song lyrics, leveraging state-of-the-art NLP techniques and models. By providing emotion classification across various media formats, the project opens up avenues for exploring emotional content in music and its applications in diverse fields.

## References

1. Sanh, V., Debut, L., Chaumond, J., Wolf, T.: Distilbert, a distilled version of bert: smaller, faster, cheaper and lighter. ArXiv abs/1910.01108 (2019)
2. Nguyen, T.H., Shirai, K., Velcin, J.: Sentiment analysis on social media for stock movement prediction. Expert Systems with Applications 42(24), 9603–9611 (2015)
3. Demszky, D., Movshovitz-Attias, D., Ko, J., Cowen, A., Nemade, G., Ravi, S.: GoEmotions: A Dataset of Fine-Grained Emotions. In: 58th Annual Meeting of the Association for Computational Linguistics (ACL) (2020)
4. Raffel, C.: Learning-Based Methods for Comparing Sequences, with Applications to Audio-to-MIDI Alignment and Matching. Ph.D. thesis, Columbia University (2016)
5. Reddit MIDI dataset, https://www.reddit.com/r/WeAreTheMusicMakers/comments/3ajwe4/the_largest_midi_collection_on_the_internet/
6. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, L.,Polosukhin, I.: Attention is all you need. In: Advances in Neural Information Processing Systems 30: Annual Conference on Neural Information Processing Systems. pp. 5998–6008 (2017)
7. Whitelaw, C., Garg, N., Argamon, S.: Using appraisal groups for sentiment analysis. In Proceedings of the 14th ACM international conference on Information and knowledge management. pp. 625–631 (2005)
8. Sulun, S., Davies, M.E.P., Viana, P.: Symbolic music generation conditioned on continuous-valued emotions. IEEE Access 10, 44617–44626 (2022)

	<https://github.com/serkansulun/lyricsemotions>