import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videocaptureobject.read()
        print(ret)
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    videocaptureobject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.BHzPz73VgcaZUxbw-t95Z0eopAYr_Z5_SV56FvHPlSXF9Gn6wPG7QJuUktX_ldm4CNNwoNs6vw0hoZ7xi-qhMTMfGJLpL4E-a4QGyPOKcS0-3M8GmzP-qs6Aj7KRoazoRlM6yoyUbsUx"
    file_from = img_name
    file_to = "/testfolder/" + (img_name)
    dbx = dropbox.Dropbox(access_token)

    with open (file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to, mode = dropbox.files.WriteMode.overwrite)
        print("files uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name = take_snapshot()
            upload_file(name)

main()

