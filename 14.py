from PIL import Image
import face_recognition

image = face_recognition.load_image_file("C:/Users/MECHREVO/Desktop/84315d9b4c8e4947db3ad514ec0e642f.jpg")
face_locations = face_recognition.face_locations(image)

n=1
for face_location in face_locations:
    top, right, bottom, left = face_location
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save(f"C:/Users/MECHREVO/Desktop/84315d9b4c8e4947db3ad514ec0e642f{n}.jpg")
    n=n+1
    