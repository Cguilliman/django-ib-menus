from django.db import models

from mptt.models import TreeManager


__all__ = ("BaseMenuManager", )


class BaseMenuManager(TreeManager):
    
    def get_queryset(self):
        """Filter by position"""
        self.position = self.model._position

        if self.position:
            return super().get_queryset().filter(
                position=self.position)

        return super().get_queryset()

    def get_by_position(self, position):
        """Get objects by position"""
        return self.get_queryset().filter(position=position)
