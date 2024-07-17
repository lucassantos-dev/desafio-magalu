from enum import Enum


class ChannelsEnums(Enum):
    SMS = "SMS"
    EMAIL = "EMAIL"
    PUSH = "PUSH"
    WHATSAPP = "WHATSAPP"

    def __str__(self):
        return self.value


class StatusEnums(Enum):
    PENDING = "PENDING"
    CANCELLED = "CANCELLED"
    SENT = "SENT"
    ERROR = "ERROR"
    SUCCESS = "SUCCESS"

    def __str__(self):
        return self.value
