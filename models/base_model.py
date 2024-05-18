#!/usr/bin/python3
"""This module defines the BaseModel class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Represents the base class for all models in the HBnB project."""
    def __init__(self, *args, **kwargs):
        """Initialize new BaseModel."""
        cls_ = '__class__'
        update = 'updated_at'
        create = 'created_at'

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for KEY_, Val in kwargs.items():
                if KEY_ != cls_:
                    if KEY_ in [update, create]:
                        setattr(self, KEY_, datetime.fromisoformat(Val))
                    else:
                        setattr(self, KEY_, Val)

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        pstr_ = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return pstr_

    def save(self):
        """Update updated_at with current time when instance is modified."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert the instance into dictionary format."""
        drictobj = self.__dict__.copy()
        drictobj['updated_at'] = self.updated_at.isoformat()
        drictobj["created_at"] = self.created_at.isoformat()
        drictobj['__class__'] = self.__class__.__name__

        return drictobj
