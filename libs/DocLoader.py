



class DocLoader:
    """
    Contains the document being inspected and the content generated by the user
    """
    def __init__(self):
        self.chunk_size = 500
        self.chunk_overlap = 20
    
    def get_doc_from_url(url: str) -> Document:
        # get document from url, from website articles
        # add source to doc metadata
        pass

    def get_doc_from_pdf(file: str) -> Document:
        # get document from pdf files
        # add source to doc metadata
        pass

    def get_doc_from_raw_text(text: str) -> Document:
        # get document from copy and pasted text in the input box
        # add source to doc metadata
        pass

    def  split_clean_doc(doc: Document) -> Document
        # clean doc of extra new lines and spaces

    def split_doc(doc: Document): -> Document
        # split documents from one big document