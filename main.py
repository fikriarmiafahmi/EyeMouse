import cv2

# Fungsi untuk mendeteksi koordinat mata secara real-time
def detect_eyes_realtime():
    # Load cascade classifier mata dari OpenCV
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    # Inisialisasi kamera
    video_capture = cv2.VideoCapture(0)  # Nomor 0 menunjukkan kamera utama, Anda dapat mengubahnya jika memiliki lebih dari satu kamera

    while True:
        # Baca frame dari kamera
        ret, frame = video_capture.read()

        # Konversi frame menjadi grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Deteksi mata pada frame
        eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Menggambar kotak pada mata yang terdeteksi
        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Tampilkan koordinat mata
            print("Koordinat Mata: x =", x, "y =", y)

        # Tampilkan frame dengan kotak mata yang terdeteksi
        cv2.imshow('Deteksi Mata Real-time', frame)

        # Berhenti jika tombol 'q' ditekan
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Setelah selesai, tutup kamera dan jendela tampilan
    video_capture.release()
    cv2.destroyAllWindows()

# Panggil fungsi untuk mendeteksi mata secara real-time
detect_eyes_realtime()
