from abc import abstractmethod as interface
from entity.eventType import EventType


class IEventTypeManager:
    """Olay Tipi iş katmanı için gerekli olan metotların imzalarını tutar

    @category: Manager, Business"""

    @interface
    def insert(self, event_type: EventType):
        raise NotImplementedError(
            "This is not implemented 'insert' from IEventTypeManager"
        )

    @interface
    def update(self, old_name: str, new_name: str):
        raise NotImplementedError(
            "This is not implemented 'update' from IEventTypeManager"
        )

    @interface
    def get_event_type_id(self, event_name: str):
        raise NotImplementedError(
            "This is not implemented 'get_event_type_id' from IEventTypeManager"
        )
    
    @interface
    def get_event_type_name(self, event_name: str):
        raise NotImplementedError(
            "This is not implemented 'get_event_type_id' from IEventTypeManager"
        )

    @interface
    def get_all_event_types(self):
        raise NotImplementedError(
            "This is not implemented 'get_all_event_types' from IEventTypeManager"
        )

    @interface
    def delete(self, event_type: EventType):
        raise NotImplementedError(
            "This is not implemented 'delete' from IEventTypeManager"
        )

    @interface
    def is_event_type(self, event_type_name: str):
        raise NotImplementedError(
            "This is not implemented 'delete' from IEventTypeManager"
        )
