from enum import Enum, auto

class PaymentState(Enum):
    IDLE = "IDLE"
    LOADING = "LOADING"
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"

class PaymentEvent(Enum):
    PAY = "PAY"
    RESOLVE = "RESOLVE"
    REJECT = "REJECT"

machine = {
    PaymentState.IDLE: {
        PaymentEvent.PAY: PaymentState.LOADING
    },
    PaymentState.LOADING: {
        PaymentEvent.RESOLVE: PaymentState.SUCCESS,
        PaymentEvent.REJECT: PaymentState.ERROR
    }
}

def transition(current_state, event):
    """Lógica de transición sin IFs anidados"""
    # Si el estado actual no existe en la máquina, se queda igual
    if current_state not in machine:
        return current_state
        
    # Busca el siguiente estado basado en el evento
    next_state = machine[current_state].get(event)
    
    # Si hay un siguiente estado definido, lo devuelve; si no, devuelve el actual
    return next_state 