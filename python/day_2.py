# Day 2 — Python Collections for RAG Implementation
# =================================================
# Topics:
# - Lists
# - Tuples
# - Sets
# - Dictionaries
# - Indexing
# - Slicing
# - Dictionary methods
# - List + dictionary structures used in RAG

# -------------------------
# 1. LISTS
# -------------------------

documents = ["doc1", "doc2", "doc3"]

print(documents)
print(documents[0])       # First item
print(documents[-1])      # Last item

# Change an item
documents[0] = "new_doc"

# Add items
documents.append("doc4")
documents.extend(["doc5", "doc6"])
documents.insert(1, "docX")

# Remove items
documents.remove("doc2")
documents.pop()           # Remove last item
documents.pop(1)          # Remove by index

print(documents)

# Useful operations
print(len(documents))
print("doc3" in documents)

# Slicing
chunks = ["c1", "c2", "c3", "c4", "c5"]

print(chunks[:3])
print(chunks[2:])
print(chunks[-2:])
print(chunks[::-1])

# Useful methods
print(chunks.index("c2"))
print(chunks.count("c2"))

chunks.sort()
chunks.reverse()

copied_chunks = chunks.copy()

# -------------------------
# 2. TUPLES
# -------------------------

document_info = ("policy.pdf", 5)

print(document_info)
print(document_info[0])
print(document_info[1])

# Tuples are immutable.
# document_info[0] = "faq.pdf"  # ERROR

print(document_info.count("policy.pdf"))
print(document_info.index(5))

# Tuple unpacking
source, page = document_info

print(source)
print(page)

# Functions can return multiple values
def get_document_info():
    return "policy.pdf", 5

source, page = get_document_info()

print(source)
print(page)


# -------------------------
# 3. SETS
# -------------------------

sources = {"policy.pdf", "faq.pdf", "policy.pdf"}

print(sources)  # Duplicates are removed.

sources.add("refund.pdf")
sources.discard("unknown.pdf")

print("policy.pdf" in sources)

# List -> Set removes duplicates
source_list = [
    "policy.pdf",
    "policy.pdf",
    "faq.pdf"
]

unique_sources = set(source_list)
print(unique_sources)

# Set operations
a = {"a.pdf", "b.pdf"}
b = {"b.pdf", "c.pdf"}

print(a | b)  # Union
print(a & b)  # Intersection
print(a - b)  # Difference
print(a ^ b)  # Symmetric difference

# Empty set
empty_set = set()
empty_dictionary = {}


# -------------------------
# 4. DICTIONARIES
# -------------------------

document = {
    "text": "Patients can cancel appointments 24 hours before.",
    "page": 5,
    "source": "policy.pdf"
}

# Access
print(document["text"])
print(document.get("text"))

# Safe access when a key may not exist
print(document.get("author"))
print(document.get("author", "Unknown"))

# Add / update
document["document_id"] = "doc123"
document["page"] = 6

document.update({
    "clinic_id": "clinic123",
    "user_id": "user456"
})

# Dictionary methods
print(document.keys())
print(document.values())
print(document.items())

for key, value in document.items():
    print(key, value)

# Check whether a key exists
if "source" in document:
    print("Source exists")

# Remove
document.pop("page")

# Copy
new_document = document.copy()

# setdefault
new_document.setdefault("page", 1)

print(new_document)


# -------------------------
# 5. LIST + DICTIONARY
# -------------------------
# This structure is extremely important for RAG.

chunks = [
    {
        "text": "Patients can cancel within 24 hours.",
        "page": 5,
        "source": "policy.pdf"
    },
    {
        "text": "Refunds are processed within 7 days.",
        "page": 8,
        "source": "refund.pdf"
    }
]

print(chunks[0])
print(chunks[0]["text"])
print(chunks[0]["page"])


# -------------------------
# 6. NESTED DATA
# -------------------------

results = [
    {
        "score": 0.92,
        "document": {
            "source": "policy.pdf",
            "page": 5
        }
    }
]

print(results[0]["score"])
print(results[0]["document"]["source"])


# -------------------------
# Day 2 Key Reminder
# -------------------------
# List      = ordered, mutable collection
# Tuple     = ordered, immutable collection
# Set       = unique values
# Dictionary = key-value data
#
# Very important for RAG:
# list of dictionaries
