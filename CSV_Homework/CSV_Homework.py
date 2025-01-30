#import Files_Homework.Files_Homework
import csv
import string
from collections import Counter

def read_text_file(filename):
    """Read text from a file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def preprocess_text(text):
    """Convert text to lowercase and remove punctuation."""
    text = text.lower()
    return text.translate(str.maketrans('', '', string.punctuation))


def count_words(text):
    """Count occurrences of each word."""
    words = text.split()
    return Counter(words)


def count_letters(text):
    """Count occurrences of each letter, uppercase letters, and calculate percentage."""
    text_no_spaces = text.replace(" ", "")
    total_letters = len(text_no_spaces)
    letter_counts = Counter(text_no_spaces)
    uppercase_counts = Counter(c for c in text if c.isupper())

    letter_data = []
    for letter, count in letter_counts.items():
        count_upper = uppercase_counts.get(letter, 0)
        percentage = (count / total_letters) * 100 if total_letters > 0 else 0
        letter_data.append([letter, count, count_upper, round(percentage, 2)])

    return letter_data


def write_csv_word_count(word_counts, filename):
    """Write word count data to a CSV file."""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Word', 'Count'])
        writer.writerows(word_counts.items())


def write_csv_letter_count(letter_counts, filename):
    """Write letter count data to a CSV file."""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Letter', 'Count_All', 'Count_Uppercase', 'Percentage'])
        writer.writerows(letter_counts)


def main():
    """Main execution function."""
    text = read_text_file('articles.txt')
    processed_text = preprocess_text(text)

    word_counts = count_words(processed_text)
    letter_counts = count_letters(text)

    write_csv_word_count(word_counts, 'word_count.csv')
    write_csv_letter_count(letter_counts, 'letter_count.csv')


if __name__ == "__main__":
    main()
