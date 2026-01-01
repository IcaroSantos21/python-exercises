import json

def save_json(file_name, data):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            users = data
            json.dump(users, file, ensure_ascii=False, indent=4)
        return f'Dados salvo com sucesso em {file_name}'
    except Exception as e:
        return f'Erro ao salvar o arquivo\n \
              Error name: {e}'

def load_json(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []