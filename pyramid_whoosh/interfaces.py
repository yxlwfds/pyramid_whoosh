from zope.interface.interface import Interface, Attribute

class IDocumentSchema(Interface):
    """Interface for adapting a model entity to a view context."""

    whoosh_schema = Attribute('A dictionnary of field to register as schema')


    def get_all_documents():
        """Return an iterator of objects to be indexed"""

    def get_document(id):
        """get data respecting the key of the schema"""
