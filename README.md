# SPEECH-RECOGNITION-SYSTEM

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: MOHAMMED IBRAHIM SH

*INTERN ID*: CT04DG2681

*DOMAIN*: ARTIFICIAL INTELLIGENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

**DESCRIPTION:**

The Python program you’ve written is designed for automatic speech recognition (ASR), which means it can turn spoken words in an audio file into written text. It achieves this by using a pre-trained deep learning model called Wav2Vec, developed by Facebook (now Meta) AI.

Wav2Vec is a powerful model that learns to understand audio directly from raw sound waves instead of relying on traditional features like spectrograms or hand-crafted signal processing. This makes it highly effective and accurate for recognizing speech. Your script connects to this model using a library called Transformers, which makes advanced AI models easy to use in Python.

How the Program Works
Your program does several things in order:

Loads the Wav2Vec model and processor

Accepts an audio file path from the user

Reads the audio from the file into memory

Processes the audio into a format the model can understand

Runs the audio through the Wav2Vec model to predict the spoken words

Decodes those predictions into human-readable text

Displays the text on the screen

Let’s discuss each of these steps in simple language.

Loading Wav2Vec and the Processor
The Wav2Vec model has two key parts:

The Wav2Vec model itself
This is a deep neural network that listens to raw audio and learns which words were spoken. It has been trained on hundreds of hours of English speech, making it quite skilled at understanding various accents and speech patterns.

The Wav2Vec processor
This tool takes care of:

Converting raw sound waves into input features the model can use.

Turning the model’s numeric predictions back into text that humans can read.

Think of the processor as an interpreter between human audio and the Wav2Vec model.

Accepting the Audio File Path
When you run your program, it asks the user for the path to an audio file.

Reading the Audio
Your program uses a library to read the audio file into memory. Audio files contain data about how sound waves change over time. These are represented as arrays of numbers:

If the audio is mono, it has one channel of data.

If it’s stereo, it has two channels (left and right).

Since Wav2Vec expects mono audio, your program converts stereo recordings into mono by averaging the two channels into one.

Ensuring the Correct Format
Wav2Vec expects audio:

To be sampled at 16,000 samples per second (16 kHz)

To be stored as floating-point numbers (not integers)

To have values between -1 and 1

If the sample rate is different, your program stops and warns the user. This is important because feeding audio with the wrong sample rate can make the model’s predictions inaccurate.

Processing the Audio
Once the audio is loaded and properly formatted, it must be transformed into a format the model understands. The processor:

Divides the audio into small overlapping pieces.

Converts each piece into features suitable for the model’s neural network.

This step turns the raw audio into “model inputs.”

Running Wav2Vec
The prepared audio data is fed into the Wav2Vec model. Inside the model:

It “listens” to the sound and predicts which sounds map to which letters or words.

It outputs something called logits, which are scores representing how likely each piece of sound matches a particular letter or word.

Decoding Predictions
The processor then:

Looks at these scores.

Figures out which letters or words are the most probable.

Puts them together into a complete transcription of what was said.

This decoding step is what transforms raw model outputs into readable sentences.

Displaying the Text
Finally, your program prints the text to the screen. For instance, if your audio file says:

“Hello, how are you?”

The model might output:

makefile
Copy
Edit
Transcription: Hello how are you
The punctuation might sometimes be missing because Wav2Vec focuses on recognizing words rather than punctuation marks. However, it’s possible to add extra models later to handle punctuation or formatting.

Why Wav2Vec is Impressive
What makes Wav2Vec remarkable is:

It can handle different speakers and accents quite well.

It works directly on audio waveforms without complex feature engineering.

It performs competitively with traditional speech recognition systems.

Because of these strengths, tools like Wav2Vec have made speech-to-text far more accessible for developers, researchers, and businesses.

How You Could Expand This
Your program currently works with audio files. In the future, you could:

Allow live recording through a microphone.

Support other languages by loading different Wav2Vec models.

Automatically resample audio to the correct rate.

Save transcriptions into text files or databases.

In Summary
Your Python script uses Wav2Vec and its processor to:

Load an audio file.

Convert it into the right shape and format.

Feed it into a powerful deep learning model.

Decode the results into written text.

Show the transcription to the user.

Thanks to models like Wav2Vec, speech recognition tasks that once required huge teams of engineers and complicated code can now be handled with just a few lines of Python. Your program is a great example of how modern AI makes advanced technology accessible for many applications, including transcription services, virtual assistants, accessibility tools, and more.

**OUTPUT:** ![Image](https://github.com/user-attachments/assets/35935ebe-d538-4950-ac4c-35d9d053fcf3)
