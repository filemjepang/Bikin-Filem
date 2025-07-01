import argparse
import whisper
from moviepy.editor import VideoFileClip
import argostranslate.translate

def extract_audio(video_path, audio_path="audio.wav"):
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)
    return audio_path

def transcribe_audio(audio_path, model_size="small"):
    model = whisper.load_model(model_size)
    return model.transcribe(audio_path, language="ja")

def translate_segments(segments):
    translated = []
    for seg in segments:
        ja_text = seg["text"]
        id_text = argostranslate.translate.translate(ja_text, "ja", "id")
        translated.append((seg["start"], seg["end"], id_text))
    return translated

def format_timestamp(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds % 1) * 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

def write_srt(segments, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for i, (start, end, text) in enumerate(segments, 1):
            f.write(f"{i}\n")
            f.write(f"{format_timestamp(start)} --> {format_timestamp(end)}\n")
            f.write(f"{text}\n\n")

def main():
    parser = argparse.ArgumentParser(description="Subtitle Otomatis Jepang ke Indonesia (Offline)")
    parser.add_argument("--video", required=True, help="Path ke file video")
    parser.add_argument("--output", default="subtitle.srt", help="Output file SRT")
    parser.add_argument("--model", default="small", help="Model whisper (tiny/base/small/medium/large)")

    args = parser.parse_args()

    print("[1/4] Ekstrak audio...")
    audio_path = extract_audio(args.video)

    print("[2/4] Transkripsi Jepang...")
    result = transcribe_audio(audio_path, args.model)

    print("[3/4] Terjemahan ke Bahasa Indonesia...")
    translated = translate_segments(result["segments"])

    print(f"[4/4] Simpan subtitle ke: {args.output}")
    write_srt(translated, args.output)
    print("✅ Selesai!")

if __name__ == "__main__":
    main()
