from L8text import generate_char_signatures, genetrate_single_signature, genetrate_inverted_file

def l8sample():
    doc_array = [
        (1, "adfmnz"),
        (2, "bcm"),
        (3, "acy"),
        (40, "eyz"),
        (50, "acm"),
    ]
    length = 5

    generate_char_signatures(doc_array, length)
    genetrate_inverted_file(doc_array)



