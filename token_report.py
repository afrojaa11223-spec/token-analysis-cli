import tiktoken
import unicodedata
import re
import argparse


#canonical normalization

Price_per_million = 2.0 

ZERO_WIDTH = ['\u200b', '\u200c', '\u200d', '\ufeff']

def canonical(text):
    normalized =  unicodedata.normalize('NFKC', text)

    for z in ZERO_WIDTH:
        normalized = normalized.replace(z, "")

    normalized = re.sub(r'\s+', " ", normalized).strip()
    return normalized

#api cost calculation

def calculate_cost(tokens, price_per_million=Price_per_million):
    cost = (tokens/1000000)*price_per_million
    return cost

#text analysis

def analyses(text):
    clean_text = canonical(text)
    token_ids = enc.encode(clean_text)
    characters = len(clean_text)
    original_characters = len(text)
    bytes_count = len(clean_text.encode('utf-8'))
    tokens = len(token_ids)
    bytes_per_token = bytes_count/tokens if tokens else 0
    cost = calculate_cost(tokens)    

    print("\n--- TEXT ANALYSIS ---")

    print("Original characters:", original_characters)
    print("Normalized Characters:", characters)
    print("Bytes:", bytes_count)
    print("Tokens:", tokens)
    print("Bytes per token:", round(bytes_per_token, 2))
    print("Estimated API cost: $", format(cost, '.8f'))

#normalization comparison

def compare_normalization(text):
    before_tokens= len(enc.encode(text))
    clean_text = canonical(text)
    after_tokens= len(enc.encode(clean_text))

    print("\n--- NORMALIZATION ---")

    print("Before normalization:", before_tokens)
    print("After normalization:", after_tokens)

    print("Normalized text:", repr(clean_text))

#token visualization
def visualize(text):
    token_ids = enc.encode(canonical(text))
    pieces = []
    for token_id in token_ids:
        raw_piece = enc.decode_single_token_bytes(token_id)
        piece =raw_piece.decode('utf-8', errors='backslashreplace')
        piece = piece.replace(' ', '.')
        pieces.append(f'[{piece}]')

    print("\n--- TOKEN VISUALIZATION ---")

    print("".join(pieces))

#command line argument

parser = argparse.ArgumentParser(
    description='Analyse text files using tokenization'
)

parser.add_argument('file', help='Path to the text file')
parser.add_argument('--encoding', default='cl100k_base', help='Tokenizer encoding')
parser.add_argument('--viz', action='store_true', help='visualize token splits')

#main program

args = parser.parse_args()
enc = tiktoken.get_encoding(args.encoding)

with open(args.file, 'r', encoding='utf-8') as f:
    text = f.read()
#done logics

analyses(text)
compare_normalization(text)
if args.viz:
    visualize(text)