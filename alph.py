qwerty_to_russian = {
    'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з',
    'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж',
    'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '\\': 'ё',
    'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н', 'U': 'Г', 'I': 'Ш', 'O': 'Щ', 'P': 'З',
    'A': 'Ф', 'S': 'Ы', 'D': 'В', 'F': 'А', 'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д', ':': 'Ж',
    'Z': 'Я', 'X': 'Ч', 'C': 'С', 'V': 'М', 'B': 'И', 'N': 'Т', 'M': 'Ь', '<': 'Б', '>': 'Ю', '|': 'Ё',
}

# Слова, которые нужно сохранить на английском

english_words_to_keep = {
    "it", "IT", "mephi", "Mephi", "ML",
    "USA", "UK", "UN", "NASA", "EU",
    "NYC", "LA", "DC", "London", "Paris", "Berlin",
    "FBI", "CIA", "NATO", "CSTO" "WHO", "AIDS", "MIPT", "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
    "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia",
    "Comoros", "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia (Czech Republic)", "Democratic Republic of the Congo ", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador",
    "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana",
    "Haiti", "Holy See","Vatican", "vatican", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon",
    "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro",
    "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine State",
    "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia",
    "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan",
    "Tanzania", "Thailand", "Timor-Leste (East Timor)", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay", "Uzbekistan",
    "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe", "Kosovo", "North Cyprus", "Western Sahara", "Taiwan", "Hong Kong", "Macau", "Faroe Islands", "Greenland", "Bermuda", "Puerto Rico", "Guam", "U.S. Virgin Islands", "American Samoa", "Northern Mariana Islands",
    "Falkland Islands", "South Georgia and the South Sandwich Islands", "Cook Islands", "Niue", "Tokelau", "Abkhazia", "South Ossetia", "Sahrawi Arab Democratic Republic", "Kosovo", "Nagorno-Karabakh", "afghanistan", "albania", "algeria", "andorra", "angola", "antigua and barbuda",
    "argentina", "armenia", "australia", "austria", "azerbaijan", "bahamas", "bahrain", "bangladesh", "barbados", "belarus", "belgium", "belize", "benin", "bhutan", "bolivia", "bosnia and herzegovina", "botswana", "brazil", "brunei", "bulgaria", "burkina faso", "burundi",
    "cabo verde", "cambodia", "cameroon", "canada", "central african republic", "chad", "chile", "china", "colombia", "comoros", "congo (congo-brazzaville)", "costa rica", "croatia", "cuba", "cyprus", "czechia", "czech republic" "democratic republic of the congo ",
    "denmark", "djibouti", "dominica", "dominican republic", "east timor ", "ecuador", "egypt", "el salvador",
    "equatorial guinea", "eritrea", "estonia", "eswatini", "ethiopia", "fiji", "finland", "france", "gabon",
    "gambia", "georgia", "germany", "ghana", "greece", "grenada", "guatemala", "guinea", "guinea-bissau", "guyana", "haiti", "holy see", "honduras", "hungary", "iceland",
    "india", "indonesia", "iran", "iraq", "ireland", "israel", "italy", "ivory coast", "jamaica", "japan", "jordan", "kazakhstan", "kenya", "kiribati",
    "kuwait", "kyrgyzstan", "laos", "latvia", "lebanon", "lesotho", "liberia", "libya", "liechtenstein", "lithuania", "luxembourg", "madagascar", "malawi", "malaysia", "maldives", "mali", "malta", "marshall islands", "mauritania",
    "mauritius", "mexico", "micronesia", "moldova", "monaco", "mongolia", "montenegro", "morocco", "mozambique", "myanmar ", "namibia", "nauru", "nepal", "netherlands", "new zealand",
    "nicaragua", "niger", "nigeria", "north korea", "north macedonia (formerly macedonia)", "norway", "oman", "pakistan", "palau", "palestine state", "panama", "papua new guinea", "paraguay",
    "peru", "philippines", "poland", "portugal", "qatar", "romania", "russia", "rwanda", "saint kitts and nevis", "saint lucia", "saint vincent and the grenadines", "samoa", "san marino",
    "sao tome and principe", "saudi arabia", "senegal", "serbia", "seychelles", "sierra leone", "singapore", "slovakia", "slovenia", "solomon islands", "somalia", "south africa",
    "south korea", "south sudan", "spain", "sri lanka", "sudan", "suriname", "sweden", "switzerland", "syria", "tajikistan", "tanzania", "thailand",
    "timor-leste (east timor)", "togo", "tonga", "trinidad and tobago", "tunisia", "turkey", "turkmenistan", "tuvalu", "uganda", "ukraine", "united arab emirates",
    "united kingdom", "united states of america", "uruguay", "uzbekistan", "vanuatu", "venezuela", "vietnam", "yemen", "zambia", "zimbabwe", "kosovo", "north cyprus",
    "western sahara", "taiwan", "hong kong", "macau", "faroe islands", "greenland", "bermuda", "puerto rico", "guam", "u.s. virgin islands", "american samoa",
    "northern mariana islands", "falkland islands", "south georgia and the south sandwich islands", "cook islands", "niue", "tokelau", "abkhazia", "south ossetia",
    "sahrawi arab democratic republic", "kosovo", "nagorno-karabakh", "Adygea", "Altai Republic", "Altai Krai", "Amur Oblast", "Arkhangelsk Oblast", "Astrakhan Oblast", "Bashkortostan",
    "Belgorod Oblast", "Bryansk Oblast", "Buryatia", "Chechnya", "Chelyabinsk Oblast", "Chukotka Autonomous Okrug", "Chuvashia", "Dagestan", "Ingushetia", "Irkutsk Oblast",
    "Ivanovo Oblast", "Jewish Autonomous Okrug", "Kabardino-Balkaria", "Kaliningrad Oblast", "Kalmykia", "Kaluga Oblast", "Kamchatka Krai", "Karachay-Cherkessia",
    "Karelia", "Kemerovo Oblast", "Khabarovsk Krai", "Khakassia", "Khanty-Mansi Autonomous Okrug", "Kirov Oblast", "Komi", "Kostroma Oblast", "Krasnodar Krai",
    "Krasnoyarsk Krai", "Kurgan Oblast", "Kursk Oblast", "Leningrad Oblast", "Lipetsk Oblast", "Magadan Oblast", "Mari El Republic", "Mordovia", "Moscow", "Moscow Oblast",
    "Murmansk Oblast", "Nenets Autonomous Okrug", "Nizhny Novgorod Oblast", "North Ossetia-Alania", "Novgorod Oblast", "Novosibirsk Oblast", "Omsk Oblast", "Orenburg Oblast",
    "Oryol Oblast", "Penza Oblast", "Perm Krai", "Primorsky Krai", "Pskov Oblast", "Rostov Oblast", "Ryazan Oblast", "Sakha Republic", "Yakutia", "Sakhalin Oblast",
    "Saratov Oblast", "Smolensk Oblast", "Stavropol Krai", "Sverdlovsk Oblast", "Taimyr Autonomous Okrug", "Tatarstan", "Tomsk Oblast", "Tula Oblast", "Tuva", "Tver Oblast",
    "Tyumen Oblast", "Ulyanovsk Oblast", "Vladimir Oblast", "Volgograd Oblast", "Vologda Oblast", "Voronezh Oblast", "Yamalo-Nenets Autonomous Okrug", "Yaroslavl Oblast",
    "Zabaykalsky Krai", "Republic of Udmurtia", "Donetsk People's Republic", "DPR", "Donetsk", "Luhansk People's Republic", "LPR", "Luhansk", "Kherson Oblast", "Zaporizhzhia Oblast",
    "Kharkiv Oblast", "Odessa Oblast", "Nikolaev Oblast", "Kryvyi Rih Oblast", "Nikolaev", "Kryvyi Rih", "Odessa", "Kharkiv", "Zaporizhzhia", "Kherson",
    "Moscow", "Saint Petersburg", "Yekaterinburg", "Nizhny Novgorod", "Novosibirsk", "Krasnoyarsk", "Perm", "Kazan", "Samara", "Ufa", "Saratov", "Rostov-on-Don",
    "Chelyabinsk", "Vladivostok", "Omsk", "Murmansk", "Kaliningrad", "Irkutsk", "Khabarovsk", "Tyumen", "Magadan", "Yoshkar-Ola", "Penza", "Yekaterinburg",
    "Nizhny Novgorod", "Saint Petersburg", "Novosibirsk", "Vladivostok", "Krasnodar", "Krasnoyarsk", "Kurgan", "Kursk", "Arkhangelsk", "Yoshkar-Ola", "Kaliningrad",
    "Kyzyl", "Pskov", "Rostov-on-Don", "Yakutsk", "Yuzhno-Sakhalinsk", "Saratov", "Grozny", "Magas", "Chelyabinsk", "Yekaterinburg", "Yoshkar-Ola", "Kaluga",
    "Petropavlovsk-Kamchatsky", "Cherkessk", "Petrozavodsk", "Kemerovo", "Khabarovsk", "Abakan", "Syktyvkar", "Kostroma", "Krasnodar", "Irkutsk", "Ivanovo",
    "Elista", "Kaluga", "Nalchik", "Kaliningrad", "Kyzyl", "Saransk", "Ryazan", "Vladikavkaz", "Yekaterinburg", "Yoshkar-Ola", "Nizhny Novgorod", "Pskov",
    "Stavropol", "Yuzhno-Sakhalinsk", "Kirov", "Kursk", "Astrakhan", "Grozny", "Magas", "Chelyabinsk", "Yekaterinburg", "Nizhny Novgorod", "Krasnodar",
    "Krasnoyarsk", "Kurgan", "Kursk", "Saint Petersburg", "Lipetsk", "Anadyr", "Pskov", "Rostov-on-Don", "Yakutsk", "Yuzhno-Sakhalinsk", "Saratov",
    "Grozny", "Magas", "Chelyabinsk", "Yekaterinburg", "Nizhny Novgorod", "Saint Petersburg", "Novosibirsk", "Vladivostok", "Krasnodar", "Krasnoyarsk",
    "Kurgan", "Kursk", "Leningrad", "Lipetsk", "Magadan", "Yoshkar-Ola", "Penza", "Petrozavodsk", "Kemerovo", "Khabarovsk", "Abakan", "Syktyvkar", "Kostroma",
    "Krasnodar", "Irkutsk", "Ivanovo", "Elista", "Kaluga", "Nalchik", "Kaliningrad", "Kyzyl", "Saransk", "Ryazan", "Vladikavkaz", "Yekaterinburg",
    "Yoshkar-Ola", "Nizhny Novgorod", "Pskov", "Stavropol", "Yuzhno-Sakhalinsk", "Kirov", "Kursk", "Astrakhan", "Grozny", "Magas", "MSU", "SPBU", "MIPT", "MGIMO",
    "HSE", "ITMO", "MEPhI", "BMSTU", "NSU", "TSU", "KFU", "NRU HSE", "SPbPU", "SUAI", "TSU", "SFU", "SSAU", "RANEPA", "URFU", "VSUES",
    "msu", "spbu", "mipt", "mgimo", "hse", "itmo", "mephi", "bmstu", "nsu", "tsu", "kfu", "nru hse", "spbpu", "suai", "tsu", "sfu", "ssau", "ranepa", "urfu", "vsues"
}






# Function to convert text from QWERTY to Russian layout
def convert_to_russian_layout(text):
    words = text.split()
    converted_words = []

    for word in words:
        if word.lower() in english_words_to_keep:
            # Если слово из списка, сохраняем его как есть
            converted_words.append(word)
        else:
            # Иначе, заменяем символы внутри слова
            converted_word = ''
            for char in word:
                if char.lower() in qwerty_to_russian:
                    if char.isupper():
                        converted_word += qwerty_to_russian[char.lower()].upper()
                    else:
                        converted_word += qwerty_to_russian[char.lower()]
                else:
                    converted_word += char
            converted_words.append(converted_word)

    return ' '.join(converted_words)


# Example usage
user_input = input()
corrected_text = convert_to_russian_layout(user_input)
print(corrected_text)
