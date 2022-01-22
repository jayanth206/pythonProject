def search(pat, word):
    n = len(pat)
    m = len(word)

    for i in range(m-n+1):
        j=0

        while(j<n):
            if(word[i+j]!=pat[j]):
                break
            j+=1
        if(j==n):
            print("pattern found at index", i)

if __name__ == '__main__':
    word = "AABAACAADAABAAABAA"
    pat = "AABA"
    search(pat, word)