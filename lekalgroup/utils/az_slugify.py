def az_slugify(text):
    mapping = {
        'ə': 'e', 'Ə': 'E',
        'ç': 'c', 'Ç': 'C',
        'ğ': 'g', 'Ğ': 'G',
        'ı': 'i', 'İ': 'I',
        'ö': 'o', 'Ö': 'O',
        'ş': 's', 'Ş': 'S',
        'ü': 'u', 'Ü': 'U',
        ' ': '-',  
    }
    for az_char, en_char in mapping.items():
        text = text.replace(az_char, en_char)
    import re
    text = text.lower()
    text = re.sub(r'[^a-z0-9\-]', '', text)
    text = re.sub(r'-+', '-', text)
    text = text.strip('-')
    return text