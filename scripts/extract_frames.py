import cv2
import os

# Video dosyaları ve çıktı klasörleri
videos = {
    "videos/UAI_ISIKLI.mp4": "extracted_frames/UAI_ISIKLI",
    "videos/UAI_ISIKSIZ.mp4": "extracted_frames/UAI_ISIKSIZ",
    "videos/UAP_ISIKLI.mp4": "extracted_frames/UAP_ISIKLI",
    "videos/UAP_ISIKSIZ.mp4": "extracted_frames/UAP_ISIKSIZ"
}

# Her videodan alınacak frame sayısı
TARGET_FRAMES = 500

for video_path, output_folder in videos.items():

    print(f"\nİşleniyor: {video_path}")

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Video açılamadı: {video_path}")
        continue

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print(f"Toplam frame sayısı: {total_frames}")

    # Kaçar kaçar frame alınacağını hesapla
    step = max(total_frames // TARGET_FRAMES, 1)

    saved_count = 0
    frame_id = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Belirli aralıklarla frame kaydet
        if frame_id % step == 0:

            frame_name = f"{saved_count:04d}.jpg"
            save_path = os.path.join(output_folder, frame_name)

            cv2.imwrite(save_path, frame)

            saved_count += 1

            print(f"Kaydedildi: {save_path}")

            # 500 frame olunca dur
            if saved_count >= TARGET_FRAMES:
                break

        frame_id += 1

    cap.release()

    print(f"{saved_count} adet frame kaydedildi.")

print("\nTüm işlemler tamamlandı.")