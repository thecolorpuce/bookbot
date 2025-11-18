def get_num_words():    
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        num_words = file_contents.split()
        print(f"Found {len(num_words)} total words")

def count_unique_characters():
    counts = {}
    with open('books/frankenstein.txt') as f:
        text = f.read().lower()

    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
        
    return counts

        