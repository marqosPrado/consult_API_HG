ATUALIZACAO = 300

def chave():
    HG_API_KEY = "7cea6a0c"
    return HG_API_KEY.join(HG_API_KEY.split())

def color_red():
    color = "\033[1;31m"
    return color

def color_green():
    color = "\033[0;32m"
    return color

def color_white():
    color = "\u001b[37m"
    return color

def reset():
    reset = "\033[0;0m"
    return reset