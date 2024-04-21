def designerPdfViewer(h, word):
    size = len(word)
    maxHeight = 0 

    for ch in word:
        maxHeight = max(maxHeight, h[ord(ch)-97])
        
    return size * maxHeight