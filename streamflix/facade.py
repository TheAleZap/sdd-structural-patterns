
from .payments import PaymentProcessor
from .catalog import Video


class StreamingFacade:
    """
    Simplified entry point for the mobile/web client: it never talks to
    payment processors or videos directly, only to this facade.
    """

    def __init__(self, payment_processor: PaymentProcessor):
      # TODO: store the payment processor and start unsubscribed
      self._payment_processor = payment_processor
      self._is_subscribed = False

    def subscribe(self, monthly_fee: float) -> str:
      # TODO: charge `monthly_fee` through the payment processor, mark the
      # account as subscribed, and return the processor's receipt string.
      receipt = self._payment_processor.pay(monthly_fee)
      self._is_subscribed = True
      return receipt

    def watch(self, video: Video) -> str:
      # TODO: if not subscribed, raise PermissionError("subscription required").
      # Otherwise delegate to `video.play()` and return its result.
      if not self._is_subscribed:
          raise PermissionError("subscription required")
      return video.play()
