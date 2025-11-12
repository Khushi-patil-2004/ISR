import os
import string

folder = "/content/drive/MyDrive/inverted/inverted"
files = []
for f in os.listdir(folder):
  if f.endswith(".txt"):
    files.append(f)

inverted_index = {}
for file in files:
  with open(os.path.join(folder,file),'r',encoding='utf-8') as f:
    text = f.read().lower()
    for p in string.punctuation:
      text = text.replace(p," ")
    words = text.split()

    for word in set(words):
      if word not in inverted_index:
        inverted_index[word] = [file]
      else:
        inverted_index[word].append(file)

print("inverted Index Created")

count = 0

for term, docs in inverted_index.items():
    print(term, "-->", docs)
    count += 1
    if count == 10:   # stop after first 10 terms
        break

query = input("Enter a query term: ").lower().strip()

if query in inverted_index:
    print(f"Documents containing '{query}':")
    for doc in inverted_index[query]:
        print(f" - {doc}")
else:
    print(f"No documents found containing the term '{query}'.")