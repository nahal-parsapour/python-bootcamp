from text_tools import remove_extra_spaces, remove_punctuation
from text_tools import word_count, char_frequency

def main():
    sample = "Hello, world!!   This is a   sample text, from Week 7.   "
    print(f"Original text: {sample}")

    step1 = remove_punctuation(sample)
    print(f"After removing punctuation: {step1}")

    step2 = remove_extra_spaces(step1)
    print(f"After removing extra spaces: {step2}")

    step3 = word_count(step2)
    print(f"After counting word count: {step3}")

    step4 = char_frequency(step2)
    print(f"After counting char frequency: {step4}")

if __name__ == "__main__":
    main()
