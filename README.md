# Filem Jepang

![](https://github.com/filemjepang/Bikin-Filem/blob/main/banner_fj.png)

## Install 

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

## Tambah Watermark

```
ffmpeg -i <video> -vf "drawtext=text='@filemjepang':fontcolor=white:fontsize=24:x=w-tw-20:y=h-th-20" -codec:a copy <output>
```

## Perbesar Suara 2x

```
ffmpeg -i <video> -vcodec copy -af "volume=2.0" <output>
```
