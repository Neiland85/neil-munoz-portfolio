import logging
import os

try:
    import structlog  # type: ignore
except ImportError:
    # Fallback if structlog is not installed
    structlog = None


def setup_logging():
    """
    Configura el logging estructurado para la aplicación.
    En producción emite JSON. En local emite texto coloreado.
    """
    # Leer de las variables de entorno (similares a tu .env)
    if structlog is None:
        # Fallback to standard logging if structlog is missing
        logging.basicConfig(level=logging.INFO)
        return logging.getLogger("app")

    env = os.getenv("APP_ENV", "local")
    log_level_str = os.getenv("LOG_LEVEL", "INFO").upper()

    # Mapeo de niveles de string a constantes de logging
    getattr(logging, log_level_str, logging.INFO)

    # Procesadores comunes para ambos entornos (añaden fecha, nivel, etc.)
    shared_processors = [
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
    ]

    # Renderizador condicional según el entorno
    if env == "production":
        renderer = structlog.processors.JSONRenderer()
    else:
        renderer = structlog.dev.ConsoleRenderer(colors=True)

    structlog.configure(
        processors=shared_processors + [renderer],
        wrapper_class=structlog.stdlib.BoundLogger,
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=False,
    )

    # Opcional: silenciar logs muy ruidosos de librerías de terceros
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)

    return structlog.get_logger()


# Instancia global lista para ser importada en el resto de la app
logger = setup_logging()
