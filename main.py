import pygame
import time
import numpy as np

# Initialize pygame mixer
pygame.mixer.init()

# Define the notes for an extended "Jingle Bells"
notes = [
    # Jingle Bells (Chorus)
    (659, 0.4), (659, 0.4), (659, 0.8),  # E E E
    (659, 0.4), (659, 0.4), (659, 0.8),  # E E E
    (659, 0.4), (784, 0.4), (523, 0.8), (587, 0.4), (659, 0.8),  # E G C D E
    (698, 0.4), (698, 0.4), (698, 0.8), (698, 0.4),  # F F F F
    (659, 0.4), (659, 0.4), (659, 0.8), (698, 0.4),  # E E E E
    (587, 0.4), (587, 0.4), (659, 0.4), (587, 0.4), (784, 0.8),  # D D E D G

    # Oh what fun it is to ride
    (659, 0.4), (659, 0.4), (659, 0.4), (523, 0.4), (659, 0.4),  # E E E C E
    (587, 0.8), (698, 0.4), (659, 0.4), (587, 0.4), (523, 0.8),  # D F E D C

    # Jingle Bells (Chorus again)
    (659, 0.4), (659, 0.4), (659, 0.8),  # E E E
    (659, 0.4), (659, 0.4), (659, 0.8),  # E E E
    (659, 0.4), (784, 0.4), (523, 0.8), (587, 0.4), (659, 0.8),  # E G C D E
    (698, 0.4), (698, 0.4), (698, 0.8), (698, 0.4),  # F F F F
    (659, 0.4), (659, 0.4), (659, 0.8), (698, 0.4),  # E E E E
    (587, 0.4), (587, 0.4), (659, 0.4), (587, 0.4), (784, 0.8),  # D D E D G

    # Dashing through the snow
    (784, 0.4), (784, 0.4), (784, 0.4), (784, 0.4), (784, 0.4), (698, 0.4),  # G G G G G F
    (698, 0.4), (698, 0.4), (659, 0.4), (587, 0.4), (523, 0.8),  # F F E D C

    # In a one-horse open sleigh
    (587, 0.4), (659, 0.4), (587, 0.4), (523, 0.4), (698, 0.8),  # D E D C F
]

# Function to generate sound array
def generate_sound_array(frequency, duration, sample_rate=44100):
    t = np.linspace(start=0, stop=duration, num=int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    sound_array = np.int16(wave * 32767)
    stereo_sound_array = np.column_stack((sound_array, sound_array))
    return stereo_sound_array

# Function to play a note
def play_note(frequency, duration):
    sound_array = generate_sound_array(frequency, duration)
    sound = pygame.sndarray.make_sound(sound_array)
    sound.play()
    time.sleep(duration)

# Main loop to play tune
print("Playing Jingle Bells...")
for note in notes:
    frequency, duration = note
    play_note(frequency, duration)

print("Tune finished!")
