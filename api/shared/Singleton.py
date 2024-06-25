from abc import ABCMeta, abstractmethod


class SingletonMeta(ABCMeta):
  """
    Metaclass for creating singleton classes.

    Usage:
        class YourClass(metaclass=SingletonMeta):
            pass

    This metaclass ensures that only one instance of the class is created.
  """

  _instance = None

  def __call__(cls, *args, **kwargs):
    """
        Override the default __call__ method to create a singleton instance.

        Args:
            cls: The class being instantiated.
            *args: Positional arguments for the class constructor.
            **kwargs: Keyword arguments for the class constructor.

        Returns:
            The singleton instance of the class.
    """
    if cls._instance is None:
      cls._instance = super().__call__(*args, **kwargs)
    return cls._instance
