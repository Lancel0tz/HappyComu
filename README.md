# HappyComu: Interactive 3D Talking-Head Avatar System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" />
  <img src="https://img.shields.io/badge/PyTorch-Deep%20Learning-red.svg" />
  <img src="https://img.shields.io/badge/Whisper-ASR-green.svg" />
  <img src="https://img.shields.io/badge/SadTalker-Talking%20Head-purple.svg" />
  <img src="https://img.shields.io/badge/PyQt5-Desktop%20GUI-orange.svg" />
</p>

## Overview

**HappyComu** is an end-to-end conversational digital human prototype that integrates speech recognition, large language model response generation, text-to-speech synthesis, and audio-driven talking-head animation into a desktop interaction system.

The system allows users to talk with a virtual character through a PyQt-based interface. User speech is recorded and transcribed into text, then processed by a language model to generate a character-specific response. The generated response is converted into speech and used to drive a 3DMM-based talking-head animation pipeline, producing a synchronized avatar video response.

This project demonstrates the integration of multiple AI components into a complete multimodal human-computer interaction pipeline.

---


## System Pipeline

```text
User Speech
    ↓
Audio Recording
    ↓
Whisper Speech Recognition
    ↓
LLM Response Generation
    ↓
Text-to-Speech Synthesis
    ↓
3DMM-based Talking-Head Animation
    ↓
PyQt Avatar Video Playback
````

In short:

```text
User Voice → ASR → LLM Response → TTS → Facial Animation → Avatar Video Playback
```

---

## Key Features

* **End-to-end digital human interaction**

  * Supports the full loop from user voice input to animated avatar response.

* **Speech recognition with Whisper**

  * Converts recorded user speech into text for downstream dialogue generation.

* **LLM-based response generation**

  * Generates short and character-consistent responses based on conversation history and character prompt settings.

* **Text-to-speech synthesis**

  * Converts generated text responses into speech audio.

* **Audio-driven talking-head animation**

  * Uses a SadTalker-style 3DMM-based animation pipeline to generate synchronized facial movements from speech.

* **PyQt desktop interface**

  * Provides an interactive desktop application for recording, processing, and playing avatar responses.

* **Modular pipeline design**

  * Separates audio recording, dialogue generation, speech synthesis, animation inference, and GUI playback into different modules.

---

## Tech Stack

| Component               | Technology                         |
| ----------------------- | ---------------------------------- |
| Programming Language    | Python                             |
| Deep Learning Framework | PyTorch                            |
| Desktop Interface       | PyQt5                              |
| Speech Recognition      | Whisper                            |
| Response Generation     | OpenAI API / LLM                   |
| Text-to-Speech          | OpenAI TTS                         |
| Talking-Head Animation  | SadTalker-style 3DMM pipeline      |
| Audio Processing        | sounddevice, scipy                 |
| Video Playback          | PyQt Multimedia                    |
| Runtime Environment     | Conda / Python virtual environment |

---

## Project Structure

```text
HappyComu/
├── main.py                 # Main application entry point
├── player.py               # PyQt-based video player and interaction interface
├── record.py               # Audio recording module
├── respond.py              # Speech recognition, LLM response, and TTS pipeline
├── inference.py            # Talking-head animation inference pipeline
├── app_sadtalker.py        # SadTalker-related application script
├── launcher.py             # Launcher script
├── predict.py              # Prediction and inference utilities
├── setup.py                # Character prompt and configuration settings
├── scripts/                # Supporting scripts
├── src/                    # Core talking-head generation modules
├── examples/               # Example audio, image, and video files
├── results/                # Generated animation results
├── requirements.txt        # Main Python dependencies
├── requirements3d.txt      # 3D / rendering-related dependencies
├── webui.sh                # Web UI launch script for Linux/macOS
├── webui.bat               # Web UI launch script for Windows
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Lancel0tz/HappyComu.git
cd HappyComu
```

### 2. Create a virtual environment

Using Conda is recommended:

```bash
conda create -n happycomu python=3.8
conda activate happycomu
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
pip install -r requirements3d.txt
```

Depending on your local environment, you may also need to install additional packages for audio recording, video playback, and GPU acceleration.

---

## Configuration

### 1. Configure OpenAI API Key

Do **not** hard-code your API key directly in the source code.

Instead, set it as an environment variable:

#### macOS / Linux

```bash
export OPENAI_API_KEY="your_api_key_here"
```

#### Windows PowerShell

```powershell
setx OPENAI_API_KEY "your_api_key_here"
```

Then load it in Python:

```python
import os
import openai

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
```

---

### 2. Configure Character Prompt

The virtual character behaviour can be customized in:

```text
setup.py
```

You can modify the character identity, speaking style, personality, and response constraints.

For example:

```python
CHAR1 = "You are a friendly virtual companion who speaks naturally and concisely."
```

The dialogue generation module will use this character setting to produce more consistent responses.

---

### 3. Configure Reference Avatar

The talking-head generation pipeline requires a reference image or video for the avatar.

Place the reference file in the appropriate example directory, such as:

```text
examples/source_image/
```

or configure the source path according to the inference script.

---

## Usage

### Run the desktop application

```bash
python main.py
```

Typical interaction flow:

1. Launch the application.
2. Click the interaction button to start recording.
3. Speak to the virtual character.
4. Stop recording.
5. The system transcribes the speech using Whisper.
6. The LLM generates a character-specific response.
7. The response is converted into speech.
8. The generated speech drives the talking-head animation model.
9. The final avatar video is played in the PyQt interface.

---

## Core Modules

### `record.py`

Handles audio recording from the microphone and saves the user input as an audio file.

### `respond.py`

Implements the dialogue processing pipeline:

```text
Recorded Audio → Whisper ASR → LLM Response → TTS Audio
```

This module is responsible for:

* Loading the recorded audio.
* Transcribing user speech.
* Maintaining conversation history.
* Generating a short response from the language model.
* Synthesizing the response into speech audio.

### `inference.py`

Runs the talking-head animation pipeline. It takes the generated speech audio and the reference avatar input, then produces a synchronized talking-head video.

### `player.py`

Implements the PyQt-based graphical interface. It handles user interaction, video playback, and communication between frontend and backend components.

### `main.py`

The main entry point that connects the user interface, recording module, response generation pipeline, and animation generation pipeline.

---

## Engineering Highlights

This project focuses on practical AI system integration rather than a single isolated model.

Key engineering aspects include:

* Integrated ASR, LLM, TTS, and talking-head generation into one complete pipeline.
* Built a desktop-level interactive prototype using PyQt.
* Designed a modular structure for audio recording, response generation, inference, and playback.
* Maintained conversation history to support more natural multi-turn interaction.
* Adapted a research-style talking-head generation model into an interactive application.
* Connected backend AI inference with frontend video playback.
* Supported character-level customization through prompt configuration.

---

## Example Workflow

```text
User: "Hello, how are you today?"

Step 1: The microphone records the user voice.
Step 2: Whisper transcribes the voice into text.
Step 3: The LLM generates a short character-style reply.
Step 4: TTS converts the reply into speech.
Step 5: The generated speech drives the avatar animation.
Step 6: The PyQt interface plays the generated avatar response.
```

---

## Use Cases

HappyComu can be used as a prototype for:

* Conversational digital humans
* AI virtual companions
* Game NPC interaction systems
* Educational virtual tutors
* Human-computer interaction demos
* Multimodal AI application prototypes
* Talking-head avatar research demonstrations

