from sqlalchemy import true


def correo(crr):
    if "@" in crr:
        return True
    else:
        return False
