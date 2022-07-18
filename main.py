from tkinter import *
from tkinter.ttk import Combobox
from pytube import YouTube


FONT_NAME = "Edu VIC WA NT Beginner"
BACKGROUND_COLOR = "#FAD9A1"
FOREGROUND_COLOR = "#BD4B4B"
QUALITY_LIST = ["144p", "240p", "360p", "480p", "720p", "1080p"]
DOWNLOAD_DIRECTORY = 'C:/Users/User/Downloads'


def get_video_url():
    youtube_object = YouTube(url=url_field.get())
    return youtube_object


def download_video():
    get_video_url().streams.filter(resolution=quality_list.get(), file_extension='mp4') \
        .first().download(output_path=DOWNLOAD_DIRECTORY)


def detailed_window():
    # TODO: Creating window.
    window_2 = Toplevel(window)
    window_2.title("Video Details")
    window_2.iconphoto(False, photo)
    window_2.config(width=500, height=550, background=BACKGROUND_COLOR)

    # TODO: Creating a labels.
    name_label = Label(window_2, text="Name :", font=(FONT_NAME, 11, "bold"), bg=BACKGROUND_COLOR)
    name_label.place(x=100, y=300)

    length_label = Label(window_2, text="Length :", font=(FONT_NAME, 11, "bold"), bg=BACKGROUND_COLOR)
    length_label.place(x=100, y=330)

    publish_date_label = Label(window_2, text="Publish Date :", font=(FONT_NAME, 11, "bold"), bg=BACKGROUND_COLOR)
    publish_date_label.place(x=100, y=360)

    views_label = Label(window_2, text="Views :", font=(FONT_NAME, 11, "bold"), bg=BACKGROUND_COLOR)
    views_label.place(x=100, y=390)

    description_label = Label(window_2, text="Description :", font=(FONT_NAME, 11, "bold"), bg=BACKGROUND_COLOR)
    description_label.place(x=100, y=420)

    # TODO: Creating a text boxs.
    name_text = Text(window_2, state=NORMAL, width=35, height=1, highlightthickness=0, border=False,
                     bg=BACKGROUND_COLOR)
    name_text.place(x=160, y=305)

    length_text = Text(window_2, state=NORMAL, width=20, height=1, highlightthickness=0, border=False,
                       bg=BACKGROUND_COLOR)
    length_text.place(x=160, y=337)

    publish_date_text = Text(window_2, state=NORMAL, width=20, height=1, highlightthickness=0, border=False,
                             bg=BACKGROUND_COLOR)
    publish_date_text.place(x=200, y=364)

    views_text = Text(window_2, state=NORMAL, width=20, height=1, highlightthickness=0, border=False,
                      bg=BACKGROUND_COLOR)
    views_text.place(x=160, y=397)

    description_text = Text(window_2, state=NORMAL, width=35, height=7, highlightthickness=0, border=False,
                            bg=BACKGROUND_COLOR)
    description_text.place(x=190, y=427)

    # TODO: Getting video details from entries.
    name_text.insert(INSERT, get_video_url().title)

    # TODO: Check if the length of the video is greater than 60 sec.
    if get_video_url().length < 60:
        length_text.insert(INSERT, str(get_video_url().length))
    else:
        length_text.insert(INSERT, str(divmod(get_video_url().length, 60)))

    views_text.insert(INSERT, str(get_video_url().views))
    publish_date_text.insert(INSERT, str(get_video_url().publish_date))
    description_text.insert(INSERT, get_video_url().description)

    # TODO: Creating a canvas.
    canvas_2 = Canvas(window_2, width=256, height=160, highlightthickness=0)
    placeholder_img = PhotoImage(get_video_url().thumbnail_url)
    canvas_2.create_image(128, 128, image=placeholder_img)
    canvas_2.place(x=130, y=50)


# ---------------------------- UI SETUP ------------------------------- #

# TODO: Creating window.
window = Tk()
photo = PhotoImage(file="images/youtube.ico")
window.iconphoto(False, photo)
window.title("YouTube Downloader")
window.config(width=600, height=400, bg=BACKGROUND_COLOR)

# TODO: Creating a canvas.
canvas = Canvas(width=300, height=167, bg=BACKGROUND_COLOR, highlightthickness=0)
logo_img = PhotoImage(file="images/yt_logo.png")
canvas.create_image(150, 83, image=logo_img)
canvas.place(x=150, y=20)

# TODO: Creating a label.
url_label = Label(text="Url :", font=(FONT_NAME, 11, "bold"), bg=BACKGROUND_COLOR, fg="black")
url_label.place(x=150, y=245)

quality_label = Label(text="Choose quality :", font=(FONT_NAME, 11, "bold"), bg=BACKGROUND_COLOR, fg="black")
quality_label.place(x=80, y=270)

# TODO: Creating entries.
url_field = Entry(width=40)
url_field.focus()
url_field.place(x=190, y=250)

# TODO: Creating a combobox.
quality_list = Combobox(width=37, values=QUALITY_LIST)
quality_list.place(x=190, y=280)

# TODO: Creating a button.
download_button = Button(text="Download", width=30, command=download_video)
download_button.place(x=203, y=320)

details_button = Button(text="Get Details", width=30, command=detailed_window)
details_button.place(x=203, y=350)

window.mainloop()
