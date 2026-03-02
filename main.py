import wave
import numpy as np

# Open the WAV file
with wave.open("glow.wav", "r") as f:

    # Get the parameters of the WAV file
    sample_rate = f.getframerate()
    num_channels = f.getnchannels()
    bit_depth = f.getsampwidth() * 8 # Multiplying by 8 returns bits instead of bytes
    num_frames = f.getnframes()

    # Calculate duration
    duration = num_frames / sample_rate

    # Read raw bytes from the file
    raw_bytes = f.readframes(f.getnframes())

# Convert bytes into numbers
audio_data = np.frombuffer(raw_bytes, dtype=np.int16)



print(f"Type: {type(audio_data)}")
print (f"Shape: {audio_data.shape}")
print(f"First 20 samples: {audio_data[:20]}")
print(f"Min value: {audio_data.min()}")
print(f"Max value: {audio_data.max()}")
print(f"Data type: {audio_data.dtype}")




"""
    print (f"Sample rate: {sample_rate} Hz")
    print(f"Channels: {num_channels}")
    print(f"Bit depth: {bit_depth} bit")
    print(f"Number of samples: {num_frames}")
    print(f"Duration: {duration:.2f} seconds")
"""

