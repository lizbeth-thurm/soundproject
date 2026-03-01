import wave

# Open the WAV file
with wave.open("glow.wav", "r") as f:

    # Get the parameters of the WAV file
    sample_rate = f.getframerate()
    num_channels = f.getnchannels()
    bit_depth = f.getsampwidth() * 8 # Multiplying by 8 returns bits instead of bytes
    num_frames = f.getnframes()

    # Calculate duration
    duration = num_frames / sample_rate

    print (f"Sample rate: {sample_rate} Hz")
    print(f"Channels: {num_channels}")
    print(f"Bit depth: {bit_depth} bit")
    print(f"Number of samples: {num_frames}")
    print(f"Duration: {duration:.2f} seconds")
