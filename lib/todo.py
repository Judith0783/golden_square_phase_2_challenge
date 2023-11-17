def includes_to_do(text):
    if "COMPLETED" in text:
        raise Exception("Already completed")
    elif "#TODO" in (text):
        return True
    else:
        return False