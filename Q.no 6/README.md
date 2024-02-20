This application creates a simple Tkinter GUI with an entry widget for the image URL, a download button, and a canvas to display the downloaded image. Here multithreading is implemented as: the start_download method creates a new thread for downloading the image. The save_image method is run in the new thread, and it downloads the image using the request library. The image saved is then displayed in the UI using the update_image method.


Here the breakdown:

1) Libraries used:
      Tinkinter : For the GUI purpose. The background canvas, save button, url field and so on.
      PIL : Library used for image processing
      IO (BytesIO) : For binary data like file object
      Threading : For creating and managing threads
      OS : For saving the file in the device
      Datetime : I used this library for naming the file so no replacement of image occurs

2) SandhyaDownloader
      Main class for the download purpose. Contains four separate methods inside of it
      Init method : The constructor method that is used to initialize the instance of the class
      All the labels, bars, buttons are placed in the class and the method

3) download_image method:
      Here we defined the method for initiating download of image. We get the url from the url
      field and creates a new thread with target function and pass the argument.

4) save_image:
      We have try catch exception block over here where we sends the HTTP get request to the given
      URL and receives the response. The Binary object that is received on the response is used and PIL
      module is used to open the image. The image is then stored in the res of 400 * 400 with fixed aspect ratio.
      Then the update_image method is scheduled after the current image is completely processed

5) update_image:
      This updates the canvas on the screen with the image. The PIL image is converted to tkinter
      image object. The dimension is updated to match the image.

8) Pause, Resume, and Cancel

      Pause (pause Button):Pauses the ongoing download process. No new downloads can be initiated while paused.

      Resume (Resume Button): Resumes the download process after a pause.

      Cancel (Cancel Button): Cancels ongoing downloads and allows for a fresh start. This action terminates all existing threads and creates a new thread pool.

7) main method:.
      This is the main function for running the application. Here we created the main
      Tkinter window. The instance of the SandhyaDownloader is also created here. Also the mainloop
      enters to start the GUI application.

Things to keep in mind : Python must be installed in your system along with the libraries like tkinter, urllib,
PIL, IO, OS, datetime. You can always use the pip installation process to install any of the libraries.
