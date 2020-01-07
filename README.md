# About
Automate file categorization and keep your download folder clutter free! (**Linux only**)

### How to use:

1. Download the zip file

2. Move the Download_Cleanup script to a permanent location ( I recommend a folder in your documents folder):
    > **Terminal**: mkdir Documents/DownloadCleanupScript
    mv Download_Cleanup 
    **Terminal:** /home/<user>/Documents/DownloadCleanupScript/
    (***Remember where this location is***)

3. Move the DownloadCleanup.service file to the system folder: 
    > **Terminal:** mv DownloadCleanup.service /etc/systend/system/ 
    Edit the DownloadCleanup.service to indicate script location and user
    **Terminal:** sudo nano DownloadCleanup.service
    Change user to your user (***User='user'***)
    Change ExecStart to the directory of your script (***ExecStart=/usr/bin/python3 /'directory of script'/DownloadCleanup***)
    
4. Create folders for script to send files to:
    > mkdir Documents/{PDF_Files, DEB_Files, Image_Files, Text_Files, Spreadsheet_Files, Random_Files}

### Add further categorizing directories:
1. Add another elif statement in the scrip:
    > elif filename.endswith(('.FileTpye'....'.FileType')):
        src = folder_to_track + "/" + filename
        new_destination_name = destination_name + "/" + filename
        os.rename(src, new_destination_name)
2. Add another destination folder above the others at the bottom of the script:
    > 'new_destination' = "/home/'user'/Documents/new_folder"
        
#### Any questions please contact me @:
***ggushurst@gmail.com***

##### Enjoy a clean download folder!
