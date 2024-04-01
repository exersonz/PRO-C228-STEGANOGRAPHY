import wave
song = wave.open("song_embedded.wav", mode='rb')

# reads all the audio frames from the WAV file, converting them into a list of bytes
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# extracts the least significant bit (LSB) from each byte of the audio data
# `& 1` operation masks the byte with 1, effectively isolating the LSB
extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]

# convert LSBs --> characters (by grouping them into groups of 8) --> integer --> character
# ultimately creates a string representation of the hidden message
string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))

# split decoded string at the delimiter "###" and takes the first part
decoded = string.split("###")[0]

print("Sucessfully decoded: "+decoded)
song.close()