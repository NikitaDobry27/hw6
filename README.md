This script sorts files in a directory into appropriate folders. The script identifies the type of file by its extension and moves it to a folder that corresponds to its category.

## Running the script

To run the script, enter the following command in the terminal:

```
python sort_files.py folder_path

```

Replace `folder_path` with the path to the folder that you want to sort.

## File types and categories

The following file types are supported:

- Images (jpg, jpeg, png, gif, svg)
- Videos (avi, mp4, mov, mkv)
- Documents (doc, docx, pdf, xls, xlsx, ppt, pptx)
- Archives (zip, tar, gz, rar)

## Output

After running the script, the following output will be generated:

- A list of moved files
- A list of known file formats
- A list of unknown file formats

## Note

Empty folders that are not part of the supported file categories will be deleted.
