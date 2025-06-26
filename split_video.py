import os
import argparse
import subprocess
import sys

# Список поддерживаемых расширений видео
VIDEO_EXTS = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm', '.mpg', '.mpeg', '.m4v']

def main():
    parser = argparse.ArgumentParser(description='Разложение видео на кадры')
    parser.add_argument('--fps', type=float, default=1.5, help='Кадры в секунду (по умолчанию: 1.5)')
    parser.add_argument('--input-dir', default='.', help='Директория с видео (по умолчанию: текущая)')
    args = parser.parse_args()

    # Проверка наличия ffmpeg
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Ошибка: ffmpeg не найден! Установите ffmpeg.", file=sys.stderr)
        sys.exit(1)

    # Обработка видеофайлов
    for filename in os.listdir(args.input_dir):
        filepath = os.path.join(args.input_dir, filename)
        
        if os.path.isfile(filepath):
            ext = os.path.splitext(filename)[1].lower()
            if ext in VIDEO_EXTS:
                # Создаем директорию для кадров
                output_dir = os.path.splitext(filepath)[0]
                os.makedirs(output_dir, exist_ok=True)
                
                # Формируем путь для сохранения кадров
                output_pattern = os.path.join(output_dir, 'image-%04d.png')
                
                # Команда для ffmpeg
                cmd = [
                    'ffmpeg',
                    '-i', filepath,
                    '-vf', f'fps={args.fps}',
                    '-q:v', '2',
                    output_pattern
                ]
                
                print(f"Обработка: {filename} -> {output_dir}")
                try:
                    subprocess.run(cmd, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Ошибка при обработке {filename}: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()
