
def insert_document_in_index(ix, document):
    data = document
    if not isinstance(data ,dict):
        data = data.__dict__

    writer = ix.writer()
    writer.add_document(**data)
    writer.commit()

def update_document_in_index(ix, document):
    data = document
    if not isinstance(data ,dict):
        data = data.__dict__
    writer = ix.writer()
    ix.update_document(data)
    writer.commit()

def remove_document_in_index(ix, id_field, id_value):
    writer = ix.writer()
    ix.delete_by_term(id_field, id_value)
    writer.commit()
    
