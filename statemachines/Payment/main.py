import asyncio
from payment_processor import PaymentProcessor

async def bootstrap():
    processor = PaymentProcessor()

    print("--- Iniciando Simulación de Pago ---")
    
    # Ejecutamos el proceso de pago
    await processor.process_payment(100)

    print("\n--- Estado Final del Sistema ---")
    print(f"¿Cargando? (isLoading): {processor.get_is_loading()}")
    print(f"¿Éxito? (isSuccess): {processor.get_is_success()}")
    print(f"¿Error? (isError): {processor.get_is_error()}")

    # Verificación de inconsistencia (CRITICAL)
    if processor.get_is_loading() and processor.get_is_error():
        print("\n[CRITICAL]: El sistema está en un estado inconsistente: Cargando y con Error al mismo tiempo.")

if __name__ == "__main__":
    asyncio.run(bootstrap())