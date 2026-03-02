import wave
import numpy as np

# Open the WAV file
with wave.open("glow.wav", "r") as f:

    # Get the parameters of the WAV file
    sample_rate = f.getframerate()
    num_channels = f.getnchannels()
    samp_width = f.getsampwidth()
    num_frames = f.getnframes()
    raw_bytes = f.readframes(num_frames)

audio_data = np.frombuffer(raw_bytes, dtype=np.int16).reshape(-1, num_channels)

# Half Volumeit
quiet = (audio_data * .5).astype(np.int16)

# Reverse
reversed_audio = audio_data[::-1]

three_seconds = sample_rate * 3
trimmed = audio_data[:three_seconds]

def save_wav(filename, data, sample_rate, num_channels, samp_width):
    with wave.open(filename, "w") as f:
        f.setnchannels(num_channels)
        f.setsampwidth(samp_width)
        f.setframerate(sample_rate)
        f.writeframes(data.tobytes())

save_wav("quiet.wav", quiet, sample_rate, num_channels, samp_width)
save_wav("reversed.wav", reversed_audio, sample_rate, num_channels, samp_width)
save_wav("trimmed.wav", trimmed, sample_rate, num_channels, samp_width)

""""

# Reshape into (num_samples, num_channels)
audio_data = audio_data.reshape(-1, num_channels)

print(f"Shape after reshape: {audio_data.shape}")
print(f"First 10 frames:\n{audio_data[:10]}")

# Assign each channel individually
left_channel = audio_data[:, 0]
right_channel = audio_data[:, 1]

print(f"\nLeft Channel first 10 samples: {left_channel[:10]}")
print(f"Right channel first 10 samples: {right_channel[:10]}")

print(f"Type: {type(audio_data)}")
print (f"Shape: {audio_data.shape}")
print(f"First 20 samples: {audio_data[:20]}")
print(f"Min value: {audio_data.min()}")
print(f"Max value: {audio_data.max()}")
print(f"Data type: {audio_data.dtype}")

print (f"Sample rate: {sample_rate} Hz")
print(f"Channels: {num_channels}")
print(f"Bit depth: {bit_depth} bit")
print(f"Number of samples: {num_frames}")
print(f"Duration: {duration:.2f} seconds")

"""

