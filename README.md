# Install 

```
apt-get update
apt-get install ffmpeg 
```

## Potong Video 

```
ffmpeg -ss <durasi_awal> -to <durasi_akhir> -i <video> -c copy <output>
```

## Crot 1:1 Video

```
ffmpeg -i <video> -filter:v "crop='min(iw\,ih)':'min(iw\,ih)':(iw-min(iw\,ih))/2:(ih-min(iw\,ih))/2" -c:a copy <output>
```

## Perbesar Suara 2x

```
ffmpeg -i <video> -vcodec copy -af "volume=2.0" <output>
```

## Tambah Watermark

```
ffmpeg -i <video> -vf "drawtext=text='@filemjepang':fontcolor=white:fontsize=24:x=w-tw-20:y=h-th-20" -codec:a copy <output>
```

# Subtitle 

## 1. Instal Python3

```
sudo apt-get update 
sudo apt-get install python3 python3-pip
```

## 2. Buat Virtual Enviroment

```
python3 -m venv venv
```

## 3. Aktifkan Virtual Enviroment 

```
source bin/activate
```

## 4. Instal Modul 

```
pip3 install openai-whisper moviepy argostranslate srt
```

## Run

```
python3 subtitle_gen.py --help
```
