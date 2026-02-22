#file utils. handles all the files and stuff

#function for making sure the file exists.
def ensure_file(path):
    try:
        open(path, 'r').close()
    except FileNotFoundError:
        open(path, "w").close()

def split_content_and_data(text):
    lines = text.strip().split("\n")
    content_lines = []
    data_lines = []
    #varaibale 
    i = 0
    while i < len(lines):
        if lines[i].startswith("Word Count:"):
            #data pair  found
            #so word count
            #and last updated
            data_lines.append(lines[i])
            if i + 1 < len(lines):
                data_lines.append(lines[i + 1])
            i += 2#skip lines we just did
        else:
            content_lines.append(lines[i])
            i += 1#move to next line

        return "\n".join(content_lines).strip(), "\n".join(data_lines).strip()
    
def read_document(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

        content, _ = split_content_and_data(text)
        return content

def add_content(path, new_text):
    with open (path, "r", encoding="utf-8") as f:
        text = f.read()
    
    content, data = split_content_and_data(text)

    updated = content + "\n" + new_text.strip() + "\n"

    if data:
        updated += "\n" + data + "\n"

    with open(path, "w", encoding="utf-8") as f:
        f.write(updated)

def updated_data(path, word_count, time_stamp):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    content, data = split_content_and_data(text)

    new_block = f"Word Count: {word_count}\n Last updates {time_stamp}"

    if data:
        updated_data = data + "\n\n" + new_block
    else:
        updated_data = new_block
    
    final_text = content + "\n\n" + updated_data + "\n"

    with open(path, "w", encoding="utf-8") as f:
        f.write(final_text)

