def main():
    sentence=input("please enter a sentence: ")
    words=sentence.split()
    print(words)
    max_len=max(len(word)for word in words)
    longest_word=[word for word in words if len(word)==max_len]
    uniqe_longest=list(dict.fromkeys(longest_word))
    print("Longest word(s):")
    for word in uniqe_longest:
        print(f"{word}({len(word)} letters)")

if __name__=="__main__":
    main()