def parse_member_id(member_id):
    if not isinstance(member_id, str):
        return None
    parts = member_id.split('-')
    if len(parts) != 2:
        return None
    member_type, number = parts[0].strip(), parts[1].strip()
    if not member_type or not number.isascii() or not number.isdigit():
        return None
    return member_type.upper(), int(number)

def total_fine(days_csv):
    if not isinstance(days_csv, str):
        return 0
    fine = 0
    for part in days_csv.split(','):
        part = part.strip()
        if not part.isascii() or not part.lstrip('-').isdigit():
            continue
        d = int(part)
        if d > 14:
            fine += (d - 14) * 2
    return fine


def shelf_code(title):
    if not isinstance(title, str):
        return ""
    words = title.split()
    if len(words) < 2:
        return ""
    return (words[0][0] + words[1][0]).upper()

def main():
    print("==== Running parse_member_id ====")
    user_input = input("Enter a member ID (e.g. STU-1023): ")
    result = parse_member_id(user_input)
    print("Member Type and Number:", result)

    print("\n==== Running total_fine ====")
    user_input = input("Enter days kept for each book as CSV (e.g. 10,20,30): ")
    result = total_fine(user_input)
    print("Total Fine:", result)

    print("\n==== Running shelf_code ====")
    user_input = input("Enter a book title with at least two words: ")
    result = shelf_code(user_input)
    print("Shelf Code:", result)

if __name__ == "__main__":
    main()
