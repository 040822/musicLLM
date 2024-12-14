import os
import json

def process_directory(directory, output_file):
    aggregated_data = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
                    mp3_file_path = os.path.splitext(file_path)[0] + ".mp3"
                    aggregated_data.append({
                        "path": mp3_file_path,
                        "duration": data.get("duration", None),
                        "sample_rate": data.get("sample_rate", None),
                        "description": data.get("description", None),
                        "keywords": data.get("keywords", None),
                        "bpm": data.get("bpm", None),
                        "genre": data.get("genre", None),
                        "title": data.get("title", None),
                        "name": data.get("name", None),
                        "instrument": data.get("instrument", None),
                        "moods": data.get("moods", None),
                        "file_extension": data.get("file_extension", None)
                    })

    with open(output_file, 'w', encoding='utf-8') as output_json_file:
        json.dump(aggregated_data, output_json_file, ensure_ascii=False, indent=4)
    print(f"Aggregated data written to {output_file}")

if __name__ == "__main__":
    directory = "audiocraft-main\dataset\game musics标记"  # 替换为你的JSON文件所在目录
    output_file = "aggregated_data.json"  # 输出文件名
    process_directory(directory, output_file)