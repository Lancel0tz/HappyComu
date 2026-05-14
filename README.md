# HappyComu: Interactive 3D Talking-Head Avatar System

HappyComu is an end-to-end conversational digital human prototype that combines:
- speech recording
- Whisper speech-to-text
- LLM response generation
- text-to-speech
- SadTalker-style 3DMM-based talking-head animation
- PyQt desktop interaction interface

## Pipeline
User voice → ASR → LLM response → TTS → 3DMM-based facial animation → avatar video playback

## Features
- Audio-driven talking-head generation
- 3DMM coefficient extraction and rendering
- Character prompt configuration
- PyQt-based interaction window
- Support for pose, eye-blink, and facial enhancement options

## Tech Stack
Python, PyTorch, PyQt5, SadTalker, 3DMM, Whisper, OpenAI API, TTS
