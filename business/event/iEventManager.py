from abc import abstractmethod as interface
from entity.event import Event
from entity.user import User


class IEventManager:
    """Olay iş katmanı için gerekli olan metotların imzalarını tutar

    @category: Manager, Business"""

    @interface
    def insert(self, event: Event) -> bool:
        raise NotImplementedError("This is not implemented 'insert' from IEventManager")

    @interface
    def update(self, event: Event) -> bool:
        raise NotImplementedError("This is not implemented 'update' from IEventManager")

    @interface
    def delete(self, event: Event) -> bool:
        raise NotImplementedError("This is not implemented 'delete' from IEventManager")

    @interface
    def get_all_events(self, user: User) -> list[Event]:
        raise NotImplementedError(
            "This is not implemented 'get_all_events' from IEventManager"
        )

    @interface
    def get_event_id(self, date: str, start: str, finish: str):
        raise NotImplementedError(
            "This is not implemented 'get_event_id' from IEventManager"
        )

    @interface
    def is_event(self, event: Event) -> Event:
        raise NotImplementedError(
            "This is not implemented 'is_event' from IEventManager"
        )
