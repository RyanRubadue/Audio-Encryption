from DES import des_encryption, des_decryption, demoDES
from playsound import playsound

import librosa
import pkg_resources
import time
import wave
pkg_resources.require("playsound==1.2.2")

SOUNDS = ["guitar", "cat"]

print("Welcome! This program demonstrates the use of DES encryption/decryption on audio files.\n")

# Demonstration DES
print("Demonstration of DES Algorithm:\n")
demoDES()


for sound in SOUNDS:
    print(f"\n\n****Press Enter to hear {sound} Raw Audio File***\n")

    file = str(sound + ".wav")
    # Load Sound
    y, sr = librosa.load(file)
    playsound(file)

    w = wave.open(file, 'rb')
    params = w.getparams()
    frames = []

    for i in range(w.getnframes()):
        frames.append(w.readframes(i).hex())

    # WRITE AND PLAY NEW WAV FILE DEMO
    file = "decryptions/" + sound + "_test.wav"
    w = wave.open(file, 'w')

    w.setparams(params)
    for i in frames:
        # print(i)
        w.writeframes(bytes.fromhex(i))
    w.close()
    input(f"\n\n****Press Enter to hear {sound} WRITTEN AUDIO File***\n")
    playsound(file)
    # exit(0)

    encrypted_Strings = []

    print("Running DES Encryption on Audio File. (This may take several minutes)")
    start = time.time()
    for frame in frames:
        line = []
        for chunk in range(0, len(frame), 16):
            line.append(des_encryption(frame[chunk: chunk + 16]))
        encrypted_Strings.append(line)
    end = time.time()
    print(f"\n{sound} audio file was encrypted in {end - start} seconds")

    file = 'encryptions/' + sound + '.txt'
    with open(file, "w") as f:
        for line in encrypted_Strings:
            data = ""
            for encryption in line:
                data += encryption
            f.write(data)
    print(f"Encrypted data written to {file}")

    print("\nRunning DES Decryption on Audio File. (This may take several minutes)")

