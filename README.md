## ID3GUI
Unsurprisingly, a shoddy GUI to automate issuing [id3v2](https://github.com/myers/id3v2) commands, built with Python and brain damage.

### 📖 Contents
+ [About](#about)
+ [Features](#features)
+ [Prerequisites](#prerequisites)
+ [Running the dang thing](#Usage)
+ [Why](#motivation)

### ❓ About
ID3GUI is a graphical interface to batch rename and tag entire albums of songs. Specifically, it issues id3v2 commands in order to tag .mp3 files; turning untagged trainwrecks like:
>1 - Song_Title - BAND.mp3  

into a neatly tagged:
>Song_Title.mp3

I am no audio codec expert, but it appears to be able to tag .flac files in much the same way.  
This is far from the best way of doing it, but it is what works for me and thus it is what I decide to chuck into this repo.

### 🛠️ Features
- **Set up ID3 tags for Artists, Albums, Release Year, Genre, Track Number and Song Title in one fell swoop**
- **Extract an album's song titles from filenames and batch rename said files**
- **100% idiot coded, not a single shred of AI used in this crime against python**

### ✅ Prerequisites
+ id3v2 installed on your system (https://id3v2.sourceforge.net)
+ Python 3.7 or greater

### ⌨️ Usage

```sh
git clone https://github.com/Randoodl/ID3GUI
cd ID3GUI
python ./src/main.py
```

Assuming you have an assortment of untagged songs from one album chucked in a directory as such:
>AlbumTitle/   
>├─ 1_Song_Band_AlbumTitle.mp3  
>├─ 2_Another Song_Band_AlbumTitle.mp3  
>...  
>└─ 10_Final Song_Band_AlbumTitle.mp3  

You can simply navigate to the directory, manually set the song title extraction range, set up the tags as needed and hit the Encode button. Which would leave you with a neat:

>AlbumTitle/   
>├─ Song.mp3  
>├─ Another Song.mp3  
>...  
>└─ Final Song.mp3  

> [!WARNING]  
> This will mess up your files if you're not careful. It is highly recommended to back up your .mp3s before you work on them. 
Ask me how I know.

### 🔍 Motivation
The sudden decision to organise my several decades' worth of songs came with the equally sudden and sinking realisation that hardly any of them were titled or tagged correctly.  
Now, I am too lazy to automate everything with a bash script, but I am not above wasting a few days shoddily cobbling together a GUI to ease the pain of tagging aforementioned collection.  
Perhaps, this abomination of patched together bits and bobs of python can resemble enough of a program to be useful to someone else, too.