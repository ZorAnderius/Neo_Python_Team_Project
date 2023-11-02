from datetime import datetime
from colorama import Fore
import uuid

from .Title import Title
from .Body import Body
from .Tag import Tag


class Note:
    def __init__(self, name, title="", body="", *tags):
        self.__name = name
        new_title = Title(title)
        if new_title.title and type(new_title.title) is str:
            self.__title = new_title
        else:
            self.__title = None

        new_body = Body(body)
        if new_body.body and type(new_body.body) is str:
            self.__body = new_body
        else:
            self.__body = None
        if tags:
            self.__tags = [Tag(tag) for tag in tags]
        else:
            self.__tags = []
        self.__id = uuid.uuid1()
        self.__created_at = datetime.today().strftime("%a %d %b %Y, %I:%M%p")

    @property
    def title(self):
        return self.__title

    @title.setter
    def set_title(self, title):
        self.__title = Title(title)

    @property
    def body(self):
        return self.__body

    @body.setter
    def set_body(self, body):
        new_body = Body(body)
        if new_body.body and type(new_body.body) is str:
            self.__body = new_body
        else:
            self.__body = None

    @property
    def created_at(self):
        return self.__created_at

    @property
    def tags(self):
        return self.__tags

    @tags.setter
    def set_tags(self, tags):
        if tags:
            self.__tags = tags
        else:
            self.__tags = []

    @property
    def id(self):
        return self.__id

    def add_title(self, title: str):
        new_title = Title(title)
        if new_title and type(new_title) is Title:
            self.__title = new_title

    def add_body(self, body: str):
        new_body = Body(body)
        if new_body.body and type(new_body.body) is str:
            self.__body = new_body
        else:
            self.__body = None

    def add_tag(self, tag: str):
        new_tag = Tag(tag)
        if new_tag.tag in self.__tags:
            raise ValueError(Fore.YELLOW + f"Duplicate tag {new_tag}")
        elif new_tag.tag:
            self.__tags.append(new_tag)

    def __str__(self):
        tags_str = None
        if self.tags and type(self.tags) is list:
            tags_str = ", ".join(tag.tag for tag in self.__tags)
        if self.__title is None and tags_str is None and self.__body is None:
            return f"Title: Add title\nNote: Add note\nCreated: {self.__created_at}\n"
        if tags_str is None and not self.__body:
            return f"Title: Add title\nNote: Add note\nCreated: {self.__created_at}\n"
        if self.__title is None and not self.__body:
            return f"Title: Add title\nTags: {tags_str}\nNote: Add note\nCreated: {self.__created_at}\n"
        if self.__title is None and tags_str is None:
            return (
                f"Title: Add title\nNote: {self.__body}\nCreated: {self.__created_at}\n"
            )
        if self.__title is None:
            return f"Title: Add title\nTags: {tags_str}\nNote: {body}\nCreated: {self.__created_at}\n"
        if not self.__body:
            return f"Title: {self.__title}\nTags: {tags_str}\nNote: Add note\nCreated: {self.__created_at}\n"
        if tags_str is None:
            return f"Title: {self.__title}\nNote: {self.__body}\nCreated: {self.__created_at}\n"

        return f"Title: {self.__title}\nTags: {tags_str}\nNote: {body}\nCreated: {self.__created_at}\n"


if __name__ == "__main__":
    new_title = "Bargains"
    body = "fkfkdkfkkfkkfkfkkfkkdfkmmvmfd"
    notes = Note()
    print(notes)
    notes.add_body(body)
    print(notes)
    notes.add_title(new_title)
    print(notes)
    notes.add_tag("zoo")
    notes.add_tag("moo")
    notes.add_tag("doo")
    print(notes)
