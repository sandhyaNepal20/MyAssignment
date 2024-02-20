import tkinter as tk
from tkinter import Entry, Button, Label
from urllib.request import urlopen
from PIL import Image, ImageTk
from io import BytesIO
import threading
import os
from datetime import datetime

class SandhyaDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("Sandhya Image Downloader")

        self.url = Label(root, text="Enter image URL:")
        self.url.pack()

        self.url_bar = Entry(root, width=100)
        self.url_bar.pack()

        self.btn_download = Button(root, text="Download", command=self.download_image)
        self.btn_download.pack()

        self.btn_pause = Button(root, text="Pause", state=tk.DISABLED, command=self.pause_download)
        self.btn_pause.pack(side=tk.LEFT)

        self.btn_resume = Button(root, text="Resume", state=tk.DISABLED, command=self.resume_download)
        self.btn_resume.pack(side=tk.LEFT)

        self.btn_cancel = Button(root, text="Cancel", state=tk.DISABLED, command=self.cancel_download)
        self.btn_cancel.pack(side=tk.LEFT)

        self.status_label = Label(root, text="Status: Ready")
        self.status_label.pack()

        self.image = Label(root, text="Saved Image:")
        self.image.pack()

        self.image_res = tk.Canvas(root, width=400, height=400)
        self.image_res.pack()

        self.download_thread = None
        self.paused = False

    def download_image(self):
        if self.paused:
            self.resume_download()
        else:
            url = self.url_bar.get()
            if url:
                self.status_label.config(text="Status: Downloading")
                self.download_thread = threading.Thread(target=self.save_image, args=(url,))
                self.download_thread.start()
                self.btn_pause.config(state=tk.NORMAL)
                self.btn_cancel.config(state=tk.NORMAL)
                self.btn_download.config(state=tk.DISABLED)

    def save_image(self, url):
        try:
            response = urlopen(url)
            image_data = BytesIO(response.read())
            image = Image.open(image_data)
            image.thumbnail((400, 400))

            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

            filename = f"untitled_image_{timestamp}.jpg"
            save_path = os.path.join(os.getcwd(), filename)
            image.save(save_path)

            self.root.after(0, self.update_image, image)
            self.status_label.config(text="Status: Download Complete")

        except Exception as ex:
            self.status_label.config(text=f"Status: Error - {ex}")

    def update_image(self, image):
        tk_img = ImageTk.PhotoImage(image)

        self.image_res.config(width=tk_img.width(), height=tk_img.height())
        self.image_res.create_image(0, 0, anchor=tk.NW, image=tk_img)
        self.image_res.image = tk_img

    def pause_download(self):
        self.paused = True
        self.btn_pause.config(state=tk.DISABLED)
        self.btn_resume.config(state=tk.NORMAL)
        self.status_label.config(text="Status: Paused")

    def resume_download(self):
        self.paused = False
        self.btn_pause.config(state=tk.NORMAL)
        self.btn_resume.config(state=tk.DISABLED)
        self.status_label.config(text="Status: Resuming Download")

        self.download_image()

    def cancel_download(self):
        if self.download_thread and self.download_thread.is_alive():
            self.download_thread.join()
        self.btn_download.config(state=tk.NORMAL)
        self.btn_pause.config(state=tk.DISABLED)
        self.btn_resume.config(state=tk.DISABLED)
        self.btn_cancel.config(state=tk.DISABLED)
        self.status_label.config(text="Status: Download Cancelled")

def main():
    root = tk.Tk()
    app = SandhyaDownloader(root)
    root.mainloop()

if __name__ == "__main__":
    main()

# https://cdni.autocarindia.com/utils/imageresizer.ashx?n=https://cms.haymarketindia.net/model/uploads/modelimages/Hyundai-Grand-i10-Nios-200120231541.jpg&w=872&h=578&q=75&c=1