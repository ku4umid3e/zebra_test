# Примеры данных и результатов

Эта папка содержит минимальный набор примеров для демонстрации работы модели.

## 📁 Структура

```
examples/
├── images/           # Примеры входных изображений (2-3 от каждого класса)
├── predictions/      # Результаты работы модели с визуализацией
└── README.md        # Этот файл
```

## 🗂️ Что НЕ включено в репозиторий (из-за размера >20ГБ):

- **Полный датасет:** `dataset/` и `YOLO_dataset/` (~20+ ГБ)
- **Все результаты экспериментов:** только лучший в `runs/segment/train/`
- **Исходное видео:** файлы *.mp4/*.avi
- **Все веса моделей:** только `best.pt` лучшей модели

## ✅ Что ВКЛЮЧЕНО для оценки работы:

- **Код:** все Python скрипты
- **Конфигурация:** `data.yaml`, `requirements.txt`
- **Результаты лучшего эксперимента:** метрики, графики, веса
- **Документация:** `report.md`, `README.md`
- **Примеры:** несколько изображений и предсказаний (здесь)

## 🔄 Воспроизведение полных результатов

Для полного воспроизведения потребуется:
1. Исходное видео (предоставляется отдельно)
2. Выполнить весь pipeline согласно `report.md`
3. Или использовать готовую модель `runs/segment/train/weights/best.pt` 