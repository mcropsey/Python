import os
import gzip
import tarfile
import zipfile
import io

def process_file(file_path, display_name, search_terms, out, separator):
    """
    Open and process a file, handling various compression formats.
    
    If an error occurs during opening or reading any file, an error message
    is printed to the console.
    """
    # Check if the file is a tar archive (including tar.gz/tgz, etc.)
    if tarfile.is_tarfile(file_path):
        try:
            print(f"Processing tar file: {file_path}")
            with tarfile.open(file_path, "r:*") as tar:
                for member in tar.getmembers():
                    if member.isfile():
                        f = tar.extractfile(member)
                        if f is None:
                            print(f"Error: Could not extract member '{member.name}' from tar file '{file_path}'")
                            continue
                        # Wrap the binary stream to text.
                        text_file = io.TextIOWrapper(f, errors="ignore")
                        for line in text_file:
                            if any(term.lower() in line.lower() for term in search_terms):
                                out.write(separator + "\n")
                                out.write(f"File: {display_name} (Archive member: {member.name})\n")
                                out.write(line.rstrip() + "\n")
                                out.write(separator + "\n\n")
                        text_file.close()
        except Exception as e:
            print(f"Error opening tar file '{file_path}': {e}")

    # Check if the file is a zip archive.
    elif zipfile.is_zipfile(file_path):
        try:
            print(f"Processing zip file: {file_path}")
            with zipfile.ZipFile(file_path, 'r') as z:
                for info in z.infolist():
                    if not info.is_dir():
                        try:
                            with z.open(info) as f:
                                text_file = io.TextIOWrapper(f, errors="ignore")
                                for line in text_file:
                                    if any(term.lower() in line.lower() for term in search_terms):
                                        out.write(separator + "\n")
                                        out.write(f"File: {display_name} (Archive member: {info.filename})\n")
                                        out.write(line.rstrip() + "\n")
                                        out.write(separator + "\n\n")
                                text_file.close()
                        except Exception as inner_e:
                            print(f"Error opening member '{info.filename}' in zip file '{file_path}': {inner_e}")
        except Exception as e:
            print(f"Error opening zip file '{file_path}': {e}")

    # Check if the file is a gzip file (and not a tar archive).
    elif file_path.endswith('.gz'):
        try:
            print(f"Processing gzip file: {file_path}")
            with gzip.open(file_path, "rt", errors="ignore") as f:
                for line in f:
                    if any(term.lower() in line.lower() for term in search_terms):
                        out.write(separator + "\n")
                        out.write(f"File: {display_name}\n")
                        out.write(line.rstrip() + "\n")
                        out.write(separator + "\n\n")
        except Exception as e:
            print(f"Error opening gzip file '{file_path}': {e}")

    # Otherwise, assume it's a regular text file.
    else:
        try:
            print(f"Processing regular text file: {file_path}")
            with open(file_path, "r", errors="ignore") as f:
                for line in f:
                    if any(term.lower() in line.lower() for term in search_terms):
                        out.write(separator + "\n")
                        out.write(f"File: {display_name}\n")
                        out.write(line.rstrip() + "\n")
                        out.write(separator + "\n\n")
        except Exception as e:
            print(f"Error opening file '{file_path}': {e}")

def main():
    # Read search terms from search-items.txt.
    search_terms_file = "search-items.txt"
    try:
        with open(search_terms_file, "r") as f:
            # Only include non-empty, stripped lines.
            search_terms = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading '{search_terms_file}': {e}")
        return

    # Open the output file (overwriting it if it exists).
    output_file = "logparse-results.txt"
    try:
        out = open(output_file, "w")
    except Exception as e:
        print(f"Error opening '{output_file}' for writing: {e}")
        return

    separator = "*" * 80

    # Define the logs directory (should be in the same folder as this script).
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        print(f"Logs directory '{logs_dir}' does not exist.")
        out.close()
        return

    # Loop through all files in the logs directory.
    for filename in os.listdir(logs_dir):
        file_path = os.path.join(logs_dir, filename)
        if os.path.isfile(file_path):
            process_file(file_path, filename, search_terms, out, separator)

    out.close()
    print(f"Search complete. Results written to '{output_file}'")

if __name__ == "__main__":
    main()
