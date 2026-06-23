with open(
    "cleaned_data/annual+report_2024.txt",
    "r",
    encoding="utf-8"
)as f:
    text=f.read()


words=text.split()
chunk_size=500
overlap=50
chunks=[]
for i in range(0,len(words),chunk_size-overlap):
    chunk=words[i:i+chunk_size]

    chunk_text=" ".join(chunk)

    chunks.append(chunk_text)
print("Number of chunks: ",len(chunks))

print(chunks[0][:500])