import wave

song = wave.open("song.wav", mode='rb')

# reading all the audio frames from the WAV file
frame_bytes = bytearray(list(song.readframes(song.getnframes())))
string = input ("Enter your message: ")

# ensuring that the length of the message matches the avaiable space in the audio file
# it pads the message with '#' if needed
string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'

# converting message --> ASCII --> 8-bit binary representation --> integer
bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))

# iterating over each bit of the message and modifies the least significatn bit (LSB)
for i, bit in enumerate(bits):
    frame_bytes[i] = (frame_bytes[i] & 254) | bit

# convert modified frame_bytes back into a bytes object
frame_modified = bytes(frame_bytes)

with wave.open('song_embedded.wav', 'wb') as fd:
    # sets the parameters of the new WAV file to match the original
    fd.setparams(song.getparams())
    fd.writeframes(frame_modified)
song.close()