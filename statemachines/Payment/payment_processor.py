import asyncio
from payment_machine import PaymentState, PaymentEvent, transition

class PaymentProcessor:
    def __init__(self):
        # Estado inicial
        self.state = PaymentState.IDLE

    async def process_payment(self, amount):
        # 1. Pasar a estado LOADING
        self.state = transition(self.state, PaymentEvent.PAY)
        print(f"[Payment]: Procesando pago de ${amount}...")

        try:
            # Simulamos la llamada a la API
            await self._api_call()
            # 2. Si tiene éxito, pasar a SUCCESS
            self.state = transition(self.state, PaymentEvent.RESOLVE)
        except Exception:
            # 3. Si falla, pasar a ERROR
            self.state = transition(self.state, PaymentEvent.REJECT)

    async def _api_call(self):
        """Simula una llamada de red que falla después de 1 segundo"""
        await asyncio.sleep(1)
        # Forzamos un error para ver el cambio de estado a ERROR
        raise Exception("Network Error")

    # Métodos Helper (Getters de estado)
    def get_is_loading(self):
        return self.state == PaymentState.LOADING

    def get_is_error(self):
        return self.state == PaymentState.ERROR

    def get_is_success(self):
        return self.state == PaymentState.SUCCESS