import json
import urllib.request
import ssl
from deep_translator import GoogleTranslator

# Download original JSON
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request("https://raw.githubusercontent.com/cypressf/dominion/master/cards.json")
try:
    with urllib.request.urlopen(req, context=ctx) as response:
        data = json.loads(response.read().decode())
except Exception as e:
    print("Error downloading JSON:", e)
    data = {}

# Add Empires
data['Empires'] = [
    { 'name': 'Archive', 'description': "Action - Duration" },
    { 'name': 'Capital', 'description': "Treasure" },
    { 'name': 'Castles', 'description': "Victory - Castle" },
    { 'name': 'Catapult / Rocks', 'description': "Action - Attack" },
    { 'name': 'Chariot Race', 'description': "Action" },
    { 'name': 'Charm', 'description': "Treasure" },
    { 'name': 'City Quarter', 'description': "Action (8 Debt)" },
    { 'name': 'Crown', 'description': "Action - Treasure" },
    { 'name': 'Encampment / Plunder', 'description': "Action / Treasure" },
    { 'name': 'Enchantress', 'description': "Action - Attack - Duration" },
    { 'name': 'Engineer', 'description': "Action (4 Debt)" },
    { 'name': 'Farmers\' Market', 'description': "Action - Gathering" },
    { 'name': 'Forum', 'description': "Action" },
    { 'name': 'Gladiator / Fortune', 'description': "Action / Treasure" },
    { 'name': 'Groundskeeper', 'description': "Action" },
    { 'name': 'Legionary', 'description': "Action - Attack" },
    { 'name': 'Overlord', 'description': "Action (8 Debt)" },
    { 'name': 'Patrician / Emporium', 'description': "Action" },
    { 'name': 'Royal Blacksmith', 'description': "Action (8 Debt)" },
    { 'name': 'Sacrifice', 'description': "Action" },
    { 'name': 'Settlers / Bustling Village', 'description': "Action" },
    { 'name': 'Temple', 'description': "Action - Gathering" },
    { 'name': 'Villa', 'description': "Action" },
    { 'name': 'Wild Hunt', 'description': "Action - Gathering" }
]

translator = GoogleTranslator(source='en', target='nl')
translations = {}

# Gather text
all_texts = []
card_map = [] # stores (name, is_desc, original_text)

for set_name, cards in data.items():
    for c in cards:
        if 'Bogus' in c['name']: continue
        name = c['name']
        desc = c.get('description', '')
        
        # We will translate name and description separately
        if name not in translations:
            translations[name] = {'name': '', 'description': ''}
            all_texts.append(name)
            card_map.append((name, 'name'))
            
            if desc:
                all_texts.append(desc)
                card_map.append((name, 'description'))

print(f"Translating {len(all_texts)} strings...")

# Batch translation to avoid limits (Google translate usually handles up to 5k chars per request)
# But deep-translator handles batching natively if we use translate_batch
translated_texts = []
batch_size = 50
for i in range(0, len(all_texts), batch_size):
    batch = all_texts[i:i+batch_size]
    try:
        translated_batch = translator.translate_batch(batch)
        translated_texts.extend(translated_batch)
    except Exception as e:
        print("Error translating batch:", e)
        # fallback
        for text in batch:
            try:
                translated_texts.append(translator.translate(text))
            except:
                translated_texts.append(text)

# Assign back to translations dict
for i, (name, field) in enumerate(card_map):
    translations[name][field] = translated_texts[i]
    
# Handle edge case type names
type_translations = {
    'Action': 'Actie',
    'Treasure': 'Schat',
    'Victory': 'Overwinning',
    'Attack': 'Aanval',
    'Reaction': 'Reactie',
    'Duration': 'Duur',
    'Castle': 'Kasteel',
    'Gathering': 'Verzameling'
}

js_content = f"""// Auto-generated Dutch translations
const nlTranslations = {json.dumps(translations, indent=2)};
const nlTypes = {json.dumps(type_translations, indent=2)};
"""

with open('nl_translations.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Translation complete! Written to nl_translations.js")
