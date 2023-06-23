phone_book = []
path = 'phones.txt'


def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        user_id, name, phone, comment, *_ = contact.strip().split(':')
        phone_book.append({'id': user_id, 'name': name, 'phone': phone, 'comment': comment})
    
def save_file():
    data = []
    for i, contact in enumerate(phone_book):
        i += 1
        new = ':'.join([str(i), contact.get('name'), contact.get('phone'), contact.get('comment')])
        data.append(new)
    data = '\n'.join(data)    
    with open(path, 'w', encoding = 'UTF-8') as file:
        file.write(data)

def check_id():
    uid_list = []
    for contact in phone_book:
        uid_list.append(int(contact.get('id')))    
    if uid_list:
        return {'id': max(uid_list) + 1}
    else:
        return {'id': 1}


def add_contact(new: dict): 
    new.update(check_id())
    phone_book.append(new)
    
def search(word: str) -> list[dict]:
    result = []
    for contact in phone_book:
        for key, value in contact.items():
            if word.lower() in value.lower():
                result.append(contact)
                break
    return result


def change(index: int, new: dict[str, str]):
    for key, field in new.items():
        if field != '':
            phone_book[index - 1][key] = field
            
def remove(index: str):
    del_cnt = phone_book.pop(int(index) - 1)
    return del_cnt
    