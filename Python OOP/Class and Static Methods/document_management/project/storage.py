from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __id_finder(self, entities, entity_id):
        for entity in entities:
            if entity_id == entity.id:
                return entity

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.__id_finder(self.categories, category_id)
        category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.__id_finder(self.topics, topic_id)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = self.__id_finder(self.documents, document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.__id_finder(self.categories, category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__id_finder(self.topics, topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__id_finder(self.documents, document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.__id_finder(self.documents, document_id)
        return repr(document)

    def __repr__(self):
        result = ''
        for document in self.documents:
            result += repr(document) + '\n'
        return result.strip() + ' '