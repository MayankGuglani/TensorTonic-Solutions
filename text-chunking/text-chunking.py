def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    
    arr = []
    step = chunk_size - overlap
    
    for i in range(0, len(tokens), step):
        if i + chunk_size >= len(tokens):
            arr.append(tokens[i:])
            break
        arr.append(tokens[i:i+chunk_size])
    
    return arr