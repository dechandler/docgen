
# Docgen

description: Document renderer

// comment!


## Capabilities

- Generates a document based on a template and a data source


###### Data sources

- MarkYaml (markdown/yaml hybrid)


###### Output formats

- Markdown
- docx
- pdf (from docx)


## Usage Notes

- Docx templates created in LibreOffice Writer cause an error in the output file, so it needs to be opened in Writer to repair before generating a pdf. Editing the file after creation works though, so you can start with a docx file initially created by MS Word or Google Docs, and edit in Writer.


## MarkYaml format

- Markdown-like header tags are parsed into nested dictionaries
- Body text is parsed as YAML and attached to its header
- Comment with `//` at the start of a line
